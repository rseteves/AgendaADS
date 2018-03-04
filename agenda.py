#Agenda Telefonica
import funcoes

while opcao!=9:
funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Seleccionaste", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 4:
        funcoes.buscar()
elif opcao==9:
	funcoes.encerramento()
else:
	funcoes.falha()


