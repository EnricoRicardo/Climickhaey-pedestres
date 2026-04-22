# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Climickhaey Pedestres |
| Repositório GitHub | |
| Integrante 1 | Enrico Ricardo de Souza Prado — 38071711 |
| Integrante 2 | Gabriel Andrade de Faria — 38095441 |
| Integrante 3 | Gustavo de Faria — 41328779 |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Algoritmo de Dijkstra |
| Categoria | Guloso |
| Complexidade de tempo | O((V+E)logV) com Min-Priority Queue |
| Complexidade de espaço | O(V+E) para a lista de adjacência e vetores de suporte |
| Problema que resolve | Caminho mínimo de fonte única em grafos com pesos não-negativos |

**Por que este algoritmo foi escolhido?**

O Dijkstra é o padrão ouro para sistemas de navegação onde o grafo possui apenas pesos positivos (como distâncias e fatores de risco de 1.0 a 3.0 definidos no E1). Ele garante a solução ótima para encontrar a rota mais segura entre dois pontos de interesse no centro de São Paulo.

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
| Bellman-Ford | Descartado por possuir complexidade $O(V \cdot E)$, superior ao Dijkstra. Como nossa malha urbana não possui pesos negativos, o custo computacional extra não se justifica |

**Limitações no contexto do problema:**

O algoritmo não lida nativamente com restrições dinâmicas de tempo real (como um bloqueio de via repentino) sem que o grafo seja recalculado e a busca reiniciada.

**Referência bibliográfica:**

CORMEN, T. H. et al. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

### 1.2 Algoritmo Adicional

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Busca em Largura (BFS) |
| Categoria | Busca em Grafo |
| Complexidade de tempo | O(V+E) |
| Complexidade de espaço | O(V) |

**Justificativa:**

Será utilizado para validar a conectividade do grafo no momento da importação do dataset, garantindo que o ponto de destino seja alcançável a partir da origem antes de iniciar o processamento pesado do Dijkstra.

**Referência bibliográfica:**

SEDGEWICK, R.; WAYNE, K. Algorithms. 4. ed. Upper Saddle River: Addison-Wesley, 2011.

---

## 2. Arquitetura em Camadas


![Diagrama de arquitetura](./docs/arquitetura_e2.png)

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) | Interface de terminal ou mobile para entrada de origem/destino e exibição da rota. | main.py, cli_handler.py |
| Aplicação (Service) | Orquestração da lógica: recebe coordenadas, chama o algoritmo e aplica o Fator de Risco (FR). | navigation_service.py |
| Domínio (Core) | Implementação das estruturas de Grafo, Vértices e do Algoritmo de Dijkstra. | graph.py, dijkstra.py |
| Infraestrutura (I/O) | Carregamento do dataset (JSON/CSV) e persistência de logs de busca. | file_loader.py, data_parser.py |

---

## 3. Estrutura de Diretórios

```
climickhaey-pedestres/
├── docs/
│   ├── E1_ClimickaeyPedestre_Documento de Visão.md
│   └── E2_ClimickaeyPedestre_Design_Técnico.md
├── src/
│   ├── core/
│   │   ├── graph.py          
│   │   └── node.py
│   ├── algorithms/
│   │   ├── dijkstra.py      
│   │   └── bfs.py
│   ├── io/
│   │   └── loader.py
│   ├── service/
│   │   └── navigation.py
│   └── main.py
├── tests/
│   ├── test_graph.py
│   └── test_algorithms.py
├── data/
│   └── centro_sp.json
└── requirements.txt
```

> **Justificativa de desvios** *(se houver)*: 

---

## 4. Definição do Dataset

**Formato de entrada aceito:**

Arquivo JSON representando uma lista de adjacência ponderada.

**Exemplo de estrutura do arquivo de entrada:**

```json
{
  "vertices": [
    {"id": 1, "nome": "Estação da Luz", "pcd_access": true},
    {"id": 2, "nome": "Rua Mauá", "pcd_access": true}
  ],
  "arestas": [
    { "origem": 1, "destino": 2, "distancia": 150, "seguranca": 2.5 }
  ]
}
```

**Estratégia de geração aleatória:**

| Parâmetro | Descrição |
|-----------|-----------|
| Número de vértices | Quantidade de interseções na malha (ex: 50 a 500). |
| Densidade | Probabilidade de conexão entre esquinas (padrão 0.1 para grafos esparsos). |
| Faixa de pesos | Distância entre 10m e 500m; FR entre 1.0 e 3.0. |

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

| # | Funcionalidade | Prioridade | Critério de aceite |
|---|---------------|------------|-------------------|
| 1 | Importação de Grafo | Alta | Dado um arquivo JSON válido, quando o sistema carregar o arquivo, então a lista de adjacência deve ser populada corretamente em memória. |
| 2 | Cálculo de Rota Segura | Alta | Dado um vértice de origem e um de destino, quando o Dijkstra for executado, então o sistema deve retornar o caminho com o menor somatório de W(e). |
| 3 | Filtro de Acessibilidade | Alta | Dado um usuário PCD, quando uma rota for solicitada, então o sistema deve ignorar arestas marcadas com pcd_access: false. |
| 4 | Gerador de Grafos Aleatórios | Média | Dado o parâmetro de 100 vértices e densidade 0.2, quando acionado, então o sistema gera um grafo conexo para testes. |
| 5 | Exportação de Log de Rota | Baixa | Dado uma rota calculada, quando o processo finalizar, então o sistema deve salvar um arquivo .txt com o passo a passo do trajeto. |

### 5.2 Out-of-Scope — O que NÃO será feito

| Funcionalidade excluída | Motivo |
|------------------------|--------|
| Integração com Google Maps API | Foco acadêmico na implementação manual da lógica de grafos e pesos customizados. |
| Atualização de tráfego em tempo real | Excede o escopo de Teoria dos Grafos, exigindo infraestrutura de streaming de dados. |
| Interface Gráfica (GUI) complexa | O projeto prioriza o motor de cálculo (Back-end) e interface via CLI ou protótipo simples. |

---

## Checklist de Entrega

- [✔] Big-O de tempo e espaço declarados para cada algoritmo
- [✔] Ao menos 1 alternativa descartada com justificativa
- [✔] Diagrama de arquitetura com 4 camadas identificadas
- [✔] Referência bibliográfica para cada algoritmo (ABNT ou IEEE)
- [✔] Backlog com ≥ 5 itens In-Scope e ≥ 3 Out-of-Scope
- [✔] Ao menos 3 critérios de aceite no formato "dado / quando / então"
- [✔] Exemplo de estrutura de arquivo de entrada presente

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
