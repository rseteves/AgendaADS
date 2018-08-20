#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(raw_input())
print("Seleccionaste", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 3:
	funcoes.Buscar()
elif opcao == 2:
	funcoes.DeletarContato()
elif opcao == 2:
	funcoes.sairDoPrograma()
else:
	funcoes.falha()


