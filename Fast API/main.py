from fastapi import FastAPI

app = FastAPI()

@app.get("/user/")
async def root(name: str, age: int):
    return {"name": name, "age": age}
