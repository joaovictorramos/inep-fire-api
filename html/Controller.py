import re
from ServiceBurned import csvOrZip
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/import_database", methods=["POST"])
def import_database():
    data = request.get_json()
        
    # regex de data
    dateHeadMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateHead'])
    dateTailMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateTail'])
    
    dateHeadNotFormmatter = datetime.strptime(dateHeadMatcher[0], "%Y-%m-%dT%H:%M")
    dateTailNotFormmatter = datetime.strptime(dateTailMatcher[0], "%Y-%m-%dT%H:%M")
    
    dateHead = dateHeadNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    dateTail = dateTailNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    
    yearHead  = dateHeadNotFormmatter.year
    monthHead = str(dateHeadNotFormmatter.month).zfill(2)
    
    yearTail  = dateTailNotFormmatter.year
    monthTail = str(dateTailNotFormmatter.month).zfill(2)
    
    state = data['state']
    
    someConverterDateHead = datetime.strptime(dateHead, "%Y-%m-%d %H:%M:%S")
    someConverterDateTail = datetime.strptime(dateTail, "%Y-%m-%d %H:%M:%S")
    
    server   = data['server']
    database = data['database']
    username = data['username']
    password = data['password']
    
    dataConnection = [server, database, username, password]
    KEY = 'Import database'
    csvOrZip(KEY, monthHead, yearHead, monthTail, yearTail, state, someConverterDateHead, someConverterDateTail, "", dataConnection)
    return jsonify(result=data)
    
    
@app.route("/export_json", methods=["POST"])
def export_json():
    data = request.get_json()
    
    dateHeadMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateHead'])
    dateTailMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateTail'])
    
    dateHeadNotFormmatter = datetime.strptime(dateHeadMatcher[0], "%Y-%m-%dT%H:%M")
    dateTailNotFormmatter = datetime.strptime(dateTailMatcher[0], "%Y-%m-%dT%H:%M")
    
    dateHead = dateHeadNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    dateTail = dateTailNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    
    yearHead  = dateHeadNotFormmatter.year
    monthHead = str(dateHeadNotFormmatter.month).zfill(2)
    
    yearTail  = dateTailNotFormmatter.year
    monthTail = str(dateTailNotFormmatter.month).zfill(2)
    
    state = data['state']
    path  = data['path']
    
    someConverterDateHead = datetime.strptime(dateHead, "%Y-%m-%d %H:%M:%S")
    someConverterDateTail = datetime.strptime(dateTail, "%Y-%m-%d %H:%M:%S")
    
    dataConnection = None
    
    KEY = 'Export json'
    csvOrZip(KEY, monthHead, yearHead, monthTail, yearTail, state, someConverterDateHead, someConverterDateTail, path, dataConnection)
    return jsonify(result=data)
    
    
@app.route("/export_csv", methods=["POST"])
def export_csv():
    data = request.get_json()
    
    dateHeadMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateHead'])
    dateTailMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateTail'])
    
    dateHeadNotFormmatter = datetime.strptime(dateHeadMatcher[0], "%Y-%m-%dT%H:%M")
    dateTailNotFormmatter = datetime.strptime(dateTailMatcher[0], "%Y-%m-%dT%H:%M")
    
    dateHead = dateHeadNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    dateTail = dateTailNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    
    yearHead  = dateHeadNotFormmatter.year
    monthHead = str(dateHeadNotFormmatter.month).zfill(2)
    
    yearTail  = dateTailNotFormmatter.year
    monthTail = str(dateTailNotFormmatter.month).zfill(2)
    
    state = data['state']
    path  = data['path']
    
    someConverterDateHead = datetime.strptime(dateHead, "%Y-%m-%d %H:%M:%S")
    someConverterDateTail = datetime.strptime(dateTail, "%Y-%m-%d %H:%M:%S")
    
    server   = data['server']
    database = data['database']
    username = data['username']
    password = data['password']
        
    dataConnection = [server, database, username, password]
    KEY = 'Export csv'
    csvOrZip(KEY, monthHead, yearHead, monthTail, yearTail, state, someConverterDateHead, someConverterDateTail, path, dataConnection)
    return jsonify(result=data)
    
    
'''
    SCRIPT (Disabled)

@app.route("/export_script", methods=["POST"])
def export_script():
    data = request.get_json()
    
    dateHeadMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateHead'])
    dateTailMatcher = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}', data['dateTail'])
    
    dateHeadNotFormmatter = datetime.strptime(dateHeadMatcher[0], "%Y-%m-%dT%H:%M")
    dateTailNotFormmatter = datetime.strptime(dateTailMatcher[0], "%Y-%m-%dT%H:%M")
    
    dateHead = dateHeadNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    dateTail = dateTailNotFormmatter.strftime("%Y-%m-%d %H:%M:%S")
    
    year  = dateHeadNotFormmatter.year
    month = str(dateHeadNotFormmatter.month).zfill(2)
    state = data['state']
    
    someConverterDateHead = datetime.strptime(dateHead, "%Y-%m-%d %H:%M:%S")
    someConverterDateTail = datetime.strptime(dateTail, "%Y-%m-%d %H:%M:%S")
    
    server   = data['server']
    database = data['database']
    username = data['username']
    password = data['password']
    
    dataConnection = [server, database, username, password]
    
    KEY = 'Export script'
    csvOrZip(KEY, month, year, state, someConverterDateHead, someConverterDateTail, dataConnection)
    return jsonify(result=data)
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)