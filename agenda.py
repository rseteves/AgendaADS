# Agenda Telefonica

import funcoes

funcoes.bemvindo()

opcao = int(input())
print("Seleccionaste", opcao)
print()  # pula linha



while opcao != 9:
	# Estrutura de controle
	if opcao == 1:
		funcoes.adicionar()
	elif opcao == 2:
		funcoes.listar()
	elif opcao == 4:
		funcoes.buscar()
	elif opcao == 9:
		agenda.close()
	else:
		funcoes.falha()


	funcoes.bemvindo()

	# Opcoes do Usuario
	opcao = int(input())
	print("Seleccionaste", opcao)
	print()  # pula linha
