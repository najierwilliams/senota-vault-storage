from fastapi import FastAPI
from src.routes.main_router import router

app=FastAPI(title="SENOTA Vault Storage")
app.include_router(router)

@app.get("/")
def root():
    return {"service":"SENOTA Vault Storage","status":"running"}
