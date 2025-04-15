n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor:"))
while n2==0:

    n2 = int(input("Digite um número acima de 0:"))

div = n1 / n2
print (f"{n1} dividido por {n2} é {div:.0f}")