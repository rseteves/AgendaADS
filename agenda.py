# Agenda Telefonica

import funcoes

funcoes.bemvindo()

<<<<<<< HEAD
#Opcoes do Usuario
=======
# Opcoes do Usuario
>>>>>>> 2db1c65c543b77800805ad8498034525b9c78aaf
opcao = int(input())
print("Seleccionaste", opcao)


<<<<<<< HEAD
#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 4:
	funcoes.buscar()
else:
	funcoes.falha()
=======
while opcao != 9:
	# Estrutura de controle
	if opcao == 9:
		agenda.close()

	if opcao == 1:
		funcoes.adicionar()
	elif opcao == 2:
		funcoes.listar()
	else:
		funcoes.falha()
>>>>>>> 2db1c65c543b77800805ad8498034525b9c78aaf

	funcoes.bemvindo()

	# Opcoes do Usuario
	opcao = int(input())
	print("Seleccionaste", opcao)
