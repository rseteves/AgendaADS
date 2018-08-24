import csv
import sys
#Mensagem de Bem Vindo e Opcoes ao Usuario

def bemvindo():
    print("Bem Vindo a Agenda")
    print("Selecione uma Opcao")
    print("1  Adicionar um novo contato")
    print("2  Listar os contatos da agenda")
    print("3  Buscar seu contato salvo")
    print("4  Deletar um contato salvo")
    print("5  Sair da agenda")
    x = int(input("Escolha sua opção ! "))    
    if x == 1:
        print ("SELECIONADA = Adicionar novo contato selecionado")
        adicionar()
    elif x == 2:
        print (" SELECIONADA = Listar os contatos da agenda")
        lista()
    elif x == 3:
        print ("SELECIONADA = Buscar seu contato salvo")
        busca()
    elif x == 4:
        print ("SELECIONADA = Deletar nome na sua lista")
        deletar()
    elif x == 5:
        print ("SELECIONADA = Parar agenda! ")
        sair ()


def voltar():
    print()
    bemvindo()

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
	voltar()

# DEFINE FUNÇÃO DE LISTAR	
def lista():
    print("\nAgenda\n\n------")
    agenda = open("agendatelefonica.csv",'r')
    for i in agenda:
        print(i)
    voltar()





    
#DEFINE FALHA
def falha():
    print("Opcao Incorreta")
    voltar()

    
    

