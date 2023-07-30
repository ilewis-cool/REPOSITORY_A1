num14=0
num15=0
for i in range (0,15):
    num1=int(input("digite um numero: "))
    if num1>=0: num14=num14+num1
    if num1<=0: num15=num15+num1
   
soma=num14+num15
if soma==0: print("hehehehehe muito engracado")
else: print(f"o soma does numeros positivos e {num14} e o soma dos negativos e {num15} e o soma total e {soma}")