from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory=".", html=True), name="static")

@app.get("/")
def root():
    return FileResponse("index.html")
