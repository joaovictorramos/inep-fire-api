def connectionDatabase(dataConnection):
    #server = "DJ10W9D3\SQLEXPRESS"
    #database = "bd_sinape_alupar"
    #username = "sa"
    #password = "DAS@sinap"
    
    server   = dataConnection[0]
    database = dataConnection[1]
    username = dataConnection[2]
    password = dataConnection[3]
    
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};sslverify=0'
    return connection_string


def findByMaxId(id, cursor):
    try:
        cursor.execute('SELECT MAX(COD_QUEIM) FROM QUEIMADA')
        result_set = cursor.fetchall()
        
        if result_set and result_set[0][0] is not None:
            id = result_set[0][0] + 1
        else:
            id = 1
    except Exception as e:
        print(f'Error in connection: {e}')
    
    return id