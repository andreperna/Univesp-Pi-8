from fastapi import FastAPI

from src.routes.status import router as route_status
from src.routes.gets import router as route_querys
from src.routes.posts import router as route_posts
from src.routes.deletes import router as route_deletes

api = FastAPI(
    title='DengueAPI',
    description='API utilizada no Back-End do Projeto Integrador VIII, da universidade UNIVESP'
)

# importando rotas
api.include_router(router=route_status, prefix='/api/status')
api.include_router(router=route_querys, prefix='/api/casos')
api.include_router(router=route_posts, prefix='/api/inserir_ocorrencia')
api.include_router(router=route_deletes, prefix='/api/excluir_ocorrencia')


