

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
        return 'Error de formato'

    entero=0
    numRepes=0
    letraAnt=''
    fueResta= False
    klist= list(numRom.keys())


    for letra in rom:
        
        if letra in numRom:
            
            if letraAnt == '' or numRom[letra]<= numRom[letraAnt]:
                entero += numRom[letra]
                fueResta= False
            else:
                if klist.index(letraAnt) %2 != 0:
                    return 'Error de formato'

                if klist.index(letraAnt)- klist.index(letra)>2:
                    return 'Error de formato'
                        
                else:
                    if numRepes==1 or fueResta== True:
                        return 'Error de formato'
                    else:
                        entero += numRom[letra]- numRom[letraAnt]*2
                        fueResta= True

        if letra not in numRom:
            return 'Error de formato'
        if letra==letraAnt and numRepes==2:
            return 'Error de formato'
        elif letra==letraAnt :
            numRepes +=1           
        else:
            numRepes=0
            


        letraAnt= letra
        

    return entero



