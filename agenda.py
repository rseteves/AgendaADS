# Agenda Telefonica

import funcoes

funcoes.bemvindo()

# Opcoes do Usuario
opcao = int(input())
print("Seleccionaste", opcao)


while opcao != 9:
	# Estrutura de controle
	if opcao == 9:
		agenda.close()

	if opcao == 1:
		funcoes.adicionar()
	elif opcao == 2:
		funcoes.listar()
	else:
		funcoes.falha()

	funcoes.bemvindo()

	# Opcoes do Usuario
	opcao = int(input())
	print("Seleccionaste", opcao)
