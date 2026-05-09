import unittest
from src.core.graph import Graph
from src.service.navigation import NavigationService

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_node(1, "Estação da Luz")
        self.graph.add_node(2, "SESC 24 de Maio")
        self.graph.add_edge(1, 2, 450, 1.5, True)
        self.service = NavigationService(self.graph)

    def test_caso_base(self):
        """Teste de rota válida"""
        path, cost = self.service.calculate_route(1, 2)
        self.assertEqual(path, [1, 2])
        self.assertEqual(cost, 675.0)

    def test_grafo_vazio(self):
        """Teste de segurança para pontos inexistentes"""
        empty_graph = Graph()
        service_vazio = NavigationService(empty_graph)
        path, cost = service_vazio.calculate_route(99, 100)
        self.assertEqual(path, [])
        self.assertEqual(cost, float('inf'))

    def test_conectividade_total(self):
        """Teste de caminho com múltiplos pontos"""
        self.graph.add_node(3, "Ponto Extra")
        self.graph.add_edge(2, 3, 100, 1.0, True)
        path, cost = self.service.calculate_route(1, 3)
        self.assertIn(3, path)
        self.assertEqual(len(path), 3)

if __name__ == '__main__':
    unittest.main()