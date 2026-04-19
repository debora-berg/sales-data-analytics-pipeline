# Sales Data Analytics Pipeline

## Sobre o Projeto

Este projeto tem como objetivo demonstrar um fluxo completo de análise de dados, desde a coleta até a geração de insights de negócio.

Foi desenvolvido um pipeline de dados (ETL) utilizando Python para extração, transformação e armazenamento de dados de vendas, seguido de análises exploratórias e construção de dashboard para suporte à tomada de decisão.

---

## Objetivo

Simular um cenário real de negócio onde dados brutos são transformados em informações estratégicas, permitindo identificar padrões, tendências e oportunidades de melhoria.

---

## Tecnologias Utilizadas

* Python (Pandas, NumPy)
* SQL (SQLite)
* Power BI
* Jupyter Notebook
* Git & GitHub

---

## Pipeline de Dados (ETL)

### Extração

* Leitura de dados de vendas a partir de arquivo CSV
* Tratamento de encoding (latin1)

### Transformação

* Limpeza de dados (remoção de nulos)
* Conversão de datas
* Criação de métricas (Revenue)
* Criação de coluna temporal (Month)

### Carga

* Armazenamento em banco SQLite
* Criação da tabela `sales`

---

## Análises Realizadas

* Faturamento por mês
* Receita por categoria
* Produtos com maior faturamento
* Identificação de padrões e tendências

---

## Insights de Negócio

### Sazonalidade de Vendas

Foi identificado aumento significativo no faturamento nos meses de novembro e dezembro, indicando forte influência de sazonalidade (ex: Black Friday e fim de ano).

**Ação sugerida:**
Aumentar investimentos em marketing e estoque nesses períodos para maximizar receita.

---

### Categoria com Maior Receita

A categoria **Technology** apresenta o maior volume de faturamento.

**Ação sugerida:**
Priorizar estratégias comerciais e expansão de portfólio nessa categoria.

---

### Concentração de Receita

Uma pequena quantidade de produtos representa grande parte do faturamento total.

**Ação sugerida:**

* Monitorar dependência desses produtos
* Avaliar margem de lucro
* Diversificar portfólio

---

## Dashboard

O dashboard está em desenvolvimento e será disponibilizado em breve.

A proposta inclui:
- Faturamento total
- Vendas por mês
- Vendas por categoria
- Top produtos

Enquanto isso, as análises exploratórias podem ser visualizadas no notebook.

---

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/sales-data-analytics-pipeline.git
cd sales-data-analytics-pipeline
```

### 2. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Executar pipeline

```
cd scripts
python main.py
```

### 5. Rodar análises

Abrir o notebook:

```
notebooks/analysis.ipynb
```

---

## Aprendizados

Durante o desenvolvimento deste projeto foram enfrentados desafios reais de dados, como:

* Problemas de encoding (UTF-8 vs latin1)
* Tratamento de tipos incompatíveis (Period → string)
* Ajustes de caminhos relativos no projeto
* Estruturação de pipeline de dados

---

## Próximos Passos

* Adicionar análise de margem de lucro
* Criar dashboard interativo online
* Integrar com banco de dados em nuvem
* Automatizar execução do pipeline

---

## Autora

Débora Berg
 LinkedIn: [www.linkedin.com/in/debora-berg-2301991b7](http://www.linkedin.com/in/debora-berg-2301991b7)
 GitHub: https://github.com/debora-berg

---
