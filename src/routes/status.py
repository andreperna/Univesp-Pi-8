from fastapi import APIRouter

router = APIRouter()

# retorna status da api
@router.get('/', tags=["API Status"])
def verifica_status():
    """Verifica se API está Online""" 
    return {'status':'ok'}