#Mensagem de Bem Vindo e Opcoes ao Usuario
def back():
    print("\n")
    bemvindo()
	
	
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")

#Funcoes do processo
def adicionar():
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
	back()
	
	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()
	back()

def falha():
	print("Opcao Incorreta")
	
	
def apagar():
    agenda = [line for line in open("agendatelefonica.csv")]
    nomeApagar = input("Digite o nome do contato a ser deletado: ").lower().capitalize()
    for y in agenda:
        if nomeApagar in y:
            agenda.remove(y)

    
    OutraAgenda= open("agendatelefonica.csv", 'w')
    OutraAgenda.writelines(agenda)
    OutraAgenda.close()

    listar()
