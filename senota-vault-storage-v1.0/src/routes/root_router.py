from fastapi import APIRouter

router=APIRouter(tags=["Root"])

@router.get("/ping")
def ping():
    return {"message":"pong"}
