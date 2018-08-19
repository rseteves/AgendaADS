#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("4  buscar os contatos da agenda")
	print("9  para sair")

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
        #print("Lista de Contatos")
        agenda = open("agendatelefonica.csv")
        numero = 0
        for num in range(25):
                print (">>>"agenda.readline()"<<<")		
        print("Listado corretamente")
        agenda.close()
	
def buscar(nome):
    agenda = open("agendatelefonica.csv",'r')
    for linha in agenda:
        linha=linha.rstrip()
    if nome in linha:
        print(linha)
    else:
        print("Nome não localizado")
    agenda.close()

def falha():
	print("Opcao Incorreta")
