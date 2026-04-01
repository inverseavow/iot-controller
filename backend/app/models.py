from pydantic import BaseModel

class DavinciDevice(BaseModel):
    id: int
    name: str
    location: str
    status: str

class Wallwasher(BaseModel):
    id: int
    model: str
    intensity: float

class User(BaseModel):
    id: int
    username: str
    email: str

class DeviceCommand(BaseModel):
    command: str
    device_id: int

class WallwasherCommand(BaseModel):
    command: str
    wallwasher_id: int

class Scenario(BaseModel):
    id: int
    name: str
    description: str
    devices: list[int]  # List of Device IDs