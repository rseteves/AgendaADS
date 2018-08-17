import sys
import csv
#Faz a busca baseado no nome escolhido
def busca():
    nome_arquivo = csv.reader(open('agendatelefonica.csv', 'r'))
    #concluido de que as pessoas neste programa não terão nomes iguais
    nome = input("Digite o nome procurado: ")
    #imprimir resultado
    for rows in nome_arquivo:
        if rows[0] == nome:
                print("Contato buscado: " , rows)
    
#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("\nSelecione uma opção:")
	print("1 -> Adicionar um novo contato")
	print("2 -> Listar os contatos da agenda")
  print("3 -> Buscar um contato")
	print("4 -> Sair do programa")

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
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()

def falha():
	print("Opcao Incorreta")

def sairDoPrograma():
	print("\nA aplicação foi encerrada!")
	sys.exit()
