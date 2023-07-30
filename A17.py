num1=int(input("digite o primeiro termo de um progressao aritimetica: "))
num3=int(input("digite o razao desse progressao aritimetica: "))
num2=int(input("digite o numero de termos desse progressao aritimetica: "))
soma=0


lista=[num1+num3*(i-1) for i in range(1,num2)]


for i in range(1,num2):
    soma=soma+lista[i-1]

print(f"o soma dos termos dessa progressão aritmética e {soma} ")
print(f"os termos também são:{lista}")




