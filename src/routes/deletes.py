from fastapi import APIRouter

router = APIRouter()

@router.delete('/{id}', tags=["Excluir Ocorrência"])
def excluir_ocorrencia(id: int):
    return {'msg': f'Ocorrencia id:{id} excluida com sucesso'}