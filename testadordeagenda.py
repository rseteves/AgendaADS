# coding:utf-8
import unittest
import funcoes
#Criando a classe que herda o unittest.TestCase

#Padrão a ser usado: Arrange-Act-Assert
#Primeiro: define comportamento(input e output esperado)

class VerificaUnitarioDevOps(unittest.TestCase):

    def test_metodo_1_Cadastro(self):
        nome = "queiroz"
        tel = "44432858"
        cad1 = funcoes.adicionar(nome, tel, 2)
        self.assertEqual(cad1,True)
        if(cad1 == True):
            funcoes.DeletarContato(nome, 2)

    def test_metodo_2_Cadastro(self):
        nome = "queiroz"
        tel = 44432858
        cad1 = funcoes.adicionar(nome, tel, 2)
        self.assertEqual(cad1,False)

    def test_metodo_3_Consulta(self):
        consu1 = funcoes.listar(2)
        self.assertEqual(consu1,True)

    def test_metodo_4_Deletar(self):
        funcoes.adicionar("queiroz2", "44432858", 2)
        del1 = funcoes.DeletarContato("queiroz2", 2)
        self.assertEqual(del1,True)

    def test_metodo_5_Deletar(self):
        del1 = funcoes.DeletarContato(2344,2)
        self.assertEqual(del1,False)
        
        
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(VerificaUnitarioDevOps)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)
