import csv
#Mensagem de Bem Vindo e Opcoes ao Usuario
def menu():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1 Adicionar um novo contato")
	print("2 Listar os contatos da agenda")
	print("3 Buscar")
	print("4 Deletar")
	print("5 Sair do programa")

#Funcoes do processo
def opcao(): #retorna a opçao
        x = int(input("Insira uma opção: "))
        return x
    
def deletar(): #deletar um contato
    import csv
    lista = []
    print("Remover um contato")
    agenda = open("agendatelefonica.csv")
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
                            print('Contato removido com sucesso!')
                            print('Contatos restantes: \n',lista,'\n')
                            agenda.close()
                    break
            else:
                print (' Contato não existe')
                
def busca():# busca um contato na lista
        agenda = csv.reader(open('agendatelefonica.csv', 'r'))
        nome = input("Digite nome que você deseja procurar: ")
        for linhas in agenda:
                if linhas[0] == nome:
                        print("Contato: ",linhas)

def adicionar():
    print("Adicionar um registro")
    agenda = open("agendatelefonica.csv",'a')
    nome = input("Nome do Contato: ")
    telefone = input("Digite o telefone: ")
    print("Contato salvo com nome: ",nome," e numero ",telefone)
    agenda.write(nome)
    agenda.write(",")
    agenda.write(telefone)
    agenda.write("\n")
    agenda.close()
    print("\nQuer add mais um ?")
    print("1-Sim ou 2-Não")
    s = int(input("digite sua opção:"))
    while s == 1:
        adicionar()
        print("Quer add mais um ?")
        print("1-Sim ou 2-Não")
        s = int(input("digite sua opção:"))
    if s == 2:
        volta()
		
def listar():#lista um contato 

	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	for linhas in agenda:
                if linhas[0] == nome:
                        print("Contato: ",linhas)
	agenda.close()

def falha(): #mensagem de falha
	print("Opcao Incorreta")
