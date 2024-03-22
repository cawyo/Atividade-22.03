n = int(input("Digite a quantidade de números que serão informados: "))
cont = 0
x = 0
z = 0
while cont < n:
    numero = int(input("Digite um número: "))
    if numero > 10:
        cont += 1
        x = numero
        z += x
    else:
        print("Inválido")
print (f"A soma é : {z}")