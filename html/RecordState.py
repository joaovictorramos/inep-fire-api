def stateToAcronym(estado):
  match(estado):
      case 'ACRE':
        estado = 'AC'

      case 'ALAGOAS':
        estado = 'AL'

      case 'AMAPÁ':
        estado = 'AP'

      case 'AMAZONAS':
        estado = 'AM'

      case 'BAHIA':
        estado = 'BA'

      case 'CEARÁ':
        estado = 'CE'

      case 'ESPÍRITO SANTO':
        estado = 'ES'

      case 'GOIÁS':
        estado = 'GO'

      case 'MARANHÃO':
        estado = 'MA'

      case 'MATO GROSSO':
        estado = 'MT'

      case 'MATO GROSSO DO SUL':
        estado = 'MS'

      case 'MINAS GERAIS':
        estado = 'MG'

      case 'PARÁ':
        estado = 'PA'

      case 'PARAÍBA':
        estado = 'PB'

      case 'PARANÁ':
        estado = 'PR'

      case 'PERNAMBUCO':
        estado = 'PE'

      case 'PIAUÍ':
        estado = 'PI'

      case 'RIO DE JANEIRO':
        estado = 'RJ'

      case 'RIO GRANDE DO NORTE':
        estado = 'RN'

      case 'RIO GRANDE DO SUL':
        estado = 'RS'

      case 'RONDÔNIA':
        estado = 'RO'

      case 'RORAIMA':
        estado = 'RR'

      case 'SANTA CATARINA':
        estado = 'SC'

      case 'SÃO PAULO':
        estado = 'SP'

      case 'SERGIPE':
        estado = 'SE'

      case 'TOCANTINS':
        estado = 'TO'

      case 'DISTRITO FEDERAL':
        estado = 'DF'
  return estado