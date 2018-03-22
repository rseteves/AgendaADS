import funcoes
import csv

funcoes.adicionar("Gigio","222")
print("Lista de Contatos")
with open('agendatelefonica.csv', 'r') as agenda:
    csvreader = csv.reader(agenda)
    for row in csvreader:
        if ','.join(row) == "Gigio,222,": 
            return (True)

x="Gigio"
y="222"
t=adicionar(x,y)

assert t == True
