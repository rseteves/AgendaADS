#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")

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

def buscar():
	array_contatos = []
	contato_escolhido = []
	valor_busca = input("Digite o nome ou o telefone para buscar:")
	csv = open("agendatelefonica.csv","r")
	arquivo = csv.readlines()
	for contatos in arquivo :
		array_contatos = contatos.split(",")
		if(array_contatos[0] == valor_busca) :
	   		contato_escolhido.append(contatos)
		elif(array_contatos[1] == valor_busca) :
			contato_escolhido.append(contatos)
	print("Resultados da busca:",len(contato_escolhido))
	if(len(contato_escolhido) >= 1) :
		for resultados in contato_escolhido :
			resultados = resultados.split(",")
			print("Nome:",resultados[0]," - Contato:",resultados[1])
