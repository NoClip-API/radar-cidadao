# MVP Sprint 3 - Radar Cidadão

## Objetivo do MVP

- Qual problema resolve? A complexidade dos indicadores políticos e a falta de contexto comparativo. O Sprint 3 foca em consolidar as análises e facilitar a interpretação dos dados.
- Qual hipótese será validada? A de que indicadores comparativos e filtros refinados aumentam a utilidade da plataforma para auditoria cidadã.
- Qual valor será entregue ao usuário final? Refinamentos de UI/UX para acessibilidade, indicadores comparativos e uma estrutura de projeto consolidada.

## Descrição da Solução

Esta etapa foca na consolidação e no refinamento técnico:

- Refinamento da interface (UI/UX) com foco em acessibilidade e navegação fluida.
- Implementação de indicadores comparativos de gastos em relação à média estadual.
- Melhoria no sistema de navegação (Header/Footer) para links consistentes.
- Consolidação do repositório e documentação final para a Feira de Soluções.

## Personas / Usuários-Alvo

Persona 1 & 2: Dona Maria e Carlos Menezes (Refinamento)
- Necessidades/Dores: Precisam de dados contextualizados (médias) e facilidade de navegação para análises rápidas.

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

## User Stories (Backlog do MVP - Sprint 3)

| ID | User Story | Prioridade | Est. | Definition of Ready (DoR) | Definition of Done (DoD) |
|---|---|---|---|---|---|
| US7 | Como professora, quero acessar os dados em meu computador para usar nas aulas. | Média | 8 | Funcionalidade de download de CSV/JSON implementada no backend. | Botão de exportação funcional e arquivo baixado contém os dados filtrados. |
| US8 | Como eleitor, quero filtrar as despesas e votos no perfil para análise específica. | Alta | 5 | Sistema de navegação por abas ou filtros internos no perfil definido. | Filtros aplicados em tempo real na página de detalhamento do deputado. |
| US9 | Como jornalista, quero acesso ao comprovante do gasto para verificar legitimidade. | Baixa | 5 | Link do comprovante (documento) identificado no retorno da API. | Link direto para o PDF/Documento oficial disponível na tabela de gastos. |

## Critérios de Aceitação

- Navegação Refinada: Header e Footer devem estar presentes em todas as páginas com links consistentes.
- Acessibilidade: Uso de cores com contraste adequado e tags semânticas HTML5.

## Métricas de Validação

- Consistência Visual: 100% das páginas devem seguir o mesmo padrão de design e navegação.

## Anexos / Evidências

| Descrição | Link / Anexo |
| --------- | ---------- |
| Repositório GitHub | https://github.com/NoClip-API/radar-cidadao |
| Google Colab | https://colab.research.google.com/drive/1cnfTIuEFLwqLYviIGmjA7siY875VRcC8?usp=sharing |
