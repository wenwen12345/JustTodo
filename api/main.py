from fastapi import FastAPI
import uvicorn as uv

app = FastAPI()


@app.get("/tasks")
def root(id: int):
    return {"message": "Hello World"}

uv.run(app, host="127.0.0.1", port=8000)