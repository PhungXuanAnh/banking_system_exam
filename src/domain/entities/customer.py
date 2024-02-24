from pydantic import BaseModel, ConfigDict


class Customer(BaseModel):
    id: int = None
    name: str
    email: str
    phone_number: str
    
    model_config = ConfigDict(from_attributes=True)
