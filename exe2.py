print("programa feito para calculo de médias.")

soma = 0

contador = 0

while contador < 10:
	nota = float(input(f"Digite a {contador + 1}° nota: \n"))
	if nota < 0 or nota > 10:
		print("ERROR: valores inválidos")
	else:
		soma += nota
		contador += 1
media = soma / contador

print(f"sua média é: {media}")