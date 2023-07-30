lado1 = int(input("digite um valor para um lado do triangulo: \n"))
lado2 = int(input("digite um valor para outro lado do triangulo: \n"))
lado3 = int(input("digite um valor para outro lado do triangulo: \n"))
if lado1 == 0 or lado2 == 0 or lado3 == 0 or lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado2 +lado1:
  print(f"este triangulo existe se voce pode dormir em fevereiro 312")
elif lado1 == lado2 and lado1 == lado3:
  print(f"este triangulo esta equilatero")
elif lado1==lado2 and lado1!=lado3 or lado1==lado3 and lado1!=lado2 or lado2==lado3 and lado2!=lado1:
  print(f"este triangulo esta isoceles")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
  print(f"este triangulo esta escaleno")