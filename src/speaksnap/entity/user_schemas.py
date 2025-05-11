from pydantic import BaseModel, EmailStr
from typing import List, Optional

class TextInput(BaseModel):
    text: str
    userid: str
    sessionid: str

class SummaryResponse(BaseModel):
    userid: str
    sessionid: str
    response: dict
