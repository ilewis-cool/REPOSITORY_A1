



def select():
    choice=int(input("digite um numero par se quer o conversao para celcius e impar para conversao farenheight: "))
    if choice%2==0:
        celcius()
    if choice%2!=0:
        farenheight()


def celcius():
    celc=(num-32)*(5/9)
    print(f"o temperatura convertido e {celc}")


def farenheight():
    farn=num*(9/5)+32
    print(f"o temperatura convertido ao farenheight e {farn}")


print("eu sou convertron. eu converto temperaturas")
num=int(input("digite um temperatura em celcius ou farenheight para converter ao outro:"))
select()
