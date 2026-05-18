# -*- coding: utf-8 -*-

import pandas as pd

# #Inspeção de conteúdo
#
# Nesta etapa, vamos aprender algumas formas simples de inspecionar o conteúdo de um DataFrame.
#
# A função `describe()` retorna estatísticas descritivas das colunas numéricas, como média, valor mínimo, valor máximo e quartis.
#
#
# ```python
# df.describe()
# ```
#
# A função `value_counts` quando usada em uma coluna, retorna os valores únicos dessa coluna e a quantidade de vezes que cada valor aparece.
#
# ```python
# df[coluna].value_counts()
# ```
#
# ##Descoberta guiada
# Inspeção de conteúdo
#
# Acesse o dataset do Titanic (https://www.harve.com.br/praticas/titanic-pt-BR.csv) e obtenha estatísticas sobre os passageiros:
#
# 1. Qual foi a idade média dos passageiros?
# 2. Quantas mulheres e quantos homens estavam a bordo?

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Qual foi a idade média dos passageiros?

# 2. Quantas mulheres e quantos homens estavam a bordo?

# ##Hands on!
# Inspeção de conteúdo
#
# Ainda sobre o dataset do Titanic (https://www.harve.com.br/praticas/titanic-pt-BR.csv), obtenha agora as seguintes informações:
#
# 1. Qual foi porcentagem de sobreviventes?
# 2. Quais foram as classes utilizadas pelos passageiros do titanic e quantas pessoas utilizaram cada uma delas?

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Qual foi porcentagem de sobreviventes?

# 2. Quais foram as classes utilizadas pelos passageiros do titanic e quantas pessoas utilizaram cada uma delas?
