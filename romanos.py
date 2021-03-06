

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

    for i in rom:
        if i not in numRom:
            return 'Error de formato'
        if klist.index(i) < klist.index(i)-1:
                if klist.index(i)+1 <= klist.index(i)-1:
                    return 'Error de formato'
                #else: 
                    #pass
        #else:
            #pass
        
            
    
    
    entero=0
    numRepes=0
    letraAnt=''
    letra2Ant= ''
    fueResta= False

    for letra in rom:
            
        if letra in numRom:
                
            if fueResta == True and numRom[letra]>= numRom[letra2Ant]:
                return 'Error de formato'
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
                

        letra2Ant= letraAnt
        letraAnt= letra
            

    return entero


def entero_a_romano(valor): 

    componentes= descomponer(valor)

    resultado= ''

    for valor in componentes:
        numRepes=0
        valRepes=0
        kAnt=''
        res = ''
        while valor>0:
            k, v= busca_valor_menor_o_igual(valor)
            valor -= v
            kind= klist.index(k)
            #ksup= kind-1
            #kinf= kind+1

            if kAnt==k:
                    
                numRepes +=1
                valRepes += numRom[klist[kind]]
                res +=k
                if numRepes>2:   
                    if valRepes + numRom[klist[kind]] == numRom[klist[kind-1]]- numRom[klist[kind]]:
                        res= (klist[kind]+ klist[kind-1])
                    
            if kAnt== '' or kAnt != k:
                    
                if klist.index(k) %2 != 0:
                    if (valor+ v) ==numRom[klist[kind-1]]- numRom[klist[kind+1]]:
                        res = (klist[kind+1]+ klist[kind-1])
                        valor -= numRom[klist[kind-1]]- numRom[klist[kind+1]]
                    else:
                        res +=k
                else:
                    res += k
                
            kAnt=k  
        resultado +=res 
    return resultado

        

def busca_valor_menor_o_igual(v):
    for key, value in numRom.items():
        if value <= v:
            return key, value


def descomponer(numero):
    res =[]
    for orden in range (3,0,-1): #desde 3 a 0, restanto de 1 en 1
        resto= numero % 10**orden
        res.append(numero- resto)
        numero= resto
    res.append(numero)
    return res
