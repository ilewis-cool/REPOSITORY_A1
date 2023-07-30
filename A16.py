num14=0
num15=0
num16=0
for i in range (0,20):
    num1=int(input("digite teu salario:"))
    if num1>=2000: num14=num14+1;num15=num15+num1
    else: num16=num16+(num1*1.075)
print(f"tem {num14} funcionarios com salario de mais que R$
2000 que a empresa gasta R${num15}")
print(f"mas se a empresa da aumento de 7.5% aos funcionarios com salario menos que R$2000 ia custar R${num16}")
