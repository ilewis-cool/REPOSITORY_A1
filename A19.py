



from random import randrange
import random
num1=1
num2=0


value=int(input("digite um número ímpar maior que 1: "))
if value%2==0 or value<1:
    print("isso não é impar ou não é maior que 1")
else:
    lista=[randrange(0,50) for i in range(0,value)]
    lista.sort()
    print(f"o lista e {lista}")
    numero=int(value/2+0.5)
    number=lista[numero]
    for i in range(0,number):
        if i<number:
            num2=num2+1
            num1=num1*num2
    print(f"o fatorial do valor do centro da lista e {num1}")






