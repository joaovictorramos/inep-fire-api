function handleButtonClick(action){
    var stateValue    = document.getElementById('state').value
    var dateHeadValue = document.getElementById('date_head').value
    var dateTailValue = document.getElementById('date_tail').value
    var serverValue   = document.getElementById('server').value
    var databaseValue = document.getElementById('database').value
    var usernameValue = document.getElementById('username').value
    var passwordValue = document.getElementById('password').value
    var pathValue     = document.getElementById('path').value

    var msgFetchValue = document.getElementById('msg')
    
    msgFetchValue.style.display = `block`
    msgFetchValue.innerText = 'Carregando...'

    var xhr = new XMLHttpRequest()
    xhr.open('POST', '/' + action, true)
    xhr.setRequestHeader('Content-Type', 'application/json')

    /*
    if(dateHeadValue > dateTailValue){
        alert('A data informada não corresponde aos parâmetros indicados!')
        msgFetchValue.style.display = `none`

    }else{
        xhr.send(JSON.stringify({
            state: stateValue, 
            dateHead: dateHeadValue, 
            dateTail: dateTailValue, 
            server: serverValue, 
            database: databaseValue, 
            username: usernameValue, 
            password: passwordValue, 
            path: pathValue
        }))
    }
    */

    if(dateHeadValue > dateTailValue){
        alert('A data informada não corresponde aos parâmetros indicados.')

    }else{
        fetch('/' + action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                state: stateValue,
                dateHead: dateHeadValue,
                dateTail: dateTailValue,
                server: serverValue,
                database: databaseValue,
                username: usernameValue,
                password: passwordValue,
                path: pathValue
            }),
        })
        .then(response => {
            if(!response.ok){
                throw new Error(`Erro na solicitação: ${response}`)
            }
            return response.json()
        })
        .catch(error =>{
            msgFetchValue.innerText = 'Não foi possível realizar a conversão!'
            console.error(`Erro na solicitação: ${error}`)
        })
        .finally(() =>{
            //msgFetchValue.style.display = `none`
            msgFetchValue.innerText = 'Conversão concluída!'
        })
    }
}