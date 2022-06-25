# importando conector mysql
import mysql.connector

# importando configurações de conexão
from src.config.database_config import connection_config


connection_config = {
    'host': 'tidb.c458433.c72edad0.us-east-1.prod.aws.tidbcloud.com',
    'user': 'root',
    'password': 'P@ssw0rd!',
    'database': 'test',
    'port': '4000'
}

# ========================================================================
# opção de abrir conexão e executar consulta sql


def connect_and_execute(sql: str):
    try:
        with mysql.connector.connect(**connection_config) as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            return (result)
    except mysql.connector.Error as e:
        return {'erro': e}
# ========================================================================


# ========================================================================
# opção de criar conexão e aproveitar ela
# criando conexão e cursor globais
connection = mysql.connector.connect(**connection_config)
cursor = None
if connection.is_connected():
    cursor = connection.cursor(dictionary=True)

# criando função para executar consulta sql


def execute(sql: str):
    cursor.execute(sql)
    result = cursor.fetchall()
    return (result)
# ========================================================================
