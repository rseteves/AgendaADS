import csv


# Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
    print('\n')
    print("Bem Vindo a Agenda")
    print("Selecione uma Opcao")
    print("1  Adicionar um novo contato")
    print("2  Listar os contatos da agenda")
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
    agenda.write(",")
    agenda.write("\n")
    agenda.close()


def deletar():
    with open("agendatelefonica.csv") as agenda:
        reader = csv.reader(agenda, delimiter=',')

        lista = list(reader)
    listar()
    nome = str("")

    while nome not in ([row[0] for row in lista]):
        nome = input("Digite o nome do contato que você deseja deletar: ")

    lista.pop([row[0] for row in lista].index(nome))

    with open("agendatelefonica.csv", "w") as f:
        writer = csv.writer(f)
        for row in lista:
            writer.writerow(row)


def listar():
    print("Lista de Contatos")
    agenda = open("agendatelefonica.csv")
    numero = 0
    while numero < 25:
        print(agenda.readline())
        numero = numero + 1
    print("Listado correctamente")
    agenda.close()


def falha():
    print("Opcao Incorreta")
