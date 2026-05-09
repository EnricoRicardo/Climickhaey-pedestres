from src.io.loader import load_graph_from_json
from src.service.navigation import NavigationService

def run():
    print("\n" + "="*50)
    print("      CLIMICKHAEY: NAVEGAÇÃO URBANA SEGURA")
    print("="*50)
    
    try:
        # 1. Carrega o dataset
        grafo = load_graph_from_json('data/centro_sp.json')
        service = NavigationService(grafo)
        
        # 2. Interface de entrada dinâmica
        print("\n[ Configurações de Rota ]")
        origem = int(input("Digite o ID do Ponto de Origem (Ex: 1): "))
        destino = int(input("Digite o ID do Ponto de Destino (Ex: 2): "))
        
        # Filtro PCD: Resolve o alerta de maturidade do E2
        pcd_opcao = input("Deseja apenas rotas com acessibilidade PCD? (s/n): ").lower()
        usar_pcd = True if pcd_opcao == 's' else False
        
        print("\nCalculando a rota mais segura...")
        
        # 3. Execução via Service
        caminho, custo = service.calculate_route(origem, destino, pcd_filter=usar_pcd)
        
        # 4. Exibição dos resultados
        print("\n" + "-"*30)
        if caminho:
            print(f"✅ ROTA ENCONTRADA: {caminho}")
            print(f"📊 CUSTO PONDERADO (Distância x Risco): {custo:.2f}")
            if usar_pcd:
                print("♿ FILTRO ATIVO: Rota validada para acessibilidade.")
        else:
            print("❌ Não foi possível encontrar uma rota segura com esses critérios.")
        print("-"*30)
            
    except FileNotFoundError:
        print("\n[ERRO]: O arquivo 'data/centro_sp.json' não foi encontrado.")
    except ValueError:
        print("\n[ERRO]: Por favor, digite apenas números para os IDs dos pontos.")
    except Exception as e:
        print(f"\n[ERRO INESPERADO]: {e}")

if __name__ == "__main__":
    run()