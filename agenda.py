#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Opção selecionada", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 9: 
	print('Fechando a agenda')
	funcoes.close()
elif opcao == 4:
	print('Buscar por nome')
	funcoes.buscarcontato()
elif opcao == 5:
	print('Remover contato')
	funcoes.removerContato()
else:
	print("Opção invalida")


