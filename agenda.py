#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Opção selecionada: ", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 4:
        print("Buscar por Nome: ")
        funcoes.buscarcontato()
elif opcao == 9:
	print("Fechando o programa...")
	funcoes.close()
else:
	print("Opção Invalida!")


