num14=0
num15=0
num16=0
num17=0
num18=0
for i in range (0,15):
    num1=int(input("digite um idade: "))
    if 0<num1<=15: num14=num14+1
    if 16<=num1<=30: num15=num15+1
    if 31<=num1<=45: num16=num16+1
    if 46<=num1<=60: num17=num17+1
    if 61<=num1: num18=num18+1
print(f"o numero de idades entre 0 e 15 e {num14}")
print(f"o numero de idades entre 16 e 30 e {num15}")
print(f"o numero de idades entre 31 e 45 e {num16}")
print(f"o numero de idades entre 46 e 60 e {num17}")
print(f"o numero de idades maiores que 60 e {num18}")
