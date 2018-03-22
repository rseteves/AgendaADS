import funcoes
import csv

def teste():
    print("Lista de Contatos")
    with open('agendatelefonica.csv', 'r') as agenda:
        csvreader = csv.reader(agenda)
        for row in csvreader:
            if ','.join(row) == "Gigio,222,": 
                return (True)

assert funcoes.adicionar(x,y) == True
