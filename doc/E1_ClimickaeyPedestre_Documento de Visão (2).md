# E1 — Proposta e Definição do Projeto

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 19 de março de 2026  
> **Peso:** 10% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Climickhaey Pedestres |
| Integrante 1 | Enrico Ricardo de Souza Prado — 38071711 |
| Integrante 2 | Gabriel Andrade de Faria — 38095441 |
| Integrante 3 | Gustavo de Faria — 41328779 |
| Domínio de aplicação | Redes de Rotas para Pedestres |

---

## 1. Contexto e Motivação

Sistemas de navegação atuais priorizam o fluxo de veículos, negligenciando as particularidades do pedestre. Em São Paulo, o deslocamento a pé é condicionado por uma análise multicritério de infraestrutura e segurança. Segundo o Relatório Anual de Sinistros de Trânsito (CET/2024), a cidade registra mais de 30 mil sinistros com pedestres, evidenciando a vulnerabilidade deste público.

A motivação do projeto é mitigar as falhas de algoritmos que ignoram barreiras arquitetónicas e zonas de risco. Conforme o Anuário Brasileiro de Segurança Pública (2025), a via pública concentra 70% dos casos de violência, onde a falta de infraestrutura básica facilita crimes de oportunidade — em São Paulo, a taxa de furtos e roubos de celulares chega a 1.425,4 por 100 mil habitantes.

O foco será atender pessoas com mobilidade reduzida (PCD) na região central de São Paulo, onde a ausência de acessibilidade força desvios perigosos. O sistema utiliza a Teoria dos Grafos com pesos dinâmicos para processar rotas que equilibrem eficiência, acessibilidade universal e segurança, transformando estatísticas oficiais em trajetos seguros.

---

## 2. Objetivo Geral

Desenvolver um sistema de navegação urbana para pedestres fundamentado em Teoria dos Grafos, capaz de calcular rotas otimizadas que integrem distância métrica e segurança viária/pessoal, utilizando algoritmos de caminho mínimo ponderado para mitigar a exposição do usuário a zonas de risco.

---

## 3. Objetivos Específicos

- [ **Modelagem de Rede Urbana:** Representar um recorte do centro de São Paulo como um grafo esparso, mapeando calçadas e travessias. ] 
- [ **Formalização da Função de Custo:** Implementar uma métrica de peso que combine distância física e um fator de risco ambiental baseado em dados oficiais de segurança. ] 
- [ **Implementação de Algoritmo de Busca:** Aplicar o algoritmo de Dijkstra para encontrar o caminho de menor custo total (distância ponderada pelo risco) entre dois pontos. ] 
- [ **Simulação de Restrições de Acessibilidade:** Mapear pontos de interesse e barreiras físicas como atributos de vértices, influenciando o cálculo das arestas adjacentes. ]
---

## 4. Público-Alvo / Caso de Uso Principal

O foco principal do sistema são pessoas com mobilidade reduzida (PCD) e pedestres que circulam em áreas de alto fluxo.

Caso de Uso: Um usuário precisa se deslocar entre a Estação da Luz e o SESC 24 de Maio. O sistema identifica que a rota mais curta possui trechos com baixa iluminação e altos índices de furtos. O algoritmo, então, sugere uma rota alternativa que, embora 50 metros mais longa, possui um "peso de segurança" menor, mantendo o usuário em vias monitoradas e acessíveis.

---

## 5. Justificativa Técnica — Por que Grafos?

A modelagem por grafos é superior a buscas em grids por sua flexibilidade topológica, permitindo representar a malha urbana como uma estrutura esparsa. Isso otimiza o processamento, focando apenas em conexões reais de caminhada. O diferencial técnico reside na Função de Peso Formal, que retira o projeto da abstração:
            $$W(e) = \text{Distância (m)} \times FR$$


Onde o Fator de Risco ($FR$) é um multiplicador escalar binário ou graduado ($1.0$ a $3.0$):
1.0 (Seguro): Via bem iluminada/baixo índice criminal.
3.0 (Risco Alto): Via com histórico de sinistros ou interrupções físicas (obras/barreiras).

---

## 6. Tipo de Grafo

| Característica | Escolha | Justificativa breve |
|----------------|---------|---------------------|
| Dirigido ou não-dirigido | Dirigido | Modela restrições de fluxo, como escadarias (apenas descida para PCD) e rampas de sentido único. |
| Ponderado ou não-ponderado | Ponderado | Necessário para a função de custo que integra distância e índices de segurança/acessibilidade. |
| Conectado / bipartido / geral | Conectado | GGarante a existência de caminhos; bloqueios temporários são simulados com peso infinito. |
| Representação interna pretendida | Lista de adjacência | Mais eficiente para grafos urbanos (esparsos), otimizando memória e busca. |

---

## 7. Diagrama Conceitual  



**Legenda:** 

- **Vértices (1-9):** Representam os pontos de interesse (POIs) e as interseções da malha urbana.
- **Arestas Dirigidas (Setas):** Indicam as conexões de caminhada disponíveis. A orientação das setas garante o cumprimento de restrições de fluxo (ex: escadarias ou rampas de sentido único).
- **Pesos Multicritério ($W$):** Cada aresta possui um custo calculado pela função formal $W(e) = \text{Distância (M)} \times \text{Fator de Risco (FR)}$.

        D: Distância física real em metros.
        FR: Multiplicador de risco (1.0 a 3.0), baseado em índices de iluminação e criminalidade.

- **Caminho Verde (Rota Otimizada):** Representa o trajeto calculado pelo algoritmo de Dijkstra para o perfil do usuário. Embora possua mais vértices intermediários, o custo acumulado ponderado é o menor da rede ($\sum W = 70$), priorizando a segurança.
- **Caminho Vermelho (Rota Evitada):** Rota que, apesar de parecer direta, é descartada pelo sistema devido ao alto custo acumulado ($\sum W = 320$), gerado por fatores de risco elevados nas vias (FR: 2.0 e 3.0).

---

## Checklist de Entrega

Antes de submeter, confirme:

- [✔] Texto entre 300 e 600 palavras (seções 1 a 5)
- [✔] Todos os campos da tabela de identificação preenchidos
- [✔] Tipo de grafo especificado com justificativa
- [✔] Diagrama presente e referenciado no texto
- [✔] Arquivo nomeado como `E1_NomeGrupo_Grafos.docx` (versão Word) ou PR aberto (versão GitHub)

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
