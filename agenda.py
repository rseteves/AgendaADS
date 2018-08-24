import funcoes
import sys
menu()
x = opcao()
#Estrutura de controle
if x==1:
    adicionar()
elif x==2:
    listar()
elif x==3:
    buscar()
elif x==4:
    deletar()
elif x==5:
    sys.exit()
