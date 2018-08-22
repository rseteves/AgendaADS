import funcoes
import csv
with open("agendatelefonica.csv") as agenda:
    reader = csv.reader(agenda)
    lista = list(reader)

def test_listar():
    assert funcoes.listar(2) == len(lista)