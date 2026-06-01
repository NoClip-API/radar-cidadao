# Guia de Instalação - Radar Cidadão

Este guia descreve os passos necessários para configurar o ambiente de desenvolvimento e executar o projeto **Radar Cidadão** em sua máquina local.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.8 ou superior**
- **Git** (para clonar o repositório)

---

## 1. Clonar o Repositório

Abra o terminal e execute o comando abaixo para clonar o projeto:

```bash
git clone https://github.com/NoClip-API/radar-cidadao.git
cd radar-cidadao
```

## 2. Configurar o Ambiente Virtual (Recomendado)

É recomendável utilizar um ambiente virtual para isolar as dependências do projeto:

### No Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### No Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes necessários listados no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

As principais bibliotecas instaladas serão:
- **Flask**: Framework web para o backend.
- **Requests**: Para consumo da API da Câmara dos Deputados.
- **Plotly**: Para geração dos gráficos interativos.
- **Python-dotenv**: Para gerenciamento de variáveis de ambiente (caso necessário).

## 4. Executar a Aplicação

Para iniciar o servidor de desenvolvimento, navegue até a pasta `src` e execute o arquivo `app.py`:

```bash
cd src
python app.py
```

Após executar o comando, você verá uma mensagem indicando que o servidor está rodando. O endereço padrão costuma ser:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Abra este link em seu navegador para acessar o Radar Cidadão.

---

## Solução de Problemas Comuns

- **Erro de Módulo não Encontrado:** Certifique-se de que o ambiente virtual está ativado e que o comando `pip install` foi executado com sucesso.
- **Porta 5000 em Uso:** Caso a porta 5000 já esteja sendo usada por outro processo, o Flask pode falhar ao iniciar. Você pode alterar a porta no arquivo `app.py` ou encerrar o processo que está utilizando a porta atual.
- **Conexão com a API:** O projeto depende de acesso à internet para realizar requisições à API de Dados Abertos da Câmara. Verifique sua conexão caso os dados dos deputados não carreguem.
