from fastapi import FastAPI

app = FastAPI()

#Ruta raiz
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# python -m uvicornmain main:app --reload