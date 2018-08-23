import csv
#Mensagem de Bem Vindo e Opcoes ao Usuario
def menu():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1 Adicionar um novo contato")
	print("2 Listar os contatos da agenda")
	print("3 Buscar")
	print("4 Deletar")
	print("5 Sair do programa")

#Funcoes do processo
def opcao(): #retorna a opçao
        x = int(input("Insira uma opção: "))
        return x

def busca():# busca um contato na lista
        agenda = csv.reader(open('agendatelefonica.csv', 'r'))
        nome = input("Digite nome que você deseja procurar: ")
        for linhas in agenda:
                if linhas[0] == nome:
                        print("Contato: ",linhas)

def adicionar():#adiciona um contato na lista
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
	

def listar():#lista um contato 

	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()

def falha(): #mensagem de falha
	print("Opcao Incorreta")
