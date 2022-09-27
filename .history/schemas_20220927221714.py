from pydantic import BaseModel
from typing import List
import numpy


class VectorMsg(BaseModel):
    vector: numpy.ndarray
