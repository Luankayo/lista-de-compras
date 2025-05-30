from .conexao import conectar

def buscar_alunos_bloqueados(data_ini, data_fim):
    con = conectar()
    cur = con.cursor()
    query = """
        SELECT NOME, STATUS, TELEFONE2, DATA_NASCIMENTO
        FROM ALUNOS
        WHERE STATUS = 'BLOQUEADO'
        AND DATA_NASCIMENTO BETWEEN ? AND ?
    """
    cur.execute(query, (data_ini, data_fim))
    resultados = cur.fetchall()
    con.close()
    return resultados
