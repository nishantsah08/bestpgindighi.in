from datetime import datetime
from typing import Any, Optional
import uuid

from google.cloud import firestore  # type: ignore


def write_audit(
    db: firestore.Client,
    *,
    action: str,
    target_type: str,
    target_id: str,
    parent_property_id: Optional[str] = None,
    actor_id: Optional[str] = None,
    before: Optional[dict[str, Any]] = None,
    after: Optional[dict[str, Any]] = None,
    ip: Optional[str] = None,
    user_agent: Optional[str] = None,
) -> str:
    doc = {
        "action": action,
        "target_type": target_type,
        "target_id": target_id,
        "parent_property_id": parent_property_id,
        "actor_id": actor_id or "api",
        "before": before,
        "after": after,
        "timestamp": datetime.utcnow().isoformat(),
        "ip": ip,
        "user_agent": user_agent,
        "correlation_id": uuid.uuid4().hex,
    }
    ref = db.collection("audit_logs").document()
    ref.set(doc)
    return doc["correlation_id"]

