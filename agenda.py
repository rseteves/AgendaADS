#Danilo Silva Babilius		RA1800140
#Diego de Almeida Saraiva	RA1800054
#Rodrigo Rodrigues da Silva	RA1800409
#Rogerio Alves Santos		RA1800386
#William Bruce Ogura		RA1800114

#Agenda Telefonica
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(input())
print("Seleccionaste", opcao)


#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 4:
	funcoes.deletar()
elif opcao == 5:
        funcoes.encontrar(str(input("Digite o nome que deseja encontrar:")))
else:
	funcoes.falha()	
