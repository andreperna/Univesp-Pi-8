from datetime import date
from pydantic import BaseModel

class Ocorrencia(BaseModel):
    cpf: str
    cep: str
    numero: int
    data_nascimento: date
    data_ocorrencia: date

