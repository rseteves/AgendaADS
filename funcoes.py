import csv
#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1 Adicionar um novo contato")
	print("2 Listar os contatos da agenda")
	print("3 Buscar")
	print("4 Deletar")
	print("5 Sair do programa")

#Funcoes do processo
def opcao():
        x = int(input("Insira uma opção: "))
        return x

def buscar():
        agenda = csv.reader(open('agendatelefonica.csv', 'r'))
        nome = input("Digite o nome a ser procurado: ")
        for linhas in agenda:
                if linhas[0] == nome:
                        print(linhas)

def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write("\n")
	agenda.close()
	
def listar():
        print("Lista de Contatos")
        agenda = open("agendatelefonica.csv")
        for linhas in agenda:
                print(linhas)
        print("Listado corretamente")	
        agenda.close()

def falha():
	print("Opcao Incorreta")
