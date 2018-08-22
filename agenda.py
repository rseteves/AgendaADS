#Agenda Telefonica
import funcoes

funcoes.bemvindo()
#Opcoes do Usuario
opcao = int(input())
print("Selecionaste", opcao)


#Estrutura de controle
if opcao==1:
	funcoes.adicionar()
elif opcao==2:
        funcoes.listar()
elif opcao==3:
        funcoes.deletanum()
elif opcao==4:
        funcoes.Busca()
elif opcao==5:
        funcoes.Sair()
else:
	funcoes.falha()


