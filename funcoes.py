import funcoes
import sys
import shelve
import teste
#Mensagem de Bem Vindo e Opcoes ao Usuario

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("5  Excluir contatos")
	

#Funcoes do processo


def adicionar(a,b):
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = a #input("Nome do Contato: ")
	telefone = b #input("Digite o telefone: ")
	print("Contato salvo com nome:",nome,"e numero",telefone,"\n")
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	x = teste.teste()
	print("adicionado")
	return x

'''def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = raw_input("Nome do Contato:")
	telefone = raw_input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
'''	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()

def falha():
	print("Opcao Incorreta")
	
def procura_numero(agenda, nome):
        agenda = open("agendatelefonica.csv")
        nome = input()
        if nome in agenda:
            print(nome, agenda[nome])
        else:
            print(nome, "não está na agenda.")
        agenda.close()


def apaga():
        print ("Opção exclir contato")
        agenda = [ line for line in open("agendatelefonica.csv")]
        nome = input("Nome do Contato:")
        for item in agenda:
                if nome in item:
                        agenda.remove(item)
                        print(item)
        print(agenda)
        archive = open("agendatelefonica.csv", 'w')
        archive.writelines(agenda)
        archive.close()
