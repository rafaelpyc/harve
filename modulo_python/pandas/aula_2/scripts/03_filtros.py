# -*- coding: utf-8 -*-

import pandas as pd

# #Filtros
#
# Filtros são usados para selecionar apenas as linhas que atendem a uma condição.
#
# Ao comparar uma coluna com algum valor, o pandas retorna `True` para as linhas que atendem à condição e `False` para as demais.
#
# ```python
# df['turma'] == 'A'
# ```
#
# Essa condição pode ser atribuída a uma variável como uma máscara ou filtro:
#
# ```
# filtro = df['turma'] == 'A'
# ```
#
# Depois, podemos aplicar o filtro dentro do DataFrame:
#
# ```
# df[filtro]
# ```
#
# Ou escrever o filtro direto no Dataframe:
# ```
# df[df['turma'] == 'A']
# ```
#
# Os operadores do python são:
#
# * `==`   igual
# * `!=`   diferente
# * `>`    maior
# * `>=`   maior ou igual
# * `<`    menor
# * `<=`   menor ou igual
#
# ## Descoberta guiada
# Filtros
#
# Usando o DataFrame de notas, responda:
#
# 1. Crie um filtro para identificar quais alunos são da turma `A`.
# 2. Selecione os alunos com nota maior ou igual a `7` na `prova_1`.
# 3. Verifique a média da `prova_1` e veja quais alunos estão abaixo da média.

dados: dict = {
    'nome': ['Ana', 'Pedro', 'João', 'Carla', 'Silvio', 'Teresa', 'Claudia', 'Cristiane'],
    'prova_1': [6, 7, 8, 8, 9, 3, 6, 5],
    'prova_2': [7, 8, 5, 7, 10, 8, 7, 7],
    'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}

df = pd.DataFrame(dados)
print(df)

# 1. Crie um filtro para identificar quais alunos são da turma `A`.

# 2. Selecione os alunos com nota maior ou igual a `7` na `prova_1`.

# 3. Verifique a média da `prova_1` e veja quais alunos estão abaixo da média.



# ## Hands on!
# Filtros
#
# Vamos voltar ao dataset do titanic e resolver:
#
# 1. Selecione somente os passageiros da classe `1`.
# 2. Selecione somente os passageiros com idade maior ou igual a `30`.
# 3. Descreva quais os Locais de Embarque mais tiveram sobreviventes.
# 4. Mostre as estatíticas dos passageiros que não sobreviveram.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
print(df.head())

# 1. Selecione somente os passageiros da classe `1`.

# 2. Selecione somente os passageiros com idade maior ou igual a `30`.

# 3. Descreva quais os Locais de Embarque mais tiveram sobreviventes.

# 4. Mostre as estatíticas dos passageiros que não sobreviveram.
