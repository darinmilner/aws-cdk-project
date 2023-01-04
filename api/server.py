import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from config import configure


settings = configure()
app = FastAPI()


class ResponseModel(BaseModel):
    message: str


def greet(name: str):
    return f"Hello {name}"

@app.get("hello/health", response_model=ResponseModel)
def health():
    return ResponseModel(message="Healthy!")


@app.get("hello/{name}", response_model=ResponseModel)
def hello(name: str) -> float:
    return ResponseModel(message=greet(name))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port, log_level=settings.log_level)
