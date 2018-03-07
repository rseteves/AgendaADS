import csv

#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("4  Buscar contato da lista")
	print("5  Remover contato da lista")
	print("9  Sair da aplicação")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato: ")
	telefone = input("Digite o telefone: ")
	print("Contato salvo com nome:",nome,"e numero",telefone,"\n")
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()

def remover():
        lista = []
        print("Remover um contato")
        with open("agendatelefonica.csv") as agenda:
                reader = csv.reader(agenda)
                for linha in reader:
                        lista.append(linha)
        nome = input('Nome: ')
        for i in range (len(lista)):
                if lista[i][0] == nome:
                        print('Excluir {}? (s/n): '.format(nome))
                        sn = input()
                        if sn == 's' or 'Sim' or 'sim':
                                lista.remove(lista[i])
#                                agenda = open('agendatelefonica.csv', 'wb') #se habilitar essa linha, apaga todos os contatos, mesmo selecionando apenas 1.
                                print('Contato removido com sucesso!')
                                print('Contatos restantes: \n',lista,'\n')
                                agenda.close()
                        break
                else:
			print ('**** Contato não existe ****')
def listar():
	print("Lista de Contatos")
	with open('agendatelefonica.csv', 'r') as agenda:
		csvreader = csv.reader(agenda)
		for row in csvreader:
			print ('|'.join(row))
	print("Listado correctamente\n")
	agenda.close()

def buscar():
        tentativa = 3
        lista = []
        print("Busca de Contatos")
        with open("agendatelefonica.csv") as agenda:
                reader = csv.reader(agenda)
                for linha in reader:
                        lista.append(linha)
        while tentativa > 0:
                nomeBusca = input("Informe um nome para ser localizado: ")
                for linha in lista:
                        if linha[0] == nomeBusca:
                                print("Dados localizados:")
                                print("Nome: ", linha[0])
                                print("Telefone: ", linha[1],"\n")
                                return
                print("Nome não encontrado")
                tentativa = tentativa - 1
        print("Excedido número de tentativas. Você será redirecionado ao menu principal!\n")
        agenda.close

def falha():
	print("Opcao Incorreta\n")

def encerramento():
        print("Você pediu o encerramento do programa")
