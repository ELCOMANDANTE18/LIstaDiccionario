import unittest

from main import busqueda

class TestSearch(unittest.TestCase):
    def test_simple(self):
        lista = [1]
        encontrado = busqueda(lista, 1)
        self.assertTrue(encontrado)


    def test_simple_not_found(self):
        lista = [2]
        encontrado = busqueda(lista, 1)
        self.assertFalse(encontrado)


    def test_complex(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        encontrado = busqueda(lista, 3)
        self.assertTrue(encontrado)

    def test_complex_not_found(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        encontrado = busqueda(lista, 10)
        self.assertFalse(encontrado)



if __name__ == '__main__':
    unittest.main()
