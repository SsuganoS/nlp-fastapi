from pydantic import BaseModel


class VectorMsg(BaseModel):
    vector: numpy.ndarray
