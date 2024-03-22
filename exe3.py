contpares = 0
somaimpares= 0
somapares = 0
inicio = 0
somatotal = 0
while contpares < 5 and somaimpares < 30: 
    inicio = int(input("Digite um número inteiro: "))
    verif = inicio%2
    if verif == 0:
        print("O número é par.")
        contpares += 1
        somapares += inicio
    if verif == 1:
        somaimpares += inicio
        print("O número é ímpar.")
    somatotal = somapares + somaimpares
print (f"A soma dos ímpares é: {somaimpares}")
print (f"A soma dos pares é: {somapares}")
print (f"A soma total é: {somatotal}")
