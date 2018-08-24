
# RA 1800306 DIEGO HANS MULLER
# RA 1800305 MATHEUS P. TAVARES
# RA 1800330 MATHEUS MENDES
# RA 1800387 RAFAEL CAVALCANTI
# RA 1801135 MATHEUS LACERDA 
# RA 1800377 VITOR REIS
# RA 1800959 VINICIUS OLIVEIRA





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

#DEFINE FUNÇÃO BUSCAR
def busca():
    agenda = csv.reader(open("agendatelefonica.csv",'r'))
    nome = input("Digite o contato para procurar: ")
    for rows in agenda:
        if rows[0] == nome:
            print(rows)
    voltar()



# DEFINE FUNÇÃO DELETAR
def deletar():
    agenda = [line for line in open("agendatelefonica.csv")]
    nome = input("Digite o nome do contato a ser deletado: ").lower().capitalize()
    for item in agenda:
        if nome in item:
            agenda.delete(item)
    lista()
    voltar()

#DEFINE FALHA
def falha():
    print("Opcao Incorreta")
    voltar()

	
# DEFINE SAIR
def sair():
	print("Seu programa foi fechado ")
	sys.exit()
    
    

