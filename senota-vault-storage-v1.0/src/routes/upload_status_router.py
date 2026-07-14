from fastapi import APIRouter
router=APIRouter(prefix='/upload',tags=['Upload'])
@router.get('/status')
def status():
    return {'status':'ready'}
