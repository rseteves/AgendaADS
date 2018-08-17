#Agenda Telefonica
import funcoes

x = 0
while x != 9: 
	funcoes.bemvindo()

	#Opcoes do Usuario
	opcao = int(input())
	print("Seleccionaste", opcao)
	
	#Estrutura de controle
	if opcao == 1:
		funcoes.adicionar()
		x = 1
	elif opcao == 2:
		funcoes.listar()
		x = 2
	elif opcao == 3:
		funcoes.excluir()
		x = 3
	elif opcao == 4:
		funcoes.buscar_nome()
		x = 4
	elif opcao == 9:
		exit()
		x = 9
	else:
		funcoes.falha()


