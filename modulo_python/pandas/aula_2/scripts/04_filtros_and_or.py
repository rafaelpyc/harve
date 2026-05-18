# -*- coding: utf-8 -*-

import pandas as pd

# # Filtros AND e OR
#
# Podemos combinar mais de uma condição em um filtro. No pandas:
#
# ```python
# &   representa E
# |   representa OU
#
# Cada condição deve ficar entre parênteses:
#
# ```
# filtros = (df['turma'] == 'A') & (df['prova_1'] > 7)
# df[filtros]
# ```
#
# em outro exemplo:
#
# ```
# df[(df['prova_1'] >= 8) | (df['prova_2'] >= 8)]
#
# ## Descoberta guiada
# Filtros utilizando AND e OR
#
# Usando o DataFrame de notas, responda:
#
# 1. Selecione os alunos da turma `A` que tiraram nota maior que `7` na `prova_1`.
# 2. Selecione os alunos que tiraram nota maior ou igual a `8` na `prova_1` ou na `prova_2`.

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Selecione os alunos da turma `A` que tiraram nota maior que `7` na `prova_1`.

# 2. Selecione os alunos que tiraram nota maior ou igual a `8` na `prova_1` ou na `prova_2`.

# ## Hands on!
# Filtros utilizando AND e OR
#
# Agora, usando o dataset do Titanic, resolva:
#
# 1. Quantos homens sobreviveram e eram das classes `1` ou `2`?
# 2. Quantas pessoas tinham mais de `40` anos e tinham pais/filhos ou irmãos/cônjuges?

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Quantos homens sobreviveram e eram das classes `1` ou `2`?

# 2. Quantas pessoas tinham mais de `40` anos e tinham pais/filhos ou irmãos/cônjuges?
