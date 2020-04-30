

numRom= {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
    }

def romano_a_entero(rom):
    if rom== '':
        return 'Carácter erróneo'

    entero=0
    numRepes=0
    letraAnt=''
    
    for letra in rom:
        if letra==letraAnt and numRepes==2:
            return 'Carácter erróneo'
        elif letra==letraAnt :
            numRepes +=1           
        else:
            pass

        letraAnt= letra
        
        if letra in numRom:
            entero += numRom[letra]
        else:
            return 'Carácter erróneo'

    return entero



