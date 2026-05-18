# -*- coding: utf-8 -*-

import pandas as pd

# # Atribuição de dados
#
# Nesta etapa, vamos aprender como acessar, alterar e criar informações dentro de um DataFrame.
#
# Um DataFrame é parecido com uma planilha excel: temos linhas, colunas e valores.
#
# Para acessar uma coluna, podemos chamar diretamente pelo nome da coluna:
#
# ```python
# df['prova_1']
# ```
#
# Para acessar um valor podemos usar a função `loc` com o nome do índice e o nome da coluna:
# ```python
# df.loc['Ana', 'prova_1']
# ```
# ou, usar a função `iloc` com a posição da linha e a posição da coluna:
# ```python
# df.iloc[0, 2]
# ```
#
# Para alterar um valor específico do DataFrame, use `loc`!
#
# O `loc` deixa claro qual linha e qual coluna devem ser alteradas.
# ```python
# df.loc['Ana', 'prova_1'] = 8
# ```
#
# Evite fazer alterações usando dois acessos seguidos, como:
#
# ```python
# df['Ana']['prova_1'] = 8
# ```
# Esse tipo de escrita pode gerar alertas no pandas e nem sempre altera o DataFrame original corretamente!
#
# Para criar uma nova coluna, atribua o resultado diretamente ao nome da nova coluna:
# ```python
# df['media'] = (df['prova_1'] + df['prova_2']) / 2
# ```
#
# ## Descoberta guiada
# Atribuição de dados
#
# A partir do DataFrame de provas, vamos explorar as seguintes questões:
#
# 1. Selecione apenas a coluna `prova_1`
# 2. Consulte a nota da Ana na `prova_1`
# 3. Consulte o valor que está na quinta linha e na segunda coluna
# 4. Selecione as notas da `prova_1` de Carla, Silvio e Teresa
# 5. Selecione as linhas de Carla até Teresa, apenas para a coluna `prova_1`.
# 6. Selecione as duas últimas linhas da coluna `prova_2`
# 7. Altere a nota da Ana na `prova_1` para `8`.
# 8. Altere a nota da quarta linha e na `prova_1` para `0`.
# 9. Crie uma coluna chamada `media`, com a média entre `prova_1` e `prova_2`.

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Selecione apenas a coluna `prova_1`

# 2. Consulte a nota da Ana na `prova_1`

# 3. Consulte o valor que está na quinta linha e na segunda coluna

# 4. Selecione as notas da `prova_1` de Carla, Silvio e Teresa

# 5. Selecione as linhas de Carla até Teresa, apenas para a coluna `prova_1`.

# 6. Selecione as duas últimas linhas da coluna `prova_2`

# 7. Altere a nota da Ana na `prova_1` para `8`.

# 8. Altere a nota da quarta linha e na `prova_1` para `0`.

# 9. Crie uma coluna chamada `media`, com a média entre `prova_1` e `prova_2`.



# ## Hands on!
# Atribuição de dados
#
# Ainda sobre o dataset de provas, resolva:
#
# 1. Qual foi a nota do Pedro na `prova_2`?
# 2. Qual o valor está na linha de posição `2` e coluna de posição `1`?
# 3. Selecione as linhas de Pedro até Silvio, apenas para as colunas `prova_1` e `prova_2`
# 4. Altere o valor da `prova_2` de Silvio
# 5. Crie uma coluna chamada `media_ponderada`, contendo a média das provas onde a `prova_1` tem peso 2 e `prova_2` tem peso 3

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Qual foi a nota do Pedro na `prova_2`?

# 2. Qual o valor está na linha de posição `2` e coluna de posição `1`?

# 3. Selecione as linhas de Pedro até Silvio, apenas para as colunas `prova_1` e `prova_2`

# 4. Altere o valor da `prova_2` de Silvio

# 5. Crie uma coluna chamada `media_ponderada`, contendo a média das provas onde a `prova_1` tem peso 2 e `prova_2` tem peso 3
