

numRom= {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
    }

klist= list(numRom.keys())

def romano_a_entero(rom):
    if rom== '':
        return 'Error de formato'

    entero=0
    numRepes=0
    letraAnt=''
    fueResta= False
    


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


def entero_a_romano(valor): 

    resultado= ''
    res = ''
    numRepes=0
    valRepes=0
    kAnt=''
    resRepes= ''

    while valor>0:
        k, v= busca_valor_menor_o_igual(valor)
        valor -= v
        kind= klist.index(k)
        ksup= kind-1
        kinf= kind+1


        if kAnt==k:
            
            numRepes +=1
            valRepes += numRom[klist[kind]]
            resRepes +=k
            if numRepes>2:
                
                if valRepes + numRom[klist[kind]] == numRom[klist[ksup]]- numRom[klist[kind]]:
                    resRepes= (klist[ksup])
                    resultado += resRepes
                #elif valRepes== 
                   # resRepes += (klist[ksup]+ klist[kinf])
            
        if kAnt== '' or kAnt != k:
             
            if klist.index(k) %2 != 0:
                if (valor+ v) ==numRom[klist[ksup]]-numRom[klist[kinf]]:
                    res += (klist[kinf]+ klist[ksup])
                    valor -= numRom[klist[ksup]]-numRom[klist[kinf]]
                else:
                    res +=k
            else:
                res += k
            #resultado += res
        kAnt=k
        resultado = (res +resRepes)   
    return resultado

    

def busca_valor_menor_o_igual(v):
    for key, value in numRom.items():
        if value <= v:
            return key, value


def descomponer(numero):
    