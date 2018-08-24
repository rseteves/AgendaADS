#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("""Selecione a Opção: 
			1 - Adicionar 	
			2 - Listar 
			3 - Buscar
			4 - Remover 
			5 - Sair""")

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

def deletar():
	lista_arquivo = []
	var_nomedeletar = input("Digite o nome do contato para deletar:")
	print(("""Tem certeza que quer deletar essa entrada? 
    1 - Sim
    2 - Não
    """))
	vopcao = int(input("Opção: "))
	if vopcao == 1:
		text_file = open("agendatelefonica.csv", "r") ##Abre o Arquivo
		nomes = text_file.readlines() ##Le todas as linhas 
		text_file.close() ##Fecha o arquivo
		text_file = open("agendatelefonica.csv", "w") ##Abre o Arquivo para escrita
		for linha in nomes:  ##Percorre o Arquivo
			lista_arquivo = linha.split(",")
			if lista_arquivo[0] != var_nomedeletar:  ##Pergunta se a linha é a que queremos deletar
				text_file.write(linha)  ##Se não for, reescreve a linha no arquivo
		text_file.close()  ##Fecha o Arquivo
		print("Registro deletado com sucesso")  ##Feedback
	else:
		print("Registro preservado")
