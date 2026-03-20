\# 📊 Agrofit Data Pipeline \& BI Analysis



\## 🧠 Sobre o Projeto



Este projeto tem como objetivo a construção de um pipeline completo de dados e um modelo analítico para exploração de informações sobre produtos de defensivos agrícolas disponibilizados pela base pública do Agrofit.



A solução contempla desde a ingestão e tratamento dos dados até a modelagem dimensional e criação de dashboards analíticos no Power BI, permitindo a geração de insights estratégicos sobre o mercado.



\---



\## 🎯 Objetivos



\* Tratar dados brutos com problemas de codificação e normalização

\* Estruturar um pipeline de dados reutilizável

\* Modelar os dados em formato estrela (Star Schema)

\* Criar análises e dashboards com foco em negócio

\* Extrair insights sobre o mercado de defensivos agrícolas



\---



\## ⚙️ Tecnologias Utilizadas



\* Python

\* Pandas

\* Power BI

\* Modelagem Dimensional

\* ETL (Extract, Transform, Load)



\---



\## 🏗️ Estrutura do Projeto



```

agrofit-case/

│

├── data/

│   ├── raw/                # Dados brutos (CSV original)

│   └── processed/          # Dados tratados (saída do pipeline)

│

├── src/

│   ├── ingestao.py         # Leitura dos dados

│   ├── limpeza.py          # Tratamento e padronização

│   └── transformacao.py    # Normalização e modelagem

│

├── notebooks/              # Explorações (opcional)

├── main.py                 # Pipeline principal

└── README.md               # Documentação do projeto

```



\---



\## 🔄 Pipeline de Dados



O pipeline foi estruturado nas seguintes etapas:



\### 1. Ingestão



\* Leitura de arquivos CSV

\* Tratamento de encoding



\### 2. Limpeza



\* Padronização de nomes de colunas

\* Correção de caracteres especiais

\* Tratamento de valores nulos



\### 3. Transformação



\* Normalização de colunas multivaloradas

\* Separação em entidades (dimensões)

\* Criação de tabelas de relacionamento (bridges)



\### 4. Modelagem



\* Construção de tabela fato

\* Criação de dimensões

\* Estruturação em modelo estrela



\### 5. Exportação



\* Geração de arquivos CSV tratados para consumo analítico



\---



\## 🧩 Modelagem de Dados



O modelo segue o padrão \*\*Star Schema\*\*, com suporte a relações muitos-para-muitos.



\### 🔷 Tabela Fato



\* `fato\_produto`



\### 🟨 Dimensões



\* `dim\_empresa`

\* `dim\_cultura`

\* `dim\_ingrediente`

\* `dim\_praga`

\* `dim\_praga\_nome`



\### 🟩 Tabelas de Relacionamento (Bridge)



\* `bridge\_produto\_cultura`

\* `bridge\_produto\_ingrediente`

\* `bridge\_produto\_praga`



\---



\## 🔗 Relacionamentos



\* Modelo baseado em \*\*fato → bridge → dimensão\*\*

\* Uso de cardinalidade muitos-para-muitos

\* Direção de filtro ajustada para garantir propagação correta



\---



\## 📊 Dashboard (Power BI)



O dashboard foi estruturado em três níveis analíticos:



\### 1. Visão Geral



\* KPIs principais (produtos, empresas, culturas)

\* Distribuição por classe e risco

\* Top empresas



\### 2. Análise Técnica



\* Relação Cultura × Praga

\* Ingredientes mais utilizados

\* Distribuição de soluções por cultura



\### 3. Deep Dive (Aprofundamento)



\* Complexidade dos produtos

\* Versatilidade (multi-cultura e multi-praga)

\* Estratégias de atuação das empresas



\---



\## 💡 Principais Insights



\* Mercado com alta diversidade, porém concentrado em grandes players

\* Predominância de herbicidas, fungicidas e inseticidas

\* Culturas como soja, milho e café concentram maior volume de soluções

\* Existência de produtos com alta versatilidade (atuam em múltiplos cenários)

\* Empresas adotam estratégias distintas: especialização vs diversificação



\---



\## ▶️ Como Executar



\### 1. Criar ambiente virtual



```bash

python -m venv venv

```



\### 2. Ativar ambiente



```bash

venv\\Scripts\\activate

```



\### 3. Instalar dependências



```bash

pip install pandas

```



\### 4. Executar pipeline



```bash

python main.py

```



\### 5. Saída



Os arquivos tratados serão gerados em:



```

data/processed/

```



\---



\## 📌 Decisões Técnicas



\* Uso de funções genéricas para colunas simples e específicas para regras de negócio

\* Modelagem com tabelas bridge para suportar relações muitos-para-muitos

\* Padronização de tipos de dados para garantir integridade relacional

\* Separação clara entre dados de negócio e chaves técnicas



\---



\## 🚀 Possíveis Melhorias



\* Automatização com pipeline orquestrado (Airflow)

\* Persistência em banco de dados (PostgreSQL)

\* Criação de API para consumo dos dados

\* Incremento de métricas analíticas



\---



\## 👤 Autor



Projeto desenvolvido por \*\*Gelson Moraes\*\* como parte de processo seletivo para a vaga de Analista de Dados.



\---



\## 📎 Observação Final



Este projeto demonstra a aplicação prática de conceitos de engenharia de dados e BI, incluindo tratamento de dados reais, modelagem dimensional e geração de insights orientados a negócio.



# analise_agrofit
