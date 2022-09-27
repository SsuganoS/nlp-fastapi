from pydantic import BaseModel


class VectorStr(BaseModel):
    vector: str
