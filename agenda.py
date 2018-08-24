#Agenda Telefonica
import funcoes



repeticao = True

#Estrutura de controle
#Opcoes do Usuario
while repeticao == True:
	funcoes.bemvindo()
	opcao = int(input("Opção: "))
	if opcao == 1:
		funcoes.adicionar()
	elif opcao == 2:
		funcoes.listar()
	elif opcao == 3:
		funcoes.buscar()
	elif opcao == 4:
		repeticao = False
	else:
		funcoes.falha()
input("Pressione ENTER para Sair")


