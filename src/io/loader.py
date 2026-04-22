import json

def load_graph_from_json(file_path):
    from src.core.graph import Graph # Import local para evitar circularidade
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    g = Graph()
    for node in data['vertices']:
        g.add_node(node['id'], node)
    
    for edge in data['arestas']:
        # Carrega os dados mapeados no seu E1
        g.add_edge(edge['origem'], edge['destino'], edge['distancia'], edge['seguranca'])
    
    return g