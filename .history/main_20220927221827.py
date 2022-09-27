from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from gensim.models import KeyedVectors

from schemas import VectorStr

app = FastAPI()
origins = ['http://localhost:5000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{word}", response_model=VectorStr)
async def root(word):
    return {"vector": wv[word]}


if __name__ == '__main__':
    wv = KeyedVectors.load_word2vec_format("ja_vectors.kv")
    uvicorn.run(app)
