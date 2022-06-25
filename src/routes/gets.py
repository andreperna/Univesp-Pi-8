from fastapi import APIRouter

import src.database.database_queries as q

router = APIRouter()

# retorna casos geral
@router.get('/', tags=["Consultas"],)
def casos_geral(filtro:str = 'Total'):
    """Retorna todos os Casos Registrados"""
    return q.retorna_casos_geral(filtro)

# retorna casos de um estado específico
@router.get('/{estado}', tags=["Consultas"])
def casos_estado(estado, filtro:str = 'Total'):
    return q.retorna_casos_estado(estado, filtro)

# retorna casos de uma cidade específica (resumo por bairro ou rua)
@router.get('/{estado}/{cidade}', tags=["Consultas"])
def casos_cidade(estado, cidade, filtro:str = 'Total', resume_by:str = 'bairro'):
    return q.retorna_casos_cidade(estado, cidade, filtro, resume_by)


