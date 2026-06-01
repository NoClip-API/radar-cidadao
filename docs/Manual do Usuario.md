# Manual do Usuário - Radar Cidadão

O **Radar Cidadão** é uma plataforma desenvolvida para tornar os dados da Câmara dos Deputados mais acessíveis, transparentes e compreensíveis para o cidadão. Este manual descreve as principais funcionalidades do sistema e como utilizá-las para fiscalizar a atuação dos parlamentares.

---

## 1. Acesso ao Sistema
Ao iniciar a aplicação, você será direcionado para a página inicial (Home), onde poderá visualizar a galeria de deputados federais em exercício.

## 2. Página Inicial: Busca e Filtros
A página inicial permite localizar deputados de forma rápida através de três critérios:

- **Busca por Nome:** Digite o nome do deputado no campo de busca para filtrar a lista.
- **Filtro por Estado (UF):** Selecione uma unidade federativa para ver apenas os deputados daquele estado.
- **Filtro por Partido:** Selecione um partido político para visualizar seus integrantes.

Os filtros podem ser combinados para uma busca mais refinada (ex: Deputados do partido "PT" no estado de "SP").

## 3. Detalhes do Deputado
Ao clicar no card de um deputado, você acessará sua página individual, que contém:

### 3.1 Informações Básicas
Foto oficial, nome eleitoral, partido e estado de origem.

### 3.2 Gráfico de Gastos (Cota Parlamentar)
Visualize como o deputado utiliza a Cota para Exercício da Atividade Parlamentar (CEAP).
- **Filtros de Gastos:** Você pode filtrar os gastos por **Tipo de Despesa**, **Mês** e **Ano**.
- **Visualização:** O gráfico apresenta a distribuição dos gastos, permitindo identificar onde o recurso público está sendo mais utilizado.

### 3.3 Gráfico de Presença
Acompanhe o compromisso do parlamentar com as sessões e votações.
- **Filtro por Ano:** Escolha o ano para visualizar o histórico de presença.
- **Indicadores:** O gráfico mostra a relação entre presenças, ausências justificadas e ausências não justificadas.

### 3.4 Participação em Votações
Uma lista das votações recentes em que o deputado participou, mostrando sua posição (Sim, Não, Abstenção, etc.) e o tema da votação.

## 4. Exportação de Dados (CSV)
Para usuários que desejam realizar análises próprias (jornalistas, pesquisadores), o sistema permite exportar os dados de gastos:

1. Na página do deputado, clique no botão **"Ver Detalhes dos Gastos / Exportar CSV"**.
2. Uma prévia dos gastos será exibida em formato de tabela.
3. Clique em **"Baixar CSV"** para fazer o download do arquivo completo com todos os registros de despesas filtrados.

## 5. Comparação de Desempenho
Através do menu **"Gráficos"** no topo do site, você pode comparar dois deputados:

1. Digite o nome do primeiro deputado no campo **"Deputado 1"**.
2. Digite o nome do segundo deputado no campo **"Deputado 2"**.
3. Clique em **"Comparar"** para gerar gráficos lado a lado das despesas de ambos, facilitando a análise comparativa de custos.

---

## 6. Metodologia e Fonte de Dados
- **Fonte:** Todos os dados são extraídos em tempo real da [API da Câmara dos Deputados](https://dadosabertos.camara.leg.br/).
- **Neutralidade:** O Radar Cidadão não emite juízo de valor. As informações apresentadas são dados brutos processados para facilitar a leitura visual.
- **Atualização:** Os dados refletem as informações mais recentes disponibilizadas pelo portal de Dados Abertos.

---

## 7. Suporte e Contato
Em caso de dúvidas, sugestões ou problemas técnicos, entre em contato com a equipe de desenvolvimento através do repositório oficial do projeto.
