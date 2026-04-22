class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.nodes_data = {}

    def add_node(self, node_id, data=None):
        self.adjacency_list[node_id] = []
        self.nodes_data[node_id] = data

    def add_edge(self, source, target, distance, risk_factor):
        # Implementação da Função de Peso do E1: W = Distância * FR
        weight = distance * risk_factor
        self.adjacency_list[source].append({
            "target": target,
            "weight": weight,
            "distance": distance,
            "risk_factor": risk_factor
        })