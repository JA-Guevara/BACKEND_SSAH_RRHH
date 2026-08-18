from fastapi import FastAPI

app = FastAPI(title="SSAH RRHH API")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Backend SSAH RRHH"}
