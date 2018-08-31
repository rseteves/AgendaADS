import sys
import csv

def volta():
    print("\n")
    bemvindo()
    
def Estrutura(opcao):
    if opcao == 1:
        nome = input("Nome do Contato: ").lower().capitalize()
        telefone = input("Digite o telefone: ")
        adicionar(nome, telefone)
    elif opcao == 2:
        listar()
    elif opcao == 3:
        nome = input("Digite o nome procurado: ")
        Busca(nome)
    elif opcao == 4:
        nome = input("Digite o nome do contato a ser deletado: ").lower().capitalize()
        DeletarContato(nome)
    elif opcao == 5:
        sairDoPrograma()
    else:
        falha()
    
    
#Faz a busca baseado no nome escolhido    
def Busca(nome):
    nome_arquivo = csv.reader(open('agendatelefonica.csv', 'r'))
    #concluido de que as pessoas neste programa não terão nomes iguais
    #imprimir resultado
    for rows in nome_arquivo:
        if rows[0] == nome:
                print("Contato buscado: " , rows)
    volta()

#Realiza a exclusão de um contato
def DeletarContato(nome):
    agenda = [line for line in open("agendatelefonica.csv")]
    #delete da o contato da variavel agenda
    for item in agenda:
        if nome in item:
            agenda.remove(item)

    #abre uma outra agenda para sobreescrever com a agenda com o contato ja deletado
    agenda_secundaria = open("agendatelefonica.csv", 'w')
    agenda_secundaria.writelines(agenda)
    agenda_secundaria.close()

    listar()
    
#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
    print("Bem Vindo a Agenda")
    print("\nSelecione uma opção:")
    print("1 -> Adicionar um novo contato")
    print("2 -> Listar os contatos da agenda")
    print("3 -> Buscar um contato")
    print("4 -> Deletar um contato")
    print("5 -> Sair do programa")
    print("Selecione uma Opcao")
    opcao = int(input())
    print("Selecionado", opcao)
    Estrutura(opcao)

 #Funcoes do processo
def adicionar(nome, telefone):
    print("Adicionar um registro")
    agenda = open("agendatelefonica.csv",'a')
    print("Contato salvo com nome: ",nome," e numero ",telefone)
    agenda.write(nome)
    agenda.write(",")
    agenda.write(telefone)
    agenda.write("\n")
    agenda.close()
    volta()
	
def listar():
    print("Lista de Contatos\n")
    agenda = open("agendatelefonica.csv")
    for rows in agenda:
        print(rows)
    agenda.close()
    volta()

def falha():
	print("Opcao Incorreta")
	volta()
        
def sairDoPrograma():
	print("\nA aplicação foi encerrada!")
	sys.exit()

