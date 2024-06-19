from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/suma/{uno}/{dos}")
async def sumar(uno: int, dos: int):
    suma = uno + dos
    return {"La suma es: ": suma}
