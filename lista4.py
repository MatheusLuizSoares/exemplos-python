n= int(input("informe um valor :"))

if n>0:
    listpares=list()
    for i in range(1,n*2+1):
        if i%2==0:
         listpares.append(i)
         print(listpares)
else:
        print("valor iformado invalido")