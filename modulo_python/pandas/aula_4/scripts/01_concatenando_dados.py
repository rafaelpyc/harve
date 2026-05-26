# -*- coding: utf-8 -*-

import pandas as pd

# # Concatenando dados
# <a name="merge"></a>

# O merge funciona como o **JOIN do SQL**: ele conecta duas tabelas usando uma **coluna em comum** (a chave).

# Quando as colunas-chave possuem o **mesmo nome** nas duas tabelas, usamos o parâmetro `on`:
#
# ```python
# pd.merge(df_esquerda, df_direita, on='coluna_chave')
# ```

# Quando as colunas-chave possuem **nomes diferentes**, usamos `left_on` e `right_on`:
#
# ```python
# pd.merge(df_esquerda, df_direita, left_on='clientePK', right_on='idCliente')
# ```

# O parâmetro `how` define **quais registros** aparecem no resultado:
#
# * `inner` (padrão) — apenas as linhas que existem em **ambas** as tabelas
# * `left` — todas as linhas da tabela da **esquerda** (NaN onde não houver correspondência)
# * `right` — todas as linhas da tabela da **direita**
# * `outer` — **todas** as linhas de ambas as tabelas

# Quando ambas as tabelas possuem colunas com o **mesmo nome** (além da chave), o Pandas adiciona sufixos `_x` e `_y`. Para controlar isso, usamos `suffixes`:
#
# ```python
# pd.merge(df1, df2, on='equipePK', suffixes=('_func', '_equipe'))
# ```

# ## Descoberta guiada
# *Concatenando dados*

# Vamos carregar os dados de um Data Warehouse e praticar merges entre tabelas fato e dimensão.
#
# **Atenção:** os nomes das colunas-chave nem sempre são iguais entre as tabelas!

negociacao  = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/negociacao.csv')
cliente = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/cliente.csv')
equipe = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/equipe.csv')
pagamento = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/pagamento.csv')
funcionario = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/funcionario.csv')
cargo = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/cargo.csv')
data = pd.read_csv('https://raw.githubusercontent.com/rafaelpyc/harve/main/modulo_python/pandas/aula_4/data/data.csv')

# Antes de fazer merge, sempre **observe as colunas** de cada tabela:

print(negociacao.head())

print(cliente.head())

print(equipe.head())

# 1. Faça o merge de `negociacao` com `cliente`. Cuidado: as colunas-chave têm **nomes diferentes**!
# 2. Faça o merge de `negociacao` com `equipe`. Aqui a chave tem o **mesmo nome**.
# 3. Faça o merge de `pagamento` com `cargo` usando a chave `cargoPK`. Compare o resultado usando `how='inner'` e `how='left'`. Qual a diferença na quantidade de linhas?

# 1. Merge de negociacao com cliente (nomes diferentes!)

# 2. Merge de negociacao com equipe (mesmo nome)

# 3a. Merge de pagamento com cargo - inner (padrão)

# 3b. Merge de pagamento com cargo - left

# ## Hands on!
# *Concatenando dados*

# Usando os dados do Data Warehouse, resolva:
#
# 1. Faça o merge de `pagamento` com `funcionario` e depois com `equipe`. Atenção: as tabelas `funcionario` e `equipe` possuem uma coluna chamada `nome` — use o parâmetro `suffixes` para diferenciá-las.
# 2. A partir do DataFrame montado no exercício anterior, qual é o **salário médio** por `funcEstadoSigla`?

# 1. Merge de pagamento com funcionario e depois equipe (cuidado com suffixes!)

# 2. Salário médio por funcEstadoSigla
