import funcoes
import csv

x="Gigio"
y="222"
t=funcoes.adicionar(x,y)

print("Lista de Contatos")
with open('agendatelefonica.csv', 'r') as agenda:
    csvreader = csv.reader(agenda)
    for row in csvreader:
        if ','.join(row) == "Gigio,222,": 
            t=(True)



assert t == True
