num1 = int(input("digite um numero:\n"))
num2 = int(input("digite outro numero:\n"))
if num1 < num2:
  print(f"o menor numero e {num1}")
elif num2 < num1:
  print(f"o menor numero e {num2}")
elif num2 == num1:
  print(f"voce digitou dois numeros iguais cara!!!!")