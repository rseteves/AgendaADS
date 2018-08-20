#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Selecione", opcao)

#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 3:
	funcoes.Busca()
elif opcao == 4:
	funcoes.DeletarContato()
elif opcao == 5:
	funcoes.sairDoPrograma()
else:
	funcoes.falha()
