ListaUF= list()
sigla=input("Dgita UF:").upper()[:2]
while sigla !='s':
    if sigla not in ListaUF:
        ListaUF.append(sigla)
        sigla= input("Digite o UF:").upper()[:2]
    
print(ListaUF)