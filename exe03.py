par_cont = 0
par_sum = 0
impar_sum = 0

lista_par = []
lista_impar = []

while par_cont < 5 and impar_sum <= 30:
  
	numero = int(input("digite o número:"))
	if numero < 0:
		print("não admitido números negativos, faça novamente")
	elif numero%2 == 0:
		par_sum += numero
		lista_par.append(numero)
		par_cont += 1
		print(f"{numero} é par")
	else:
		lista_impar.append(numero)
		impar_sum += numero
		print(f"{numero} é impar")

print(f"\nResultado: \n\nOs números pares digitados foram: \n{lista_par} \nOs números impares foram: \n{lista_impar} \nA soma dos números impares é: \n{impar_sum} \nA soma dos números pares é:{par_sum}")