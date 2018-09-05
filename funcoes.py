import sys
import csv

def volta():
    print("\n")
    bemvindo()
    
def Estrutura(opcao):
    if opcao == 1:
        nome = input("Nome do Contato: ")
        telefone = input("Digite o telefone: ")
        adicionar(nome, telefone)
    elif opcao == 2:
        listar()
    elif opcao == 3:
        nome = input("Digite o nome procurado: ")
        Busca(nome)
    elif opcao == 4:
        nome = input("Digite o nome do contato a ser deletado: ")
        DeletarContato(nome)
    elif opcao == 5:
        sairDoPrograma()
    else:
        falha()
    
    
#Faz a busca baseado no nome escolhido
#Variavel teste é opcional
#Caso não passarem o valor dela, ela mesmo se insere um
def Busca(nome, teste = 1):
    nome_arquivo = csv.reader(open('agendatelefonica.csv', 'r'))
    #concluido de que as pessoas neste programa não terão nomes iguais
    #imprimir resultado
    for rows in nome_arquivo:
        if rows[0] == nome:
                #Caso for um teste, retorna valor ao teste
            if(teste==2):
                return True
            #Caso for o usuario, o código continua normal
            print("Contato buscado: " , rows)
    if(teste == 1):
        volta()

#Realiza a exclusão de um contato
def DeletarContato(nome, teste =1):
    try:
        agenda = [line for line in open("agendatelefonica.csv")]
        #delete da o contato da variavel agenda
        for item in agenda:
            if nome.lower().capitalize() in item:
                agenda.remove(item)

        #abre uma outra agenda para sobreescrever com a agenda com o contato ja deletado
        agenda_secundaria = open("agendatelefonica.csv", 'w')
        agenda_secundaria.writelines(agenda)
        agenda_secundaria.close()
        if(teste == 1):
            listar()
        elif(teste == 2):
            return True
    except Exception:
        if(teste == 1):
            print("Digite um nome válido")
            volta()
        elif(teste == 2):
            return False
    
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
def adicionar(nome, telefone, teste = 1):
    try:
        agenda = open("agendatelefonica.csv",'a')
        agenda.write(nome.lower().capitalize())
        agenda.write(",")
        agenda.write(telefone)
        agenda.write("\n")
        agenda.close()
        if(teste == 1):
            print("Contato salvo com nome: ",nome," e numero ",telefone)
            listar()
        elif(teste == 2):
            return True
    except Exception:
        if(teste == 1):
            print("Digite um nome ou um telefone válido")
            volta()
        elif(teste == 2):
            return False
	
def listar(teste =1):
    #usando try catch para verificar erros
    #Usando comparação de testes:
    #quando for 1 é usuario quando for 2 é testeUnitario
    try:
        if(teste == 1):
            print("Lista de Contatos\n")
        agenda = open("agendatelefonica.csv")
        for rows in agenda:
            if(teste == 1):
                print(rows)
        agenda.close()
        if(teste == 1):
            volta()
        elif(teste == 2):
            return True
    except Exception:
        if(teste == 1):
            print("Existe algum problema com teu arquivo CSV")
            volta()
        elif(teste == 2):
            return False

def falha():
	print("Opcao Incorreta")
	volta()
        
def sairDoPrograma():
	print("\nA aplicação foi encerrada!")
	sys.exit()

