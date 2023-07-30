import random
lista=[input("qual é teu nome: ") for i in range(0,20)]


random.shuffle(lista)


ganhador=random.choice(lista)
print(f"o ganhador e {ganhador}")
