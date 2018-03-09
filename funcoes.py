#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Excluir contatos da agenda")

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

def excluir():
	import csv
	lista = []
	agenda = open('agendatelefonica.csv')
	ler = csv.reader(agenda)
	for lin in ler:
		lista.append(lin)

	nome = input('Escreva o nome para excluir da agenda\n').lower()
	x=0
	while x<len(lista):
		contato = lista[x]
		if nome in contato:
			print('Deseja excluir este contato?\n')
			print('Nome {} - Telefone {}\n'.format(contato[0],contato[1]))
			resp=int(input('[1]Sim   [2]Nao'))
			if resp==1:
				del(lista[x])
				print('contato excluido')
				break
		x += 1
		if x==len(lista):
			print('contato nao encontrado')
	with open('agendatelefonica.csv', "wt") as arquivo:
		escritor = csv.writer(arquivo, delimiter=",")
		for linha in lista:
			escritor.writerow(linha)
			