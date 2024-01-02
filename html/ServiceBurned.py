def csvOrZip(KEY, monthHead, yearHead, monthTail, yearTail, state, dateHead, dateTail, path, dataConnection):
    import zipfile
    import requests
    from io import BytesIO
    from BurnedCsv import openCsv
    from BurnedZip import openZip
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    while int(yearHead) <= int(yearTail):
        while int(monthHead) <= int(monthTail):
            
            year  = str(yearHead)
            month = str(monthHead).zfill(2)
            
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            urlCsv = f'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/focos_mensal_br_{year}{month}.csv'
            response = requests.get(urlCsv, verify=False)
            
            try:
                if response.status_code == 404:
                    urlZip = f'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/focos_mensal_br_{year}{month}.zip'
                    
                    response = requests.get(urlZip, verify=False)
                    zip_file = zipfile.ZipFile(BytesIO(response.content))
                    
                    extractPath = 'C:\\QUEIMADAS\\PLANILHA'
                    
                    zip_file.extractall(extractPath)
                    zip_file.close()
                    
                    openZip(KEY, month, year, state, dateHead, dateTail, path, dataConnection)
                else:
                    
                    year  = str(yearHead)
                    month = str(monthHead).zfill(2)
                    
                    openCsv(KEY, month, year, urlCsv, state, dateHead, dateTail, path, dataConnection)
                    
            except Exception as e:
                print(f'Error in csv file: {e}')
            
            monthHead = int(monthHead)+1
        yearHead = int(yearHead)+1
    