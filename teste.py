import funcoes.py
import sys
errolistar = False

listar = funcoes.listar()

if list != "":
  errolistar = True

if errolistar:
	sys.exit(1)
else:
	sys.exit(0)
