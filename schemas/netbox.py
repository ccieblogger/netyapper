from typing import Optional
from pydantic import BaseModel

class IntentRequest(BaseModel):
    prompt: str

class DeviceInfoRequest(BaseModel):
    device: str

class InterfaceIPRequest(BaseModel):
    device: str
    interface: str

class DeviceInfoResponse(BaseModel):
    device: str
    interfaces: list

class InterfaceIPResponse(BaseModel):
    device: str
    interface: str
    ip: Optional[str]
    error: Optional[str] = None
