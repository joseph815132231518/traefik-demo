from fastapi import FastAPI
from time import sleep

app = FastAPI()

@app.get("/api")
def read_root():
    sleep(5)
    return {"message": "Hello from FastAPI through Traefik!"}
