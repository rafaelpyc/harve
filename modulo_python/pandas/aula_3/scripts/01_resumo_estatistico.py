# -*- coding: utf-8 -*-

import pandas as pd

# # Resumo estatístico
#
# O Pandas permite realizar diversas análises estatísticas com poucas linhas de código.
#
# Para **somar** os valores de uma coluna, usamos a função `sum()`:
#
# ```python
# df['prova_1'].sum()
# ```
#
# Existem outras funções de agregação disponíveis:
#
# * `sum()` — soma dos valores
# * `mean()` — média
# * `median()` — mediana
# * `max()` — valor máximo
# * `min()` — valor mínimo
# * `count()` — quantidade de valores não nulos
# * `std()` — desvio padrão
#
# Para descobrir **qual índice** possui o maior ou menor valor de uma coluna, usamos `idxmax()` e `idxmin()`:
#
# ```python
# df['prova_1'].idxmax()   # índice da maior nota
# df['prova_1'].idxmin()   # índice da menor nota
# ```
#
# Isso é muito útil para responder perguntas como "quem tirou a maior nota?" em vez de apenas "qual foi a maior nota?".
#
# A função `cumsum()` retorna a **soma acumulada** dos valores de uma coluna:
#
# ```python
# df['prova_1'].cumsum()
# ```
#
# Cada linha mostra a soma de todos os valores anteriores até ela. É útil para acompanhar a evolução de totais.
#
# Para verificar a **correlação** entre colunas numéricas, usamos `corr()`:
#
# ```python
# df.corr(numeric_only=True)
# ```
#
# O resultado varia de `-1` (correlação negativa perfeita) a `1` (correlação positiva perfeita). Valores próximos de `0` indicam pouca correlação.
#
# ## Descoberta guiada
# Resumo estatístico
#
# Usando o dataset do Titanic (https://www.harve.com.br/praticas/titanic-pt-BR.csv), responda:
#
# 1. Qual é a idade máxima e a idade mínima dos passageiros?
# 2. Qual é a soma total da coluna `Pais ou filhos`?
# 3. Qual é o índice do passageiro mais velho? E do mais novo?
# 4. Crie uma coluna `Idade_acumulada` com a soma acumulada da coluna `Idade`.
# 5. Exiba a correlação entre as colunas numéricas do DataFrame.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Qual é a idade máxima e a idade mínima dos passageiros?

# 2. Qual é a soma total da coluna `Pais ou filhos`?

# 3. Qual é o índice do passageiro mais velho? E do mais novo?

# 4. Crie uma coluna `Idade_acumulada` com a soma acumulada da coluna `Idade`.

# 5. Exiba a correlação entre as colunas numéricas do DataFrame.

# ## Hands on!
# Resumo estatístico
#
# Usando o DataFrame de notas, responda:
#
# 1. Qual é a soma das notas da `prova_1`?
# 2. Qual é a nota máxima e a nota mínima da `prova_2`?
# 3. Qual é a média da `prova_1`?

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Qual é a soma das notas da `prova_1`?

# 2. Qual é a nota máxima e a nota mínima da `prova_2`?

# 3. Qual é a média da `prova_1`?
