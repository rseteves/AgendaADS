# Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Remover um contato da agenda")
	print("4  Buscar um contato na agenda")
	print("9  Sair do sistema")


# Funcoes do processo
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



def listar():
	print("Lista de Contatos")

	with open("agendatelefonica.csv") as agenda:
		for linha in agenda:
			print(linha.strip())

	print("\nListado correctamente\n\n")


def remover():
	print("Digite o nome para remover: ")
	nome = input()
	agenda = open("agendatelefonica.csv", "r")
	linhas = agenda.readlines()
	# Implementar o restante da função (Mauricio)


def buscar():
	print("Digite o nome para buscar")
	buscar = input()
	agenda = open("agendatelefonica.csv",'r')
	for line in agenda:
		bCount = 0
		if (buscar.upper() in line.upper()):
			bCount += 1
			print("Item {} :".format(bCount) , line)
	print("================== {} resultado(s) encontrado(s).".format(bCount))
	agenda.close()

def falha():
	print("Opcao Incorreta")
