def taxa():
    taxaimposto=int(input("digite o porcentagem do taxa do imposto: "))
    taxaimposto=1+taxaimposto/100
    custo=int(input("digite o custo desse item: "))
    custo=custo*taxaimposto
    print(f"o custo desse item depois do taxa do imposto e {custo}")


print("eu sou o taxomatico. cálculo o custo de coisas depois do taxa de imposto")
taxa()


