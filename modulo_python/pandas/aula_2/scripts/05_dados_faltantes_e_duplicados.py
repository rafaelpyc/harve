# -*- coding: utf-8 -*-

import pandas as pd

# # Dados faltantes e duplicados
#
# Antes de analisar os dados, precisamos verificar se existem valores faltantes ou registros duplicados.
#
# Para identificar valores nulos:
#
# ```python
# df.isnull()
#
# Para contar valores nulos por coluna:
# ```
# df.isnull().sum()
# ```
#
# Para preencher valores nulos vom um determinado `valor`:
# ```
# df['coluna'].fillna(valor)
# ```
#
# Para remover linhas com valores nulos:
# ```
# df.dropna()
# ```
#
# Para remover linhas com valores nulos em um determinado subconjunto use `subset`:
# ```
# df.dropna(subset=['Idade', 'Cabine'])
# ```
#
# Para verificar valores únicos de uma coluna:
# ```
# df['coluna'].unique()
# ```
#
# Para verificar linhas duplicadas:
# ```
# df.duplicated()
# ```
#
# Para remover duplicatas:
# ```
# df.drop_duplicates()
# ```
#
# ## Descoberta guiada
# Dados faltantes e duplicados
#
# Usando o dataset do Titanic, responda:
#
# 1. Verifique quais colunas possuem valores nulos.
# 2. Quantos valores nulos existem na coluna `Idade`?
# 3. Quais são os valores únicos da coluna `Local de embarque`?
# 4. Verifique se existem linhas duplicadas no DataFrame.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Verifique quais colunas possuem valores nulos.

# 2. Quantos valores nulos existem na coluna `Idade`?

# 3. Quais são os valores únicos da coluna `Local de embarque`?

# 4. Verifique se existem linhas duplicadas no DataFrame.

# ## Hands on!
# Dados faltantes e duplicados
#
# Ainda sobre o dataset do Titanic:
#
# 1. Apague os registros de passageiros sem local de embarque definido.
# 2. Substitua os valores nulos de `Cabine` por `C9999`
# 3. Substitua os valores de `Local de embarque`: `S` por `Southampton`, `C` por `Cherbourg` e `Q` por `Queenstown` e verifique novamente quantas vezes cada valor aparece.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Apague os registros de passageiros sem local de embarque definido.

# 2. Substitua os valores nulos de `Cabine` por `C9999`

# 3. Substitua os valores de `Local de embarque`:
# `S` por `Southampton`
# `C` por `Cherbourg`
# `Q` por `Queenstown`
#  e verifique novamente quantas vezes cada valor aparece.
