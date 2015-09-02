import unittest

class TestContarLetrasNumeros(unittest.TestCase):
    def test_indivisiveis(self):
        self.assertEqual(contar(1), 2)
        self.assertEqual(contar(2), 4)
        self.assertEqual(contar(3), 4)
        self.assertEqual(contar(4), 6)
        self.assertEqual(contar(5), 5)
        self.assertEqual(contar(6), 4)
        self.assertEqual(contar(7), 4)
        self.assertEqual(contar(8), 4)
        self.assertEqual(contar(9), 4)
        self.assertEqual(contar(10), 3)
        self.assertEqual(contar(11), 4)
        self.assertEqual(contar(12), 4)
        self.assertEqual(contar(13), 5)
        self.assertEqual(contar(14), 7)
        self.assertEqual(contar(15), 6)
        self.assertEqual(contar(16), 9)
        self.assertEqual(contar(17), 9)
        self.assertEqual(contar(18), 7)
        self.assertEqual(contar(19), 8)
        self.assertEqual(contar(20), 5)
        self.assertEqual(contar(30), 6)
        self.assertEqual(contar(40), 8)
        self.assertEqual(contar(50), 9)
        self.assertEqual(contar(60), 8)
        self.assertEqual(contar(70), 7)
        self.assertEqual(contar(80), 7)
        self.assertEqual(contar(90), 7)
        self.assertEqual(contar(100), 3)
        self.assertEqual(contar(200), 8)
        self.assertEqual(contar(300), 9)
        self.assertEqual(contar(400), 12)
        self.assertEqual(contar(500), 10)
        self.assertEqual(contar(600), 10)
        self.assertEqual(contar(700), 10)
        self.assertEqual(contar(800), 10)
        self.assertEqual(contar(900), 10)
        self.assertEqual(contar(1000), 3)
    
    def test_divisiveis(self):
        self.assertEqual(contar(21), 8)
        self.assertEqual(contar(22), 10)
        self.assertEqual(contar(31), 9)
        self.assertEqual(contar(32), 11)
        self.assertEqual(contar(41), 11)
        self.assertEqual(contar(42), 13)
        self.assertEqual(contar(51), 12)
        self.assertEqual(contar(53), 14)
        self.assertEqual(contar(61), 11)
        self.assertEqual(contar(101), 8)
        self.assertEqual(contar(102), 10)
        self.assertEqual(contar(124), 18)
        self.assertEqual(contar(150), 15)
        self.assertEqual(contar(153), 20)
        self.assertEqual(contar(201), 11)
        self.assertEqual(contar(472), 25)
        self.assertEqual(contar(999), 23)

    def test_soma_de_mil_numeros(self):
        soma = 0
        for numero in range(1, 1001):
            soma += contar(numero)
        self.assertEqual(19662, soma)

def contar(numero):
    indivisiveis = {
        1:2, 2:4, 3:4, 4:6, 5:5, 6:4, 7:4, 8:4, 9:4,
        10:3, 11:4, 12:4, 13:5, 14:7, 15:6, 16:9, 17:9, 18:7, 19:8,
        20:5, 30:6, 40:8, 50:9, 60:8, 70:7, 80:7, 90:7,
        100:3, 200:8, 300:9, 400:12, 500:10, 600:10, 700:10, 800:10, 900:10,
        1000:3
    }
    if numero in indivisiveis:
        return indivisiveis[numero]
    for indivisivel in sorted(indivisiveis.keys(), reverse=True):
        if numero > indivisivel:
            if indivisivel == 100:
                return indivisiveis[indivisivel] + 3 + contar(numero - indivisivel)
            else:
                return indivisiveis[indivisivel] + 1 + contar(numero - indivisivel)

if __name__ == '__main__':
    unittest.main()
