
function btnDatabase(action){
    var x   = document.getElementById("ifDatabase")
    var btn = document.getElementById("btnStartDatabase")

    console.log(x)
    if(x.style.display === "block"){
        x.style.display = "none"

    }else{
        x.style.display = "block"
        if(action === 'import_database'){
            btn.setAttribute("onclick", "handleButtonClick('import_database')")

        }else if(action === 'export_script'){
            btn.setAttribute("onclick", "handleButtonClick('export_script')")
        }
    }
}


function btnCsvOrJson(action){
    var x   = document.getElementById("ifCsvOrJson")
    var btn = document.getElementById("btnStartCsvOrJson")

    console.log(x)
    if(x.style.display === "block"){
        x.style.display = "none"

    }else{
        x.style.display = "block"
        if(action === 'export_csv'){
            btn.setAttribute("onclick", "handleButtonClick('export_csv')")

        }else if(action === 'export_json'){
            btn.setAttribute("onclick", "handleButtonClick('export_json')")
        }
    }
}