# Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("="*12)
	print("Bem Vindo a Agenda")
	print("="*12)

	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Remover um contato da agenda")
	print("4  Buscar um contato na agenda")
	print("9  Sair do sistema")


# Funcoes do processo
def adicionar():
	print("="*12)
	print("\033[32m Adicionar um registro\033[m")
	print("="*12)
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
	print("="*12)
	print("\033[32m Lista de Contatos\033[m")
	print("="*12)

	with open("agendatelefonica.csv") as agenda:
		for linha in agenda:
			print(linha.strip())

	print("\nListado correctamente\n\n")


def remover():
	print("="*12)
	print("\033[32m Digite o nome para remover:\033[m ")
	print("="*12)

	nome = input()
	agenda = open("agendatelefonica.csv", "r")
	linhas = agenda.readlines()

	for linha in linhas:
		if nome in linha:
			linhas.remove(linha)

	agenda.close()
	agenda = open("agendatelefonica.csv", "w")
	agenda.writelines(linhas)
	agenda.close()


def buscar():
	print("="*12)
	print("\033[32m Digite o nome para buscar\033[m")
	print("="*12)
	buscar = input()
	agenda = open("agendatelefonica.csv",'r')
	bCount = 0
	for line in agenda:
		if (buscar.upper() in line.upper()):
			bCount += 1
			print("Item {} :".format(bCount) , line)
	print("================== {} resultado(s) encontrado(s).".format(bCount))
	agenda.close()

def falha():
	print("\033[31m Opção Incorreta\033[m")
