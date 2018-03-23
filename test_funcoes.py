def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
    
#testa função inserir
def teste(tipo, nome):

  if tipo == 1:
        import csv

        lista = []

        with open('agendatelefonica.csv') as csvfile:

                leitor = csv.reader(csvfile, delimiter=',')

                for linha in leitor:

                        lista.append(linha)

        x=0



        while x<len(lista):

                a = lista[x]

                if nome in a:

                        print('\nNome: {} - Telefone: {}'.format(a[0],a[1]))

                x+=1

        if x == len(lista):

                print('\n\nO contato foi inserido com sucesso')

        else:

          print('\n\nO contato não foi inserido com sucesso')
