from pydantic import BaseModel, Field

class PhoneNumberRequest(BaseModel):
    phone_number: str = Field(..., regex="^\+[1-9]\d{1,10}$")