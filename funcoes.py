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

def deletar(var_nomedeletar)
    print(("""Tem certeza que quer deletar essa entrada? 
    
    1 - Sim
    2 - Não
    """))
    vopcao = (int(input("Opção: "))
    if vopcao == 1:
        text_file = open("agendatelefonica.csv", "r") ##Abre o Arquivo
        nomes = text_file.readlines() ##Le todas as linhas 
        text_file.close() ##Fecha o arquivo
        text_file = open("agendatelefonica.csv", "w") ##Abre o Arquivo para escrita
        for linha in nomes:  ##Percorre o Arquivo
            if linha != var_nomedeletar + '\n':  ##Pergunta se a linha é a que queremos deletar
                text_file.write(linha)  ##Se não for, reescreve a linha no arquivo
        text_file.close()  ##Fecha o Arquivo
        print("Registro deletado com sucesso")  ##Feedback
    else:
        print("Registro preservado")
