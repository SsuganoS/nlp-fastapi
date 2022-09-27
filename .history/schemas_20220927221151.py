from pydantic import BaseModel


class VectorMsg(BaseModel):
    vector: str
