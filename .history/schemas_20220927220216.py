from pydantic import BaseModel
from typing import Optional


class SuccessMsg(BaseModel):
    message: str
