import csv

#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("4  Apagar um contato")

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
	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero > 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()

def deletar():
        with open("agendatelefonica.csv","r") as agenda:
                reader = csv.reader(agenda)
                data = list(reader)
        nome=str("")
        while nome not in ([row[0] for row in data]):
                nome = input("Nome do contato a ser deletado: ")
        data.pop([row[0] for row in data].index(nome))
        with open("agendatelefonica.csv","w",newline="") as file:
                writer = csv.writer(file)
                for row in data :
                        writer.writerow(row)
        print("Contato removido com sucesso!!")
        bemvindo()
def falha():
	print("Opcao Incorreta")
