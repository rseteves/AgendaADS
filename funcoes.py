import csv

#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("4  Buscar contato da lista")
	print("9  Sair da aplicação")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato: ")
	telefone = input("Digite o telefone: ")
	print("Contato salvo com nome:",nome,"e numero",telefone,"\n")
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()

def listar():
	print("Lista de Contatos")
	with open('agendatelefonica.csv', 'r') as agenda:
		csvreader = csv.reader(agenda)
		for row in csvreader:
			print ('|'.join(row))
	print("Listado correctamente\n")
	agenda.close()

def buscar():
        tentativa = 3
        lista = []
        print("Busca de Contatos")
        with open("agendatelefonica.csv") as agenda:
                reader = csv.reader(agenda)
                for linha in reader:
                        lista.append(linha)
        while tentativa > 0:
                nomeBusca = input("Informe um nome para ser localizado: ")
                for linha in lista:
                        if linha[0] == nomeBusca:
                                print("Dados localizados:")
                                print("Nome: ", linha[0])
                                print("Telefone: ", linha[1],"\n")
                                return
                print("Nome não encontrado")
                tentativa = tentativa - 1
        print("Excedido número de tentativas. Você será redirecionado ao menu principal!\n")
        agenda.close

def falha():
	print("Opcao Incorreta\n")

def encerramento():
        print("Você pediu o encerramento do programa")
