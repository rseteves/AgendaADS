import csv

def bemvindo():
	print("Bem Vindo a Agenda")
	print("\n")
	print("Opções disponíveis: ")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Apagar um contato")
	print("4  Buscar um contato")
	print("5  Encerrar o programa")
	print("\n")

  
#Funcoes do processo
def adicionar():
	print("Adicionar um novo contato")
	print("\n")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("\n")
	print("Contato salvo com Nome:",nome," e Número:",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	print("\n")

def listarR():
	print("Lista de Contatos:")
	agenda = open("agendatelefonica.csv")
	contact = csv.reader(agenda)
	for y in contact:
		print (y)
	print("\n")
	print("Contatos listados corretamente!")
	print("\n")
	agenda.close()
