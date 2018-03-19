import csv


# Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
    print('\n')
    print("Bem Vindo a Agenda")
    print("Selecione uma Opcao")
    print("1  Adicionar um novo contato")
    print("2  Listar os contatos da agenda")
    print("4  Para procurar contatos na agenda")
    print("5  Remover um contato")
    print("9  Para encerrar programa")


# Funcoes do processo
def adicionar():
    print("Adicionar um registro")
    agenda = open("agendatelefonica.csv", 'a')
    nome = input("Nome do Contato:")
    telefone = input("Digite o telefone:")
    print("Contato salvo com nome:", nome, " e numero", telefone)
    agenda.write(nome)
    agenda.write(",")
    agenda.write(telefone)
    agenda.write("\n")
    agenda.close()

def deletar():
    with open("agendatelefonica.csv") as agenda:
        reader = csv.reader(agenda, delimiter=',')

        lista = list(reader)
    listar(0)
    nome = str("")

    while nome not in ([row[0] for row in lista]):
        nome = input("Digite o nome do contato que você deseja deletar: ")

    lista.pop([row[0] for row in lista].index(nome))

    with open("agendatelefonica.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for row in lista:
            writer.writerow(row)

    print("Contato removido")
    nome = input("\n Pressione qualquer tecla para continuar: ")


def listar(x):
    print("Lista de Contatos")
    print("[Nome][Telefone]")
    with open("agendatelefonica.csv") as agenda:
        reader = csv.reader(agenda)
        lista = list(reader)
        for row in reader:
            print("Nome : {} >>>>>> Telefone: {}".format(row[0],row[1]))
    print("Listado correctamente")

    if x==1:
        a = input("\n Digite qualquer tecla para continuar: ")
    return len(lista)

def falha():
    print("Opcao Incorreta")


def buscar():
    name = input("Digite o nome para procurar: ")
    with open("agendatelefonica.csv") as agenda:
        reader = csv.reader(agenda, delimiter=',')
        test = None
        for row in reader:
            if name in row:
                test = ("Nome: {} >>>>>> Telefone {} ".format(row[0], row[1]))
        if test is not None:
                print(test)
        else:
            print("Contato não encontrato")
    
    name = input("\n Pressione qualquer tecla para continuar.")
