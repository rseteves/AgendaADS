#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("""Selecione a Opção: 
			1 - Adicionar 	
			2 - Listar 
			3 - Buscar 
			4 - Sair""")
	opcao = int(input("Opção: "))

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
    	
	print("Lista de Contatos \n")
	agenda = open("agendatelefonica.csv")
	
	for linha in agenda:
    		print(linha.split(',')[0]+ ' - ' + linha.split(',')[1])

	print("\nListado correctamente!")	

	agenda.close()

def falha():
	print("Opcao Incorreta")
