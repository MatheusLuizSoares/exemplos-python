
lisatotal=list()
contador=0
somaN=0
while contador<10:
 n=int(input("Digite 10 números:"))
 lisatotal.append(n)
 print(lisatotal)
 contador+=1
 somaN+=n
print(lisatotal)


media=somaN/10

print(f"A média é: {media}")
print(f"maior número é: {max(lisatotal)}")
print(f"menor número é: {min(lisatotal)}")