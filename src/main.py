from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from os import path, getcwd, getenv

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

# servir arquivos
caminho_atual = getcwd()
caminho_htdocs = path.join(caminho_atual, 'src', 'htdocs')
caminho_index = path=path.join(caminho_htdocs, "index.html")
@api.get("/")
def index():
    return FileResponse(path=caminho_index, media_type='text/html')
api.mount(path='/', app= StaticFiles(directory=caminho_htdocs), name='htdocs')



