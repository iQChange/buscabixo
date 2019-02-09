import urllib.request
import time

print("BUSCA-BIXO: um script feito com <3 pelo bixo Lucas Henrique (fb.com/0.modernhermit)")
print("O script foi meio feito na correria, entao caso achem algum bug, e so me contatar.\n\n")
dados = urllib.request.urlopen("https://pastebin.com/raw/YQmaXzuY").read().decode('utf-8').split('\r\n')

while True:
	print("Escreva o filtro desejado para a busca, identicamente a lista em https://pastebin.com/raw/YQmaXzuY")
	filtro = input('> ').lower()
	corresp = []
	for l in dados:
		if filtro in l.lower():
			corresp.append(l)
		else:
			continue
	print('Busca concluida!\n')
	
	while True:
		print('\nDeseja imprimir os resultados na tela? (S/N)')
		resposta = input('> ')
		
		if resposta.lower() == 's':
			print('\nImprimindo resultados...\n\n')
			for c in corresp:
				print(c)
			print('\n')
			break
			
		if resposta.lower() == 'n':
			break
			
		else:
			print('\nEntrada fora do formato especificado. Por favor, entre novamente;')
			continue
	
	while True:
		print('\nDeseja gerar um arquivo TXT com os resultados?  (S/N)\nObs: O arquivo sera salvo no diretorio do script.')
		resposta = input('> ')
		if resposta.lower() == 's':
			with open('buscabixo' + time.strftime("%d_%m_%Y-%H-%M-%S.txt", time.gmtime()), 'w') as f:
				for c in corresp:
					f.write(c + '\r\n')
			break
					
		if resposta.lower() == 'n':
			break
			
		else:
			print('\nEntrada fora do formato especificado. Por favor, entre novamente;')
			continue
			
	print('\nSucesso! Deseja rodar o programa mais uma vez? (S/N)')
	resposta = input('> ')
	if resposta.lower() == 's':
		print('-'*50 + '\n\n\n')
		continue
	else:
		break
