#Agenda Telefonica
import funcoes

opcao = "0"

#Opcoes do Usuario
while opcao != "9":
        funcoes.bemvindo(x)
        opcao = input()
        print("Seleccionaste", opcao)

        #Estrutura de controle
        if opcao == "1":
                funcoes.adicionar()
        elif opcao == "2":
                funcoes.listar()
        elif opcao == "4":
               return funcoes.buscar()
        elif opcao == "5":
                funcoes.remover()
        elif opcao == "9":
               return funcoes.encerramento()
        else:
                funcoes.falha()


