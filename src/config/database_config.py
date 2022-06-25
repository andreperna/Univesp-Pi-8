import os
from dotenv import load_dotenv

# carrega arquivo .env
load_dotenv()

# configurações de conexão ao banco de dados
connection_config = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE'),
    'port': os.getenv('PORT_DB')
}
