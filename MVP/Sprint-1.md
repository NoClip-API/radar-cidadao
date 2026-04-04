# MVP Sprint 1 - Radar Cidadão

## Objetivo do MVP

- Qual problema resolve? Dados sobre parlamentares são técnicos, dispersos e de difícil interpretação para o cidadão comum. O MVP inicia a tradução desses dados em informações claras e neutras.
- Qual hipótese será validada? A de que é possível responder a uma pergunta investigativa clara (ex: gastos vs. presença) utilizando apenas o tratamento de dados da API no Google Colab.
- Qual valor será entregue ao usuário final? Transparência e veracidade na coleta de dados, fornecendo as primeiras visualizações (gráficos) que facilitam a compreensão do desempenho parlamentar.

## Descrição da Solução

Esta etapa foca na exploração, validação da pergunta e infraestrutura básica:

- Consumo da API REST oficial da Câmara via Python.
- Limpeza e tratamento de dados brutos (JSON) no Google Colab para evitar distorções.
- Criação de gráficos exploratórios que interpretem os primeiros resultados.
- Esboço inicial (wireframe) do site.

## Personas / Usuários-Alvo

Persona 1: Dona Maria (Eleitora)
- Descrição: Eleitora que votará em outubro e deseja decidir com consciência se deve reconduzir seu atual deputado ao cargo.
- Necessidades/Dores: Sente falta de uma síntese simples e objetiva sobre a atuação do parlamentar. O MVP atende sua necessidade ao transformar dados complexos em informação compreensível para auxiliar na escolha do seu voto.

Persona 2: Carlos Menezes (Jornalista Local)
- Descrição: Precisa avaliar rapidamente o desempenho de políticos de sua região.
- Necessidades/Dores: Enfrenta dados complexos e espalhados; o MVP resolve isso ao centralizar a coleta via API e permitir a visualização de tendências através de gráficos comparativos iniciais.

## User Stories (Backlog do MVP)

| ID | User Story                                                                                                                            | Prioridade  | Estimativa |
| -- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
|US1 | Como eleitor, quero ver os dados dos deputados a partir dos dados da Câmara para saber como o deputado está.                          | Alta (meta) | 5          |
|US2 |  Como jornalista, quero visualizar gráficos de número de deputados por partido e de gastos para identificar tendências de desempenho. | Alta (meta) | 5          |

## Critérios de Aceitação

Para que o MVP da Sprint 1 seja considerado entregue e validado, ele deve cumprir os seguintes requisitos:
- Conexão com a API: O Notebook deve demonstrar a coleta de dados brutos (JSON) diretamente da API oficial da Câmara.
- Tratamento de Dados: Os dados devem passar por limpeza inicial e normalização (remoção de duplicatas e ajuste de formatos) no Google Colab.
- Pergunta Investigativa: Deve haver uma pergunta clara definida no início do código que oriente toda a análise (ex: "Qual a relação entre gastos e presença?").
- Visualização: Geração de ao menos dois gráficos exploratórios que permitam interpretar os primeiros resultados sobre o desempenho dos deputados.
- Esboço: Um site capaz de renderizar uma página "Home" estática (sem dados dinâmicos ainda).

## Métricas de Validação

Utilizaremos os seguintes indicadores para medir o sucesso desta etapa:
- Integridade dos Dados: 100% das requisições à API devem retornar um JSON válido e processável pelo script Python.
- Cobertura da Pergunta: Os gráficos gerados devem responder diretamente à pergunta investigativa formulada, sem ambiguidades.
- Neutralidade Técnica: Ausência de adjetivos ou juízos de valor nos comentários do código e nas legendas dos gráficos.
- Organização do Código: O repositório deve seguir a estrutura de pastas padrão e conter um README explicativo.

## Próximos Passos

Após a conclusão da Sprint 1, a equipe avançará para a Sprint 2, focando em:
- Integração Real: Migrar a lógica de processamento de dados do Colab para as rotas do site, realizando chamadas em tempo real à API.
- Funcionalidades de Filtro: Implementar a busca por estado e partido para atender à necessidade do Jornalista Carlos.
- Interface para o Cidadão: Criar a síntese objetiva de votações e presença focada na Dona Maria, utilizando HTML5 e CSS3 responsivo.
- Cálculos Comparativos: Desenvolver a lógica para comparar gastos individuais com a média estadual.

## Anexos / Evidências

| Descrição | Link / Anexo |
| --------- | ---------- |
| Google Colab | https://colab.research.google.com/drive/1cnfTIuEFLwqLYviIGmjA7siY875VRcC8?usp=sharing