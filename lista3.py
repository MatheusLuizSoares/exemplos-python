ListaUF= list()

while True:
 sigla= input("Digite a sigla UF:").upper()[:2]
 
 if sigla =="S": break

 nome= input("Digite o nome UF:").upper()

ListaUF.append([sigla,nome])




print(ListaUF)