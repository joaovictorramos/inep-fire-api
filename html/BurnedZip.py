def openZip(KEY, month, year, state, dateHead, dateTail, path, dataConnection):
    import os
    import re
    import csv
    import json
    import ftfy
    import codecs
    import numpy as np
    from datetime import datetime
    from CreateInsert import createInsert
    from InsertDatabase import insertTable
    from RecordState import stateToAcronym
    
    dados_csv_np         = np.array([])
    insert_queimada      = []
    insert_queimada_comp = []
    insert_for_csv       = []
    
    arquivo_csv = ""
    arquivo_json = ""
    arquivo_text = ""
    arquivo_text_comp = ""
    
    pathCsv  = f'{path}\\csv'
    pathJson = f'{path}\\json'
    
    if not os.path.exists(pathCsv) and not os.path.exists(pathJson):
        os.makedirs(f'{path}\\csv')
        os.makedirs(f'{path}\\json')
        
    arquivo_csv  = os.path.join(pathCsv, f'queimadas_{year}{month}.csv')
    arquivo_json = os.path.join(pathJson, f'queimadas_{year}{month}.json')
        
    # Não está sendo usado (Insert desativado)
    arquivo_text = 'insert.txt'
    arquivo_text_comp = 'insert_comp.txt'

    cont = 0
    mainCsvInep = os.path.join('C:\\', 'QUEIMADAS', 'PLANILHA' ,f'focos_mensal_br_{year}{month}.csv')
        
    try:
        
        with open(mainCsvInep, 'r', newline='', encoding='utf-8') as dados_csv:
            csv_reader = csv.DictReader(dados_csv)
            for row in csv_reader:
                data_hora_csv_str = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', row['data_hora_gmt'])
                data_hora_csv = datetime.strptime(data_hora_csv_str[0], "%Y-%m-%d %H:%M:%S")
                state_csv = stateToAcronym(ftfy.fix_text(row['estado']))
                if(state == 'Todos'):
                    state_csv = 'Todos'
                    
                if(dateHead <= data_hora_csv <= dateTail):
                    
                    print(dateHead)
                    print(data_hora_csv)
                    print(dateTail)
                    print()
                    
                    if(state == state_csv):
                        if (KEY == 'Import database'):
                            insertTable(row, dataConnection)  # database
                                
                        elif (KEY == 'Export json'):
                            dados_csv_np = np.append(dados_csv_np, row) # json
                                
                        elif (KEY == 'Export csv'):
                            insert_for_csv.append(row) # csv
                                
                        elif (KEY == 'Export script'):
                            createInsert(row, insert_queimada, insert_queimada_comp, dataConnection, cont) # script
                        cont+=1

                if (data_hora_csv > dateTail):
                    break
    
           
        if (KEY == 'Export json'):
            novo_dados = dados_csv_np[:].tolist()
            novo_dados_csv = json.dumps(novo_dados, ensure_ascii=False, indent=4)
            novo_dados_json = ftfy.fix_text(novo_dados_csv)
            
            cont = 1
            while True:
                if os.path.exists(arquivo_json):
                    arquivo_json = os.path.join(pathJson, f'queimadas_{year}{month}({cont}).json')
                    cont+=1
                else:
                    break
            
            with codecs.open(arquivo_json, 'w', encoding='utf-8') as arquivo:
                arquivo.write(novo_dados_json)
                
            print(f'Conversão concluída. Os dados JSON foram salvos em {arquivo_json}')
        
        if (KEY == 'Export csv'):
            
            cont = 1
            while True:
                if os.path.exists(arquivo_csv):
                    arquivo_csv = os.path.join(pathCsv, f'queimadas_{year}{month}({cont}).csv')
                    cont+=1
                else:
                    break
            
            with codecs.open(arquivo_csv, 'w', encoding='utf-8') as arquivo:
                header = insert_for_csv[0].keys()
                writer = csv.DictWriter(arquivo, fieldnames=header)        
                writer.writeheader() 
                for linha in insert_for_csv:
                    writer.writerow(linha)
                    
            with codecs.open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
                read_file = arquivo.read()
                
            read_file_edit = ftfy.fix_text(read_file)
            with open(arquivo_csv, 'w', encoding='utf-8') as arquivo:
                arquivo.write(read_file_edit)
                
            print(f'Conversão concluída. Os dados CSV foram salvos em {arquivo_csv}')
                
        if(KEY == 'Export script'):
            with codecs.open(arquivo_text, 'w', encoding='utf-8') as arquivo:
                for linha in insert_queimada:
                    arquivo.write(f"{ftfy.fix_text(linha)}")
                
            with codecs.open(arquivo_text_comp, 'w', encoding='utf-8') as arquivo:
                for linha in insert_queimada_comp:
                    arquivo.write(f"{ftfy.fix_text(linha)}")
                    
            print(f'Conversão concluída. Os dados TXT foram salvos em {arquivo_text}')
            print(f'Conversão concluída. Os dados TXT foram salvos em {arquivo_text_comp}')
    
    except Exception as e:
        print(f'Diretório não encontrado: {e}')

    finally:
        os.remove(mainCsvInep)