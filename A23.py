num1=int(input("digite um numero: "))
num2=int(input("digite outro numero: "))
num3=int(input("digite outro numero: "))


def maior():
    if num1>num2 and num1>num3:
        print(f"o maior numero e {num1}")
    if num2>num1 and num2>num3:
        print(f"o maior numero e {num2}")
    if num3>num1 and num3>num2:
        print(f"o maior numero e {num3}")


def menor():
    if num1<num2 and num1<num3:
        print(f"o menor numero e {num1}")
    if num2<num1 and num2<num3:
        print(f"o menor numero e {num2}")
    if num3<num1 and num3<num2:
        print(f"o menor numero e {num3}")


maior()
menor()
