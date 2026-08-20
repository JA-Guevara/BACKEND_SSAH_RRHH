from fastapi import FastAPI
from src.auth.infrastructure.http.router import router as auth_router
from src.bitacora.infrastructure.http.router import router as bitacora_router
from src.roles.infrastructure.http.router import router as roles_router

app = FastAPI(title="SSAH RRHH API")
app.include_router(auth_router)
app.include_router(bitacora_router)
app.include_router(roles_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Backend SSAH RRHH"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
