import funcoes
import sys
errolistar = False

listar = funcoes.listar()

if listar != "":
  errolistar = True

if errolistar:
	sys.exit(1)
else:
	sys.exit(0)
