from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query, UploadFile, File
from google.cloud import firestore  # type: ignore

from ...config import get_settings
from ...firestore.client import get_client
from ...models.property_schemas import (
    PropertyCreate,
    PropertyOut,
    PropertyPatch,
    UnitCreate,
    UnitOut,
    UnitPatch,
    BedCreate,
    BedOut,
    BedPatch,
)


router = APIRouter(prefix="/v1", tags=["properties"])

from google.cloud import storage  # type: ignore
from PIL import Image  # type: ignore
import io
import re


def require_auth(authorization: Optional[str] = Header(None)):
    settings = get_settings()
    if settings.api_token is None:
        return True
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ", 1)[1]
    if token != settings.api_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True


def _normalize_property_status(status: Optional[str]) -> str:
    if status == "Operational":
        return "Operational"
    return "Non Operational"


def _normalize_unit_status(status: Optional[str]) -> str:
    if status == "Non Operational":
        return "Non Operational"
    return "Operational"


def _ensure_property_operational(db: firestore.Client, property_id: str) -> dict:
    snap = db.collection("properties").document(property_id).get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail={"code": "PROPERTY_NOT_FOUND", "message": "Property not found", "target": {"type": "property", "id": property_id}})
    d = snap.to_dict() or {}
    if d.get("status") != "Operational":
        raise HTTPException(status_code=423, detail={
            "code": "PROPERTY_LOCKED_NON_OPERATIONAL",
            "message": "Changes are blocked. Property is Non-Operational. Toggle to Operational to proceed.",
            "target": {"type": "property", "id": property_id},
            "suggested_action": "toggle_status_to_operational",
        })
    return d


@router.post("/properties", response_model=PropertyOut, dependencies=[Depends(require_auth)])
def create_property(payload: PropertyCreate) -> PropertyOut:
    db = get_client()
    data = payload.dict()
    # Global uniqueness on property_name (case-insensitive, trimmed)
    name_key = " ".join(payload.property_name.split()).strip().lower()
    exists = db.collection("properties").where("name_key", "==", name_key).limit(1).stream()
    if any(True for _ in exists):
        raise HTTPException(status_code=409, detail={
            "code": "DUPLICATE_PROPERTY_NAME",
            "message": f"Property name '{payload.property_name}' already exists.",
            "target": {"type": "property", "name": payload.property_name},
            "suggested_action": "choose_unique_name",
        })
    data["name_key"] = name_key
    data["created_at"] = firestore.SERVER_TIMESTAMP
    doc_ref = db.collection("properties").document()
    doc_ref.set(data)
    snap = doc_ref.get()
    saved = snap.to_dict() or {}
    created_at = saved.get("created_at") or datetime.utcnow()
    return PropertyOut(id=doc_ref.id, created_at=created_at, **payload.dict())


@router.get("/properties", response_model=List[PropertyOut], dependencies=[Depends(require_auth)])
def list_properties(status: Optional[str] = Query(None)) -> List[PropertyOut]:
    try:
        db = get_client()
        q = db.collection("properties")
        if status:
            q = q.where("status", "==", status)
        q = q.order_by("created_at", direction=firestore.Query.DESCENDING)

        results: List[PropertyOut] = []
        for doc in q.stream():
            d = doc.to_dict() or {}
            results.append(
                PropertyOut(
                    id=doc.id,
                    property_name=d.get("property_name"),
                    address=d.get("address"),
                    status=_normalize_property_status(d.get("status")),
                    unit_types=d.get("unit_types"),
                    created_at=d.get("created_at", datetime.utcnow()),
                )
            )
        return results
    except Exception as e:
        msg = f"Firestore list_properties failed: {type(e).__name__}: {e}"
        print(msg)
        raise HTTPException(status_code=500, detail={
            "code": "FIRESTORE_LIST_FAILED",
            "message": msg,
        })


@router.get("/properties/{property_id}", response_model=PropertyOut, dependencies=[Depends(require_auth)])
def get_property(property_id: str) -> PropertyOut:
    db = get_client()
    snap = db.collection("properties").document(property_id).get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="Property not found")
    d = snap.to_dict() or {}
    return PropertyOut(
        id=snap.id,
        property_name=d.get("property_name"),
        address=d.get("address"),
        status=_normalize_property_status(d.get("status")),
        unit_types=d.get("unit_types"),
        created_at=d.get("created_at", datetime.utcnow()),
    )


@router.patch("/properties/{property_id}", response_model=PropertyOut, dependencies=[Depends(require_auth)])
def update_property(property_id: str, patch: PropertyPatch) -> PropertyOut:
    db = get_client()
    doc_ref = db.collection("properties").document(property_id)
    snap = doc_ref.get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="Property not found")
    update = {k: v for k, v in patch.dict(exclude_unset=True).items()}
    current = snap.to_dict() or {}
    if current.get("status") == "Non Operational":
        forbidden_keys = set(update.keys()) - {"status"}
        if forbidden_keys:
            raise HTTPException(status_code=423, detail={"code": "PROPERTY_LOCKED_NON_OPERATIONAL", "message": "Property is Non-Operational; only status change is allowed", "target": {"type": "property", "id": property_id}})
    if "property_name" in update and update["property_name"]:
        name_key = " ".join(update["property_name"].split()).strip().lower()
        for doc in db.collection("properties").where("name_key", "==", name_key).stream():
            if doc.id != property_id:
                raise HTTPException(status_code=409, detail={
                    "code": "DUPLICATE_PROPERTY_NAME",
                    "message": f"Property name '{update['property_name']}' already exists.",
                    "target": {"type": "property", "name": update["property_name"]},
                })
        update["name_key"] = name_key
    if not update:
        d = current
        return PropertyOut(
            id=snap.id,
            property_name=d.get("property_name"),
            address=d.get("address"),
            status=d.get("status"),
            created_at=d.get("created_at", datetime.utcnow()),
        )
    doc_ref.update(update)
    snap = doc_ref.get()
    d = snap.to_dict() or {}
    return PropertyOut(
        id=snap.id,
        property_name=d.get("property_name"),
        address=d.get("address"),
        status=_normalize_property_status(d.get("status")),
        unit_types=d.get("unit_types"),
        created_at=d.get("created_at", datetime.utcnow()),
    )


@router.delete("/properties/{property_id}")
def delete_property(property_id: str, _: bool = Depends(require_auth)):
    db = get_client()
    prop_ref = db.collection("properties").document(property_id)
    if not prop_ref.get().exists:
        raise HTTPException(status_code=404, detail={"code": "PROPERTY_NOT_FOUND", "message": "Property not found", "target": {"type": "property", "id": property_id}})
    # Disallow delete if units exist
    if any(True for _ in prop_ref.collection("units").limit(1).stream()):
        raise HTTPException(status_code=409, detail={
            "code": "PROPERTY_DELETE_BLOCKED_HAS_UNITS",
            "message": "Cannot delete property with existing units. Delete units first, then try again.",
            "target": {"type": "property", "id": property_id},
            "suggested_action": "delete_units_first",
        })
    prop_ref.delete()
    return {"ok": True}


@router.post("/properties/{property_id}/units", response_model=UnitOut, dependencies=[Depends(require_auth)])
def create_unit(property_id: str, payload: UnitCreate) -> UnitOut:
    db = get_client()
    _ensure_property_operational(db, property_id)
    data = payload.dict()
    data["property_id"] = property_id
    # Uniqueness per property (case-insensitive)
    unit_key = payload.unit_number.lower()
    if any(True for _ in db.collection("properties").document(property_id).collection("units").where("unit_key", "==", unit_key).limit(1).stream()):
        raise HTTPException(status_code=409, detail={
            "code": "DUPLICATE_UNIT_NUMBER",
            "message": f"Unit number '{payload.unit_number}' already exists in this property.",
            "target": {"type": "unit", "property_id": property_id, "unit_number": payload.unit_number},
            "suggested_action": "use_unique_unit_number",
        })
    data["unit_key"] = unit_key
    data["created_at"] = firestore.SERVER_TIMESTAMP
    doc_ref = db.collection("properties").document(property_id).collection("units").document()
    doc_ref.set(data)
    snap = doc_ref.get()
    saved = snap.to_dict() or {}
    created_at = saved.get("created_at") or datetime.utcnow()
    return UnitOut(id=doc_ref.id, property_id=property_id, created_at=created_at, **payload.dict())


@router.get("/properties/{property_id}/units", response_model=List[UnitOut], dependencies=[Depends(require_auth)])
def list_units(property_id: str) -> List[UnitOut]:
    db = get_client()
    prop_ref = db.collection("properties").document(property_id)
    if not prop_ref.get().exists:
        raise HTTPException(status_code=404, detail="Property not found")
    results: List[UnitOut] = []
    for doc in prop_ref.collection("units").order_by("created_at", direction=firestore.Query.DESCENDING).stream():
        d = doc.to_dict() or {}
        results.append(
            UnitOut(
                id=doc.id,
                property_id=property_id,
                unit_number=d.get("unit_number"),
                status=_normalize_unit_status(d.get("status")),
                created_at=d.get("created_at", datetime.utcnow()),
            )
        )
    return results


@router.patch("/properties/{property_id}/units/{unit_id}", response_model=UnitOut, dependencies=[Depends(require_auth)])
def update_unit(property_id: str, unit_id: str, patch: UnitPatch) -> UnitOut:
    db = get_client()
    _ensure_property_operational(db, property_id)
    ref = db.collection("properties").document(property_id).collection("units").document(unit_id)
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail={"code": "UNIT_NOT_FOUND", "message": "Unit not found", "target": {"type": "unit", "id": unit_id, "property_id": property_id}})
    update = {k: v for k, v in patch.dict(exclude_unset=True).items()}
    if update:
        current = snap.to_dict() or {}
        forbidden_keys = set(update.keys()) - {"status"}
        if forbidden_keys:
            raise HTTPException(status_code=400, detail={"code": "UNIT_EDIT_NOT_ALLOWED", "message": "Units cannot be edited; only status can be changed."})
        if current.get("status") == "Non Operational" and update.get("status") is None:
            raise HTTPException(status_code=423, detail={"code": "UNIT_LOCKED_NON_OPERATIONAL", "message": "Unit is Non-Operational; only status change is allowed", "target": {"type": "unit", "id": unit_id}})
        ref.update(update)
        snap = ref.get()
    d = snap.to_dict() or {}
    return UnitOut(
        id=unit_id,
        property_id=property_id,
        unit_number=d.get("unit_number"),
        unit_type=d.get("unit_type"),
        status=_normalize_unit_status(d.get("status")),
        created_at=d.get("created_at", datetime.utcnow()),
    )


@router.delete("/properties/{property_id}/units/{unit_id}", dependencies=[Depends(require_auth)])
def delete_unit(property_id: str, unit_id: str):
    db = get_client()
    _ensure_property_operational(db, property_id)
    ref = db.collection("properties").document(property_id).collection("units").document(unit_id)
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail={"code": "UNIT_NOT_FOUND", "message": "Unit not found", "target": {"type": "unit", "id": unit_id, "property_id": property_id}})
    # Cascade delete legacy beds then remove unit
    beds_ref = ref.collection("beds")
    batch = db.batch()
    deleted_beds = 0
    for bed_doc in beds_ref.stream():
        batch.delete(beds_ref.document(bed_doc.id))
        deleted_beds += 1
    batch.commit()
    ref.delete()
    return {"ok": True, "deletedBeds": deleted_beds}


@router.post("/properties/{property_id}/photo", dependencies=[Depends(require_auth)])
async def upload_property_photo(property_id: str, file: UploadFile = File(...)):
    settings = get_settings()
    if not settings.public_assets_bucket:
        raise HTTPException(status_code=500, detail={"code": "MISSING_BUCKET", "message": "Public assets bucket is not configured"})
    db = get_client()
    content = await file.read()
    if len(content) > settings.thumb_max_bytes:
        raise HTTPException(status_code=400, detail={
            "code": "IMAGE_TOO_LARGE",
            "message": "Thumbnail must be under 2 MB.",
            "details": {"max_bytes": settings.thumb_max_bytes, "received_bytes": len(content)},
        })
    try:
        image = Image.open(io.BytesIO(content)).convert("RGB")
        image.thumbnail((settings.image_max_dim, settings.image_max_dim))
        out_io = io.BytesIO()
        image.save(out_io, format="WEBP")
        out_io.seek(0)
    except Exception as e:
        raise HTTPException(status_code=400, detail={"code": "IMAGE_PROCESSING_FAILED", "message": f"Failed to process image: {e}"})
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.public_assets_bucket)
    blob = bucket.blob(f"public/properties/{property_id}/thumb.webp")
    blob.cache_control = "public, max-age=31536000, immutable"
    blob.upload_from_file(out_io, content_type="image/webp")
    blob.make_public()
    photo_url = blob.public_url
    db.collection("properties").document(property_id).set({"photo_thumb_url": photo_url}, merge=True)
    return {"photo_thumb_url": photo_url}


@router.post(
    "/properties/{property_id}/units/{unit_id}/beds",
    response_model=BedOut,
    dependencies=[Depends(require_auth)],
)
def create_bed(property_id: str, unit_id: str, payload: BedCreate) -> BedOut:
    db = get_client()
    _ensure_property_operational(db, property_id)
    unit_ref = db.collection("properties").document(property_id).collection("units").document(unit_id)
    if not unit_ref.get().exists:
        raise HTTPException(status_code=404, detail="Unit not found")
    data = payload.dict()
    data["unit_id"] = unit_id
    data["created_at"] = firestore.SERVER_TIMESTAMP
    doc_ref = unit_ref.collection("beds").document()
    doc_ref.set(data)
    snap = doc_ref.get()
    saved = snap.to_dict() or {}
    created_at = saved.get("created_at") or datetime.utcnow()
    return BedOut(id=doc_ref.id, unit_id=unit_id, created_at=created_at, **payload.dict())


@router.get(
    "/properties/{property_id}/units/{unit_id}/beds",
    response_model=List[BedOut],
    dependencies=[Depends(require_auth)],
)
def list_beds(property_id: str, unit_id: str) -> List[BedOut]:
    db = get_client()
    unit_ref = db.collection("properties").document(property_id).collection("units").document(unit_id)
    if not unit_ref.get().exists:
        raise HTTPException(status_code=404, detail="Unit not found")
    results: List[BedOut] = []
    for doc in unit_ref.collection("beds").order_by("created_at", direction=firestore.Query.DESCENDING).stream():
        d = doc.to_dict() or {}
        results.append(
            BedOut(
                id=doc.id,
                unit_id=unit_id,
                bed_identifier=d.get("bed_identifier"),
                status=d.get("status"),
                tenant_id=d.get("tenant_id"),
                created_at=d.get("created_at", datetime.utcnow()),
            )
        )
    return results


@router.patch(
    "/properties/{property_id}/units/{unit_id}/beds/{bed_id}",
    response_model=BedOut,
    dependencies=[Depends(require_auth)],
)
def update_bed(property_id: str, unit_id: str, bed_id: str, patch: BedPatch) -> BedOut:
    db = get_client()
    _ensure_property_operational(db, property_id)
    ref = (
        db.collection("properties")
        .document(property_id)
        .collection("units")
        .document(unit_id)
        .collection("beds")
        .document(bed_id)
    )
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="Bed not found")
    update = {k: v for k, v in patch.dict(exclude_unset=True).items()}
    if update:
        ref.update(update)
        snap = ref.get()
    d = snap.to_dict() or {}
    return BedOut(
        id=bed_id,
        unit_id=unit_id,
        bed_identifier=d.get("bed_identifier"),
        status=d.get("status"),
        tenant_id=d.get("tenant_id"),
        created_at=d.get("created_at", datetime.utcnow()),
    )


@router.delete(
    "/properties/{property_id}/units/{unit_id}/beds/{bed_id}",
    dependencies=[Depends(require_auth)],
)
def delete_bed(property_id: str, unit_id: str, bed_id: str, soft: bool = Query(True)):
    db = get_client()
    _ensure_property_operational(db, property_id)
    ref = (
        db.collection("properties")
        .document(property_id)
        .collection("units")
        .document(unit_id)
        .collection("beds")
        .document(bed_id)
    )
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="Bed not found")
    if soft:
        ref.update({"status": "Archived"})
        return {"ok": True, "softDeleted": True}
    ref.delete()
    return {"ok": True}
