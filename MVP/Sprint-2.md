# MVP Sprint 2 - Radar Cidadão

## Objetivo do MVP

- Qual problema resolve? A transição de dados brutos e análises isoladas para uma plataforma web interativa, facilitando o acesso à informação através de busca visual e filtros regionais.
- Qual hipótese será validada? A de que uma interface web com busca por fotos e filtros por partido/estado aumenta o engajamento do cidadão na fiscalização parlamentar.
- Qual valor será entregue ao usuário final? Facilidade na localização de deputados específicos e contextualização de seus gastos em relação à média de seus pares.

## Descrição da Solução

Esta etapa foca na integração da lógica de dados ao ambiente web e na melhoria da experiência de busca:

- Migração do processamento de dados do Google Colab para o backend em Flask.
- Implementação de galeria de deputados com fotos para facilitar a identificação visual.
- Desenvolvimento de sistema de filtros dinâmicos por estado (UF) e partido político.
- Criação de síntese objetiva de participação em votações e presença em plenário.
- Lógica de cálculo comparativo de gastos individuais versus média estadual.

## Personas / Usuários-Alvo

Persona 1: Dona Maria (Eleitora)
- Descrição: Eleitora que votará em outubro e deseja decidir com consciência se deve reconduzir seu atual deputado ao cargo.
- Necessidades/Dores: Quer encontrar rapidamente o deputado e ver se ele compareceu às votações importantes. A Sprint 2 entrega a busca por foto e a síntese de votações.

Persona 2: Carlos Menezes (Jornalista Local)
- Descrição: Precisa avaliar rapidamente o desempenho de políticos de sua região.
- Necessidades/Dores: Precisa comparar o custo de um deputado com a média regional. A Sprint 2 resolve isso com os cálculos comparativos e filtros por estado.

## Definition of Ready (DoR)

Para que uma User Story seja considerada pronta para a Sprint, ela deve:
- **Formato Padrão:** Seguir a estrutura "Como [persona], eu quero [funcionalidade], para que [valor de negócio]".
- **Critérios de Aceitação:** Possuir no mínimo 3 critérios de aceitação claros e testáveis.
- **Mapeamento de Dados:** Identificar os endpoints específicos da API da Câmara (JSON) que serão consumidos.
- **Rigor Metodológico:** Definir a fórmula matemática ou lógica de tratamento para evitar viés político.
- **Esforço Estimado:** Ter sido pontuada pela equipe utilizando Planning Poker.
- **Dependências:** Estar com o ambiente de desenvolvimento (Google Colab/Python) configurado.

## Definition of Done (DoD)

Para que uma entrega seja considerada finalizada, ela deve:
- **Funcionalidade:** Atender integralmente a todos os critérios de aceitação.
- **Qualidade de Código:** Passar por revisão de pares (Code Review) focada em legibilidade e eficiência.
- **Neutralidade Técnica:** Não conter adjetivos ou opiniões pessoais nos logs, comentários ou saída de dados.
- **Documentação:** Possuir docstrings em todas as funções de tratamento de dados.
- **Controle de Versão:** Código commitado, com mensagem clara, e aprovado em Pull Request no GitHub.
- **Validação do PO:** Ser apresentada e validada pelo Product Owner quanto ao valor entregue.

## User Stories (Backlog do MVP - Sprint 2)

| ID | User Story | Prioridade | Est. | Definition of Ready (DoR) | Definition of Done (DoD) |
|---|---|---|---|---|---|
| US3 | Como eleitor, quero uma lista com as fotos dos deputados para facilitar a busca visual. | Alta | 8 | URL das imagens mapeada no JSON; Template HTML da galeria pronto. | Fotos exibidas corretamente na galeria com fallback para imagens ausentes. |
| US4 | Como eleitor, quero uma síntese objetiva da participação em votações. | Alta | 5 | Acesso ao endpoint `/votacoes`; Lógica de contagem de presença definida. | Resumo visual de presença e votos exibido na página do deputado. |
| US5 | Como eleitor, quero filtrar deputados por estado ou partido. | Alta | 3 | Lógica de filtragem em Python/Flask testada; Inputs do formulário definidos. | Filtros dinâmicos funcionando e atualizando a galeria em tempo real. |
| US6 | Como jornalista, quero comparar a média de gastos do deputado com a média estadual. | Média | 8 | Base de dados de gastos de todos os deputados processada; Fórmula de média pronta. | Gráfico comparativo exibindo gasto individual vs média do estado. |

## Critérios de Aceitação

Para que o MVP da Sprint 2 seja considerado entregue e validado, ele deve cumprir os seguintes requisitos:
- Galeria Visual: O site deve exibir uma lista de deputados contendo nome, partido, UF e foto oficial.
- Filtragem Funcional: Deve ser possível filtrar a lista de deputados por Estado e por Partido simultaneamente ou de forma isolada.
- Detalhamento de Votações: A página individual do deputado deve apresentar um resumo quantitativo e qualitativo de sua presença e votos.
- Comparativo de Gastos: Exibição clara (preferencialmente gráfica) da relação entre os gastos do deputado e a média de gastos dos deputados do mesmo estado.
- Backend Integrado: As rotas do Flask devem processar os dados da API (ou cache local) em tempo real sem depender de execução manual de notebooks.

## Métricas de Validação

Utilizaremos os seguintes indicadores para medir o sucesso desta etapa:
- Eficácia da Busca: O usuário deve ser capaz de localizar um deputado específico em menos de 3 cliques a partir da home.
- Integridade Comparativa: Os cálculos de média estadual devem ser validados contra a base de dados completa para garantir precisão.
- Responsividade: A interface de filtros e a galeria de fotos devem funcionar corretamente em dispositivos móveis.

## Próximos Passos

Após a conclusão da Sprint 2, a equipe avançará para a Sprint 3, focando em:
- Foco Educacional: Implementar funcionalidades específicas para a Professora, com dados organizados para uso em sala de aula.
- Rigor Metodológico: Redigir e publicar a explicação detalhada de como os indicadores e médias foram calculados.
- Refinamento de UI/UX: Melhorar a tipografia e iconografia para acessibilidade e clareza técnica.
- Consolidação do Repositório: Organização final do código, documentação de execução e preparação para a Feira de Soluções.

## Anexos / Evidências

| Descrição | Link / Anexo |
| --------- | ---------- |
| Repositório GitHub | https://github.com/NoClip-API/radar-cidadao |
| Google Colab | https://colab.research.google.com/drive/1cnfTIuEFLwqLYviIGmjA7siY875VRcC8?usp=sharing |
