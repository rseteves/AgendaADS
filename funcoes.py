#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv
import sys
def bemvindo():
    print("\nBem Vindo a Agenda")
    print("Selecione uma Opcao")
    print("1 - Adicionar um novo contato")
    print("2 - Listar os contatos da agenda")
    print("3 - Deletar contato")
    print("4 - Buscar contato")
    print("5 - Sair do programa")
    print('----------------------------------')
    opcao = int(input())
    print("Selecionaste", opcao)

    #Estrutura de controle
    if opcao==1:
        adicionar()
    elif opcao==2:
        listar()
    elif opcao==3:
        deletanum()
    elif opcao==4:
        Busca()
    elif opcao==5:
        Sair()
    else:
        falha()

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	bemvindo()
	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado corretamente")	
	agenda.close()
	bemvindo()

def falha():
	print("Opcao Incorreta")
	bemvindo()

	
def Busca(): 
    nome_arquivo = csv.reader(open("agendatelefonica.csv", 'r'))
    nome = input("Digite o nome procurado:")
    for x in nome_arquivo:
        if x[0] == nome:
            print("Contato buscado: " , x)        
    bemvindo()

def deletanum():
    agenda = [linha for linha in open("agendatelefonica.csv")]
    name = input("Insira o nome do contato que você deseja excluir:")
    for pessoa in agenda:
        if name in pessoa:
            agenda.remove(pessoa)
            print("Contato apagado com suecesso")
        else:
             print("Erro")
    

    agenda_apoio = open("agendatelefonica.csv","w")
    agenda_apoio.writelines(agenda)
    agenda_apoio.close()
    bemvindo()

def Sair():
    print("sair do programa")
    sys.exit()
    
        
        
              
                
                
                
