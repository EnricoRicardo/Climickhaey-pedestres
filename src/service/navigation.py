from src.algorithms.dijkstra import dijkstra

class NavigationService:
    def __init__(self, graph):
        self.graph = graph

    def calculate_route(self, start_node, end_node, pcd_filter=False):
        """
        Coordena a navegação, aplicando filtros de acessibilidade e segurança.
        """
        # Executa o algoritmo central
        # Nota: Para o MVP, o filtro PCD pode ser expandido aqui futuramente
        caminho, custo = dijkstra(self.graph, start_node, end_node)
        
        return caminho, custo