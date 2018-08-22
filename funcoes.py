#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv
import sys
def bemvindo():
	print("\nBem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1 - Adicionar um novo contato")
	print("2 - Listar os contatos da agenda")
	print("3 - Deletar contato")
	print("4 - Buscar contato")
	print("5 - Sair do programa")  
	print('----------------------------------')

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
	bemvindo()
	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado corretamente")	
	agenda.close()
	bemvindo()

def falha():
	print("Opcao Incorreta")
	bemvindo()

	
def Busca(): 
    nome_arquivo = csv.reader(open("agendatelefonica.csv", 'r'))
    nome = input("Digite o nome procurado:")
    for x in nome_arquivo:
        if x[0] == nome:
            print("Contato buscado: " , x)        
    bemvindo()    


                                
        
        
              
                
                
                
