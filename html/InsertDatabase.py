def insertTable(row, dataConnection):
    import ftfy
    import pyodbc
    from RecordState import stateToAcronym
    from DAO import findByMaxId, connectionDatabase
    
    id = 0
    try:
        connection = pyodbc.connect(connectionDatabase(dataConnection))
        cursor = connection.cursor()
    
        id = findByMaxId(id, cursor)
    
        latitude  = row['lat'].strip()
        longitude = row['lon'].strip()
        municipio = ftfy.fix_text(row['municipio'].replace("'","''"))
        estado    = stateToAcronym(ftfy.fix_text(row['estado']))
        satelite  = ftfy.fix_text(row['satelite'])
        
        bioma        = ftfy.fix_text(row['bioma'])
        chuva        = ftfy.fix_text(row['numero_dias_sem_chuva'])
        precipitacao = ftfy.fix_text(row['precipitacao'])
        fogo         = ftfy.fix_text(row['risco_fogo'])
        
        
        sql_insert_queimada = "INSERT INTO QUEIMADA (DataHora, Latitude, Longitude, Estado, Municipio, Satelite) VALUES (?, ?, ?, ?, ?, ?);"
        values_queimada = (row['data_hora_gmt'], latitude, longitude, estado, municipio, satelite)
        
        sql_insert_queimada_complemento_bioma = "INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES (?, ?, ?)"
        values_complemento_bioma = (id, 'Bioma', bioma)
        
        sql_insert_queimada_complemento_chuva = "INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES (?, ?, ?)"
        values_complemento_chuva = (id, 'Diasemchuva', chuva)
        
        sql_insert_queimada_complemento_precipitacao = "INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES (?, ?, ?)"
        values_complemento_precipitacao = (id, 'Precipitacao', precipitacao)
        
        sql_insert_queimada_complemento_fogo = "INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES (?, ?, ?)"
        values_complemento_fogo = (id, 'Riscofogo', fogo)
        
        cursor.execute(sql_insert_queimada, values_queimada)
        cursor.execute(sql_insert_queimada_complemento_bioma, values_complemento_bioma)
        cursor.execute(sql_insert_queimada_complemento_chuva, values_complemento_chuva)
        cursor.execute(sql_insert_queimada_complemento_precipitacao, values_complemento_precipitacao)
        cursor.execute(sql_insert_queimada_complemento_fogo, values_complemento_fogo)
    
        connection.commit()
             
    except Exception as e:
        print(f'Error in connection: {e}')
        
    finally:
        if 'cursor' in locals():
            cursor.close()
            
        if 'connection' in locals():
            connection.close()
    return id