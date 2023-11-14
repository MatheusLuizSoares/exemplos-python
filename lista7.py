
lisatotal=list()
contador=0
somaN=0
while True:
 n=int(input("Digite 10 números:"))
 if n==0:break
 lisatotal.append(n)
 print(lisatotal)
 contador+=1
 somaN+=n
 print(lisatotal)


 lisatotal.sort()
 media=somaN/10

 print(f"A média é: {media}")
 print(f"maior número é: {max(lisatotal)}")
 print(f"menor número é: {min(lisatotal)}")