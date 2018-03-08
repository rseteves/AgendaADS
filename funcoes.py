#Mensagem de Bem Vindo e Opcoes ao Usuario
import sys #modulo importado para uso da def exit() /sys.exit()/

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("4  Para procurar um contato")
	print("9  Para fechar o programa")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(", ")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	# agenda.close()
	
def listar():
	print("Lista de Contatos")
	with open("agendatelefonica.csv", "r") as file:
		for linha in file:
			print(linha)
	

def close():
	sys.exit()

def buscarcontato():
	with open("agendatelefonica.csv", "r") as archive:
		contato = input('Digite o contato: ')
	for linha in archive:
		if linha.find(contato) > -1:
			print('Contatos encontrados: ')
			print(linha)
		else:
			print('Comando invalido!')
			break 
