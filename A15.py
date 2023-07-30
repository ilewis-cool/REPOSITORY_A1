

num14=0
num15=0
for i in range (0,15):
    num1=int(input("digite teu idade: "))
    num2=int(input("digite teu altura em centimetros: "))
    if num1>=50: num14=num14+num2;num15=num15+1
    if num1<=0: print("nao funciona assim")




   
media=num14/num15
print(f"o media dos alturas de pessoas maiores que 50 e {media} centimetros")


