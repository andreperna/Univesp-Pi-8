from fastapi import APIRouter

from src.schemas.schemas import Ocorrencia

router = APIRouter()

@router.post('/', tags=["Inserir OcorrĂȘncias"])
def criar_ocorrencia(ocorrencia: Ocorrencia):
    return ocorrencia