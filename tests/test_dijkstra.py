import unittest
from src.core.graph import Graph
from src.algorithms.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):

    def test_caso_base(self):
        """Caso 1: Entrada válida com resultado conhecido"""
        g = Graph()
        g.add_node(1)
        g.add_node(2)
        # W = 10 * 1 = 10
        g.add_edge(1, 2, distance=10, risk_factor=1) 
        caminho, custo = dijkstra(g, 1, 2)
        self.assertEqual(caminho, [1, 2])
        self.assertEqual(custo, 10)

    def test_grafo_vazio(self):
        """Caso 2: Comportamento com entrada vazia ou nula"""
        g = Graph()
        caminho, custo = dijkstra(g, 1, 2)
        self.assertEqual(caminho, [])

    def test_grafo_completo(self):
        """Caso 3: Grafo completo (todos conectados)"""
        g = Graph()
        for i in range(1, 4): g.add_node(i)
        g.add_edge(1, 2, 5, 1)  # Peso 5
        g.add_edge(2, 3, 5, 1)  # Peso 5 (Total 1 a 3 = 10)
        g.add_edge(1, 3, 20, 1) # Caminho direto mais caro (Peso 20)
        caminho, custo = dijkstra(g, 1, 3)
        # Deve escolher o caminho mais barato via nó 2
        self.assertEqual(caminho, [1, 2, 3]) 
        self.assertEqual(custo, 10)

if __name__ == '__main__':
    unittest.main()