numero = int(input("digite um numero para verificar se e par:\n"))
resto = numero % 2
if resto == 0:
  print(f"este numero esta par")
elif resto != 0:
  print(f"este numero esta impar")