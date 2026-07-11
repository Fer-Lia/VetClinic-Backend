from fastapi import FastAPI

app = FastAPI(title="VetClinic API")


@app.get("/")
def read_root():
    return {"mensaje": "VetClinic API funcionando"}
