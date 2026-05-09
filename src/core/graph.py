class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.nodes_data = {}

    def add_node(self, node_id, data=None):
        """Adiciona um vértice ao grafo com metadados opcionais."""
        self.adjacency_list[node_id] = []
        self.nodes_data[node_id] = data

    def add_edge(self, source, target, distance, risk_factor, pcd_accessible=True):
        """
        Adiciona uma aresta ponderada.
        W(e) = distância * fator_segurança
        """
        # Cálculo explícito da função de custo conforme solicitado no feedback E2
        weight = distance * risk_factor
        
        self.adjacency_list[source].append({
            "target": target,
            "weight": weight,
            "distance": distance,
            "risk_factor": risk_factor,
            "pcd": pcd_accessible  # Atributo avançado elogiado no parecer
        })

    def get_neighbors(self, node_id, pcd_filter=False):
        """
        Retorna vizinhos, permitindo filtrar arestas não acessíveis se necessário.
        """
        neighbors = self.adjacency_list.get(node_id, [])
        if pcd_filter:
            # Implementação do Alerta PCD: remove arestas inacessíveis
            return [n for n in neighbors if n['pcd']]
        return neighbors