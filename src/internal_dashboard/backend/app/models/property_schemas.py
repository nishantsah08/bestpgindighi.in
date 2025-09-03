from datetime import datetime
from typing import Literal, Optional, List

from pydantic import BaseModel, Field, validator


PropertyStatus = Literal["Operational", "Non Operational"]
UnitStatus = Literal["Operational", "Non Operational"]
BedStatus = Literal["Occupied", "Vacant", "Reserved", "Archived"]


class Address(BaseModel):
    line1: str = Field(min_length=5, max_length=120)
    locality: Optional[str] = Field(default=None, max_length=80)
    city: str = Field(min_length=2, max_length=60)
    state: str = Field(min_length=2, max_length=60)
    pincode: str = Field(min_length=6, max_length=6)

    @validator("pincode")
    def pin_must_be_6_digits(cls, v: str) -> str:
        if not v.isdigit() or len(v) != 6:
            raise ValueError("Enter a valid 6-digit PIN code")
        return v


class PropertyCreate(BaseModel):
    property_name: str = Field(min_length=3, max_length=80)
    address: Address
    status: PropertyStatus = "Operational"
    unit_types: Optional[List[str]] = None

    @validator("property_name")
    def name_trim_and_validate(cls, v: str) -> str:
        name = " ".join(v.split())
        if len(name) < 3:
            raise ValueError("Property name must be at least 3 characters")
        return name


class PropertyPatch(BaseModel):
    property_name: Optional[str] = Field(default=None, max_length=80)
    address: Optional[Address] = None
    status: Optional[PropertyStatus] = None


class PropertyOut(PropertyCreate):
    id: str
    created_at: datetime


class UnitCreate(BaseModel):
    unit_number: str = Field(min_length=1, max_length=12)
    status: UnitStatus = "Operational"

    @validator("unit_number")
    def validate_unit_number(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Unit number cannot contain spaces")
        # allow alphanumeric and hyphen only
        import re
        if not re.fullmatch(r"[A-Za-z0-9-]{1,12}", v):
            raise ValueError("Unit number must be alphanumeric/hyphen, max 12 chars")
        return v


class UnitPatch(BaseModel):
    # Only status can be changed
    status: Optional[UnitStatus] = None


class UnitOut(UnitCreate):
    id: str
    property_id: str
    created_at: datetime


class BedCreate(BaseModel):
    bed_identifier: str = Field(min_length=1, max_length=50)
    status: BedStatus = "Vacant"
    tenant_id: Optional[str] = None


class BedPatch(BaseModel):
    bed_identifier: Optional[str] = Field(default=None, max_length=50)
    status: Optional[BedStatus] = None
    tenant_id: Optional[str] = None


class BedOut(BedCreate):
    id: str
    unit_id: str
    created_at: datetime
