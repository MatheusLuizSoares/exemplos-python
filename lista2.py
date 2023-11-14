ListaUF= list()
while True:
 sigla= input("Digite o UF:").upper()[:2]
 
 if sigla =="S": break
 if sigla not in ListaUF:  
     ListaUF.append(sigla)
       
print(ListaUF)