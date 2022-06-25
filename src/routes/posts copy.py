from fastapi import APIRouter

router = APIRouter()

@router.post('/', tags=["Inserir Ocorrências"])
def criar_ocorrencia(ocorrencia: Ocorrencia):
    return ocorrencia