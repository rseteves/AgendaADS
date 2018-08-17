#Agenda Telefonica
import funcoes

funcoes.bemvindo()

repeticao = True

#Estrutura de controle
#Opcoes do Usuario
while repeticao == True:
	print("""Selecione a Opção: 
			1 - Adicionar 	
			2 - Listar 
			3 - Buscar 
			4 - Sair""")
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


