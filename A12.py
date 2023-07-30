
num14=0
num15=0


for i in range (0,15):
    num1=int(input("digite um numero: "))
    if num1%2:   num14=num14+1 ; num15=num15+num1
media=num15/num14
print(f"o media aritmetica dos numeros pares e {media} ")
