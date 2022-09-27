from pydantic import BaseModel


class VectorMsg(BaseModel):
    message: str
