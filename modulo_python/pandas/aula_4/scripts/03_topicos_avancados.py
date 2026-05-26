# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# # Tópicos avançados
# <a name="topicos-avancados"></a>

# Nesta seção, o objetivo é ampliar o repertório de pandas com recursos que aparecem com frequência em análises reais.
#
# A ideia não é decorar todos os métodos, mas entender **quando cada um ajuda a resolver um problema comum**: criar novas colunas, resumir dados, padronizar textos, filtrar registros e analisar séries temporais.
#
# Vamos passar pelos seguintes tópicos:
#
# * `apply` / `lambda` / `iterrows`
# * `pivot_table`
# * `map` / `replace`
# * `rename` / manipulação de strings
# * `isin` / `between`
# * `nlargest` / `nsmallest`
# * `rolling` (janela móvel)

# ## apply / lambda / iterrows

# Em muitas situações, uma transformação simples não resolve o problema. Por exemplo: criar uma faixa etária, classificar uma tarifa como cara ou barata, ou montar uma regra que depende de mais de uma coluna.
#
# É aqui que entram `apply`, `lambda` e, em alguns casos, `iterrows`.
#
# ### `lambda`
#
# Uma função `lambda` é uma função curta, escrita em uma única linha. Ela costuma ser usada quando a regra é simples e será aplicada apenas naquele momento.
#
# ```python
# lambda x: 'ALTO' if x > 100 else 'BAIXO'
# ```
#
# Nesse exemplo, `x` representa o valor que está sendo avaliado. Em uma coluna do pandas, esse `x` será cada valor da coluna, um por vez.
#
# ### `apply`
#
# O `apply()` serve para aplicar uma função em uma coluna ou em linhas de um DataFrame.
#
# Quando usamos `apply()` em uma coluna, o pandas passa cada valor dessa coluna para a função:
#
# ```python
# df['nova_coluna'] = df['coluna'].apply(lambda x: 'ALTO' if x > 100 else 'BAIXO')
# ```
#
# Também podemos usar uma função criada com `def`. Essa opção costuma deixar o código mais legível quando a regra tem mais etapas:
#
# ```python
# def classificar_idade(idade):
#     if idade <= 12:
#         return 'Criança'
#     elif idade < 60:
#         return 'Adulto'
#     else:
#         return 'Idoso'
#
# df['faixa_etaria'] = df['Idade'].apply(classificar_idade)
# ```
#
# ### `apply` linha a linha
#
# Quando a regra depende de mais de uma coluna, usamos `axis=1`. Nesse caso, a função recebe a linha inteira, e não apenas um valor isolado.
#
# ```python
# df['categoria'] = df.apply(
#     lambda linha: 'Prioridade' if linha['Idade'] > 60 and linha['Tarifa'] > 50 else 'Normal',
#     axis=1
# )
# ```
#
# ### `iterrows`
#
# O `iterrows()` percorre o DataFrame linha por linha. A cada repetição, ele retorna duas informações: o índice da linha e os valores daquela linha.
#
# ```python
# for indice, linha in df.iterrows():
#     print(indice, linha['Nome'], linha['Idade'])
# ```
#
# Ele é útil para entender a ideia de percorrer registros individualmente ou para fazer inspeções rápidas. Porém, em bases maiores, costuma ser mais lento. Na prática, prefira operações vetorizadas ou `apply()` sempre que possível.

# 1. No Titanic, crie uma coluna `faixa_etaria` com as regras:
#    * Idade até 12 → `'Criança'`
#    * Idade entre 13 e 59 → `'Adulto'`
#    * Idade 60+ → `'Idoso'`
# 2. Use iterrows para identificar passageiros em possível situação de prioridade. A ideia é percorrer o DataFrame linha por linha e criar uma lista com uma classificação simples para cada passageiro.
#
# Crie uma nova coluna chamada `prioridade_atencao` seguindo a regra:
#
# - se o passageiro for criança, classifique como `"prioridade"`;
# - se o passageiro estiver na 1ª classe, classifique como `"prioridade"`;
# - caso contrário, classifique como `"normal"`.

df = pd.read_csv('https://www.harve.com.br/praticas/titanic-pt-BR.csv')
df.head()

# 1. Crie a coluna faixa_etaria usando apply + lambda

# 2. Use iterrows para imprimir os 5 primeiros passageiros

# ## map / replace

# `map()` e `replace()` podem parecer parecidos porque os dois permitem trocar valores. A diferença principal está no que acontece com os valores que **não aparecem no dicionário de-para**.
#
# ### `map()`
#
# O `map()` é usado principalmente em uma única coluna. Ele cria uma nova correspondência entre valores antigos e novos.
#
# ```python
# df['sexo_pt'] = df['Sexo'].map({
#     'male': 'Masculino',
#     'female': 'Feminino'
# })
# ```
#
# O ponto de atenção é: se algum valor da coluna não estiver no dicionário, o resultado será `NaN`.
#
# ```python
# pd.Series(['A', 'B', 'C']).map({'A': 1, 'B': 2})
# # resultado: 1, 2, NaN
# ```
#
# Isso pode ser útil quando queremos descobrir valores inesperados ou categorias que ainda não foram tratadas. Mas também pode gerar perda de informação quando o dicionário está incompleto.
#
# ### `replace()`
#
# O `replace()` substitui apenas os valores encontrados no dicionário. Os valores que não aparecem no dicionário permanecem como estavam.
#
# ```python
# pd.Series(['A', 'B', 'C']).replace({'A': 1, 'B': 2})
# # resultado: 1, 2, 'C'
# ```
#
# Na prática:
#
# * use `map()` quando a coluna deve seguir um mapeamento fechado e valores fora do mapa devem chamar atenção;
# * use `replace()` quando você quer trocar apenas alguns valores e preservar o restante.

# 1. Verifique o uso de `map()` e `replace()` para trocar os valores da coluna `Embarcou`: `'S'` → `'Southampton'`, `'C'` → `'Cherbourg'`, `'Q'` → `'Queenstown'`.

# 1. Verifique o uso de `map()` e `replace()` para trocar os valores da coluna `Embarcou`:
# `'S'` → `'Southampton'`, `'C'` → `'Cherbourg'`, `'Q'` → `'Queenstown'`.

# ## pivot_table

# A `pivot_table` é uma forma prática de resumir dados cruzando categorias. Ela funciona de forma parecida com uma tabela dinâmica do Excel.
#
# A estrutura geral é:
#
# ```python
# pd.pivot_table(
#     df,
#     values='valor_a_resumir',
#     index='linhas',
#     columns='colunas',
#     aggfunc='mean'
# )
# ```
#
# Os principais argumentos são:
#
# * `values`: coluna que será resumida;
# * `index`: coluna usada nas linhas da tabela;
# * `columns`: coluna usada nas colunas da tabela;
# * `aggfunc`: função de agregação, como média, soma ou contagem.

# 1. Crie uma pivot table do Titanic mostrando a **taxa de sobrevivência média** onde:
#    * Linhas = `Classe`
#    * Colunas = `Sexo`
#    * Valores = `Sobrevivente`
# 2. Crie outra pivot table com a **idade média** por `Classe` e `Local de embarque`.

# 1. Crie uma pivot table do Titanic mostrando a **taxa de sobrevivência média** onde:
#   * Linhas = `Classe`
#   * Colunas = `Sexo`
#   * Valores = `Sobrevivente`

# 2. Crie outra pivot table com a **idade média** por `Classe` e `Local de embarque`.

# ## rename / manipulação de strings

# O `rename()` permite **renomear colunas** com um dicionário:
#
# ```python
# df = df.rename(columns={'nome_antigo': 'nome_novo'})
# ```
#
# Para manipular **texto dentro das colunas**, usamos o acessor `.str`:
#
# ```python
# df['coluna'].str.lower()            # tudo minúsculo
# df['coluna'].str.upper()            # tudo maiúsculo
# df['coluna'].str.strip()            # remove espaços nas pontas
# df['coluna'].str.contains('texto')  # retorna True/False
# df['coluna'].str.title()            # Primeira Letra Maiúscula
# ```

# 1. Renomeie a coluna `Pais ou filhos` para `pais_filhos` e `Irmãos e cônjuge` para `irmaos_conjuge`.
# 2. Use `str.contains()` para filtrar os passageiros cujo `Nome` contém `'Mrs.'`.
# 3. Crie uma coluna `titulo` extraindo o título do nome (Mr., Mrs., Miss., etc). Dica: `str.split(', ').str[1].str.split('.').str[0]`.

# 1. Renomeie a coluna `Pais ou filhos` para `pais_filhos` e `Irmãos e cônjuge` para `irmaos_conjuge`.

# 2. Use `str.contains()` para filtrar os passageiros cujo `Nome` contém `'Mrs.'`.

# 3. Crie uma coluna `titulo` extraindo o título do nome (Mr., Mrs., Miss., etc).
#Dica: `str.split(', ').str[1].str.split('.').str[0]`.

# ## isin / between

# O `isin()` filtra por uma **lista de valores** — mais limpo que encadear vários `|`:
#
# ```python
# df[df['coluna'].isin(['valor1', 'valor2', 'valor3'])]
# ```
#
# O `between()` filtra por **faixa de valores**:
#
# ```python
# df[df['coluna'].between(10, 50)]
# ```

# 1. Filtre os passageiros do Titanic que embarcaram em `'Southampton'` ou `'Cherbourg'` usando `isin()`.
# 2. Filtre os passageiros com idade **entre 18 e 35** usando `between()`.

# 1. Filtre os passageiros do Titanic que embarcaram em `'Southampton'` ou `'Cherbourg'` usando `isin()`.

# 2. Passageiros com idade entre 18 e 35

# ## nlargest / nsmallest

# `nlargest()` e `nsmallest()` são atalhos para encontrar rapidamente os maiores ou menores valores de uma coluna.
#
# Eles evitam o caminho mais longo de ordenar a base inteira e depois usar `head()`.
#
# ```python
# df.nlargest(5, 'coluna')    # 5 maiores valores
# df.nsmallest(3, 'coluna')   # 3 menores valores
# ```

# 1. Encontre os **5 passageiros mais novos**.
# 2. Encontre os **5 passageiros mais velhos**.

# 1. Top 5 passageiros mais novos

# 2. Top 5 passageiros mais velhos

# ## rolling (janela móvel)

# O `rolling()` calcula estatísticas usando uma janela móvel. Isso significa que, para cada linha, o pandas olha para um conjunto de linhas anteriores e calcula uma medida, como média, soma, mínimo ou máximo.
#
# Esse recurso é muito usado em séries temporais. Um exemplo comum é a média móvel de preços de ações, que ajuda a suavizar oscilações diárias.
#
# ```python
# df['media_movel_20'] = df['Close'].rolling(window=20).mean()
# ```
#
# Nesse exemplo, `window=20` indica que cada média será calculada considerando os 20 registros mais recentes.

# Agora vamos usar um dataset de preços diários da PETR4 para praticar janela móvel.
#
# 1. Carregue o DataFrame de ações.
# 2. Calcule a **média móvel de 20 dias** do preço de fechamento (`Close`).
# 3. Plote um gráfico de linha comparando o preço de fechamento original com a média móvel de 20 dias.

# 1. Carregue o DataFrame de ações

# 2. Média móvel de 20 dias

# 3. Gráfico: Close vs média móvel 20 dias
