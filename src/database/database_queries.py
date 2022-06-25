import src.database.database_core as db

# ========================================================
def retorna_casos_geral(filtro:str = 'Total'):
    if filtro == 'Total':
        result = db.execute(
        'SELECT count(*) as qtd FROM view_ocorrencias')
    elif filtro == 'Resumo':
        result = db.execute(
        'SELECT estado, count(*) as qtd FROM view_ocorrencias GROUP BY estado ORDER BY estado')
    elif filtro == 'Idade':
        result = db.execute(
        'SELECT faixa_etaria, COUNT(*) as qtd FROM test.view_ocorrencias GROUP BY faixa_etaria ORDER BY faixa_etaria')
    return result


# ========================================================
def retorna_casos_estado(estado: str, filtro:str = 'Total'):
    if filtro == 'Total':
        result = db.execute(
        f'SELECT count(*) as qtd FROM view_ocorrencias WHERE estado = "{estado}"')
    elif filtro == 'Resumo':
        result = db.execute(
        f'SELECT cidade, count(*) as qtd FROM view_ocorrencias WHERE estado = "{estado}" GROUP BY cidade ORDER BY cidade')
    elif filtro == 'Idade':
        result = db.execute(
        f'SELECT faixa_etaria, COUNT(*) as qtd FROM test.view_ocorrencias WHERE estado = "{estado}" GROUP BY faixa_etaria ORDER BY faixa_etaria')    
    return result


# ========================================================
def retorna_casos_cidade(estado: str, cidade: str, filtro:str = 'Total', resume_by:str = 'bairro'):
    if filtro == 'Total':
        result = db.execute(
        f'SELECT count(*) as qtd FROM view_ocorrencias WHERE estado = "{estado}" AND cidade = "{cidade}"') 
    elif filtro == 'Resumo':
        result = db.execute(
            f'SELECT {resume_by}, count(*) as qtd FROM view_ocorrencias WHERE estado = "{estado}" AND cidade = "{cidade}" GROUP BY {resume_by} ORDER BY {resume_by}')
    elif filtro == 'Idade':
        result = db.execute(
        f'SELECT faixa_etaria, COUNT(*) as qtd FROM test.view_ocorrencias WHERE estado = "{estado}" AND cidade = "{cidade}" GROUP BY faixa_etaria ORDER BY faixa_etaria')  
        
    return result










