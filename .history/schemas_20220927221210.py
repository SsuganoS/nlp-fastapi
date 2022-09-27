from pydantic import BaseModel
from typing import List


class VectorMsg(BaseModel):
    vector: List[float]
