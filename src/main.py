from src.io.loader import load_graph_from_json
from src.algorithms.dijkstra import dijkstra

def run():
    print("--- Climickhaey Pedestres: Navegação Segura ---")
    try:
        # Carrega o dataset da pasta data/
        grafo = load_graph_from_json('data/centro_sp.json')
        
        # Exemplo de busca: Estação da Luz (1) para SESC 24 de Maio (2)
        origem, destino = 1, 2
        
        caminho, custo = dijkstra(grafo, origem, destino)
        
        if caminho:
            print(f"Melhor rota encontrada: {caminho}")
            print(f"Custo total ponderado (Segurança): {custo}")
        else:
            print("Não foi possível encontrar uma rota segura entre esses pontos.")
            
    except FileNotFoundError:
        print("Erro: O arquivo 'data/centro_sp.json' não foi encontrado.")

if __name__ == "__main__":
    run()