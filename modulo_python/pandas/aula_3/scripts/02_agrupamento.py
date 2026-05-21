# -*- coding: utf-8 -*-

import pandas as pd

# # Agrupamento
#
# Agrupamento é uma operação comum quando desejamos **resumir dados numéricos por categoria**.
#
# No pandas usamos o `groupby` para agrupar, escolhendo a **coluna de agrupamento** e a **função de agregação**:
#
# ```python
# df.groupby(by=['turma']).mean(numeric_only=True)
# ```
#
# Como o retorno é um DataFrame, podemos selecionar apenas a coluna que queremos visualizar:
#
# ```python
# df.groupby(by=['turma'])['prova_1'].mean()
# ```
#
# Para **ordenar** o resultado, temos duas opções:
#
# `sort_values()` ordena **pelos valores**:
# ```python
# df.groupby(by=['turma'])['prova_1'].mean().sort_values(ascending=True)
# ```
#
# `sort_index()` ordena **pelo índice** (a coluna de agrupamento):
# ```python
# df.groupby(by=['turma'])['prova_1'].mean().sort_index(ascending=True)
# ```
#
# O resultado do `groupby` usa a coluna de agrupamento como índice. Para **transformar de volta em um DataFrame comum**, usamos `reset_index()`:
#
# ```python
# df.groupby(by=['turma'])['prova_1'].mean().reset_index()
# ```
#
# Com `agg()` podemos aplicar **múltiplas funções de agregação** de uma vez:
#
# ```python
# df.groupby(by=['turma'])['prova_1'].agg(['mean', 'sum', 'count'])
# ```
#
# Também podemos aplicar **funções diferentes por coluna** usando um dicionário:
#
# ```python
# df.groupby(by=['turma']).agg({'prova_1': 'mean', 'prova_2': 'max'})
# ```
#
# Podemos agrupar por **múltiplas colunas** passando uma lista:
#
# ```python
# df.groupby(by=['turma', 'aprovado']).mean(numeric_only=True)
# ```
#
# ## Descoberta guiada
# Agrupamento
#
# Usando o DataFrame de notas, responda:
#
# 1. Calcule a média de todas as colunas numéricas agrupadas por `turma`.
# 2. Calcule a média da `prova_1` por `turma`.
# 3. Ordene o resultado do exercício anterior em ordem crescente.
# 4. Para cada `turma`, exiba a média, a soma e a quantidade de alunos da `prova_1` usando `agg()`.
# 5. Transforme o resultado do exercício anterior em um DataFrame comum usando `reset_index()`.

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Calcule a média de todas as colunas numéricas agrupadas por `turma`.

# 2. Calcule a média da `prova_1` por `turma`.

# 3. Ordene o resultado do exercício anterior em ordem crescente.

# 4. Para cada `turma`, exiba a média, a soma e a quantidade de alunos da `prova_1` usando `agg()`.

# 5. Transforme o resultado do exercício anterior em um DataFrame comum usando `reset_index()`.

# ## Hands on!
# Agrupamento
#
# Usando o dataset do Titanic, resolva:
#
# 1. Qual classe tem a maior quantidade de pais ou filhos?
# 2. Qual é a media das idades de cada classe?
#
# BÔNUS)
# Crie uma coluna `Crianca` com 1 para crianças (idade < 15) e 0 para adultos.
# Depois agrupe por `Classe`, `Sexo` e `Crianca` ao mesmo tempo e calcule a média de `Sobrevivente`.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Qual classe tem a maior de pais ou filhos?

# 2. Qual é a média das idades de cada classe?

# BÔNUS. Crie uma coluna `Crianca` com 1 para crianças (idade < 15) e 0 para adultos.
# Depois agrupe por `Classe`, `Sexo` e `Crianca` ao mesmo tempo e calcule a média de `Sobrevivente`.
