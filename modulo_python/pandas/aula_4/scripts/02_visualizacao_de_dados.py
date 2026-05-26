# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# # Visualização de dados
# <a name="visualizacao"></a>

# O pandas trabalha bem com bibliotecas como **matplotlib** e **seaborn** para criar gráficos diretamente a partir de DataFrames.

# O jeito mais rápido de visualizar dados é usando `.plot()` direto no resultado de um `groupby`:
#
# ```python
# df.groupby('coluna')['valor'].sum().plot(kind='bar')
# ```
#
# Tipos disponíveis: `'bar'`, `'barh'`, `'line'`, `'pie'`, `'scatter'`, `'hist'`.

# Para ter mais controle sobre o gráfico, usamos o **matplotlib** diretamente:
#
# ```python
# plt.figure(figsize=(10, 6))
# plt.bar(x, y)
# plt.title('Título')
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.xticks(rotation=45)
# plt.show()
# ```

# Para gráficos de **pizza**, usamos `plt.pie()` com rótulos e percentuais:
#
# ```python
# plt.pie(valores, labels=rotulos, autopct='%1.1f%%')
# plt.title('Distribuição')
# plt.show()
# ```

# ## Descoberta guiada
# *Visualização de dados*

negociacao  = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/negociacao.csv')
cliente = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/cliente.csv')
equipe = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/equipe.csv')
pagamento = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/pagamento.csv')
funcionario = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/funcionario.csv')
cargo = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/cargo.csv')
data = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/data.csv')

df_neg = pd.merge(negociacao, cliente, left_on='clientePK', right_on='idCliente', how='left')
df_neg = pd.merge(df_neg, equipe, on='equipePK')
df_neg.head()

# 1. Usando `.plot(kind='barh')`, crie um gráfico de barras com a **soma de receita por setor** (`clienteSetor`).
# 2. Usando `plt.pie()`, crie um gráfico de pizza mostrando a **distribuição de receita por filialCidade**.
# 3. Usando `plt.bar()`, crie um gráfico de barras com a **receita total por equipe** (`filialNome`). Adicione título, xlabel e ylabel.

# 1. Usando `.plot(kind='barh')`, crie um gráfico de barras com a **soma de receita por setor** (`clienteSetor`).

# 2. Usando `plt.pie()`, crie um gráfico de pizza mostrando a **distribuição de receita por filialCidade**.

# 3. Usando `plt.bar()`, crie um gráfico de barras com a **receita total por equipe** (`filialNome`). Adicione título, xlabel e ylabel.

# ## Hands on!
# *Visualização de dados*

# Usando os dados do Data Warehouse, resolva:
#
# 1. Monte o DataFrame de `pagamento` com `cargo` e crie um gráfico de barras com o **salário médio por nível de cargo** (`cargoNivel`). Use `plt.bar()` com título e rótulos nos eixos.
# 2. Crie um gráfico de pizza mostrando a **quantidade de funcionários por sexo** (`funcSexo`) a partir da tabela `funcionario`.
# 3. Crie um gráfico de barras horizontais (`plt.barh()`) com os **top 5 clientes por receita total**. Dica: use `.sort_values().tail(5)`.

# 1.  Monte o DataFrame de `pagamento` com `cargo` e crie um gráfico de barras
# com o **salário médio por nível de cargo** (`cargoNivel`).
# Use `plt.bar()` com título e rótulos nos eixos.

# 2. Crie um gráfico de pizza mostrando a **quantidade de funcionários por sexo** (`funcSexo`) a partir da tabela `funcionario`.

# 3. Gráfico de barras horizontais — top 5 clientes por receita total
