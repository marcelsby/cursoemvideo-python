palavras = ('Bonito', 'Ouro', 'Casa', 'Pulso', 'Tato', 'utf')

for palavra in palavras:
	palavra_dividida = list(palavra.lower())
	vogais = ()
	
	for letra in palavra_dividida:
		if letra == 'a':
			vogais += letra,
		elif letra == 'e':
			vogais += letra,
		elif letra == 'i':
			vogais += letra,
		elif letra == 'o':
			vogais += letra,
		elif letra == 'u':
			vogais += letra,

	if len(vogais) == 0:
		print(f'A palavra \"{palavra}\" não tem vogais.')
	elif len(vogais) == 1:
		print(f'A palavra \"{palavra}\" tem a seguinte vogal: {vogais[0]}')
	else:
		print(f'A palavra \"{palavra}\" tem as seguintes vogais:', end=' ')
		for vogal in vogais:
			print(vogal, end=' ')

		print()
