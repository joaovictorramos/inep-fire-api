def createInsert(row, insert_queimada, insert_queimada_comp, dataConnection, cont):
    import ftfy
    import pyodbc
    from RecordState import stateToAcronym
    from DAO import connectionDatabase, findByMaxId
    
    id = 0
    try:
        connection = pyodbc.connect(connectionDatabase(dataConnection))
        cursor = connection.cursor()
        
        foreign_key = findByMaxId(id, cursor)
        foreign_key += cont
        
        latitude  = row['lat'].strip()
        longitude = row['lon'].strip()
        municipio = ftfy.fix_text(row['municipio'].replace("'","''"))
        
        estado = stateToAcronym(ftfy.fix_text(row['estado']))
            
        insert_queimada.append(f"INSERT INTO QUEIMADA (DataHora, Latitude, Longitude, Estado, Municipio, Satelite) VALUES ('{row['data_hora_gmt']}', '{latitude}', '{longitude}', '{estado}', '{municipio}', '{row['satelite']}');\n")
        insert_queimada_comp.append(f"INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES ('{foreign_key}', 'Bioma', '{row['bioma']}');\n")
        insert_queimada_comp.append(f"INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES ('{foreign_key}', 'Diasemchuva', '{row['numero_dias_sem_chuva']}');\n")
        insert_queimada_comp.append(f"INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES ('{foreign_key}', 'Precipitacao', '{row['precipitacao']}');\n")
        insert_queimada_comp.append(f"INSERT INTO QUEIMADA_COMPLEMENTO (COD_QUEIM, CAMPO, VALOR) VALUES ('{foreign_key}', 'Riscofogo', '{row['risco_fogo']}');\n")    
        
    except Exception as e:
        print(f'Error in connection: {e}')
        
    finally:
        if 'cursor' in locals():
            cursor.close()
            
        if 'connection' in locals():
            connection.close()
