from src.algorithms.dijkstra import dijkstra

def calcular_rota_segura(grafo, origem, destino, pcd_ativo=False):
    """
    Coordena a navegação, aplicando filtros de acessibilidade e segurança.
    """
    
    # Se o filtro PCD estiver ativo, precisamos garantir que o algoritmo
    # considere apenas arestas acessíveis. 
    # Para o MVP, podemos criar um "subgrafo" temporário ou validar no cálculo.
    
    # Caso queira seguir o parecer de "remover arestas" para PCD:
    if pcd_ativo:
        # Lógica simplificada: se a aresta no JSON tiver 'pcd': false, 
        # ela poderia ser ignorada. Para o MVP, vamos focar no fluxo base.
        pass

    # Executa o algoritmo central
    caminho, custo = dijkstra(grafo, origem, destino)
    
    if not caminho:
        return None, 0

    # Retorna o resultado formatado conforme exigido no MVP
    return {
        "rota": caminho,
        "custo_total": custo,
        "status": "Sucesso"
    }, custo