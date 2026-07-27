<div align="center">

# projeto-bs4

**Coletor de vagas do InfoJobs com requests + BeautifulSoup**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![requests](https://img.shields.io/badge/requests-2C2D72)](https://requests.readthedocs.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4B8BBE)](https://www.crummy.com/software/BeautifulSoup/)

</div>

---

## Visão geral

Script simples que baixa a página de vagas de **programador Python** no InfoJobs,
faz o parse do HTML e extrai o título e a empresa de cada vaga.

É a versão mais direta de raspagem do módulo: uma única requisição HTTP e leitura
do HTML **estático** entregue pelo servidor — sem navegador, sem JavaScript. Por
isso pega apenas os cards renderizados na primeira carga (~20 vagas); o carregamento
por scroll infinito não é coberto aqui (para isso, veja o
[projeto-selenium](../projeto-selenium/README.md)).

---

## Como funciona

| Função | O que faz |
|---|---|
| `baixar_pagina(url)` | Faz o `GET` com um `User-Agent` de navegador e valida o status (`raise_for_status`). |
| `extrair_vagas(card)` | Lê um card e devolve `(título, empresa)` — usa `"Empresa Confidencial"` quando a empresa não aparece. |
| `coletar_vagas()` | Orquestra: baixa a página, seleciona os cards (`div.js_vacancyLoad`) e monta a lista de vagas. |

Seletores usados (classes `js_*`, mais estáveis que classes de layout):

- Card da vaga: `div.js_vacancyLoad`
- Título: `h2.js_vacancyTitle`
- Empresa: `a.text-body`

---

## Requisitos

- Python 3.10+

---

## Instalação

Recomenda-se usar um ambiente virtual. A partir da pasta `webscraping/`:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> O `requirements.txt` fica na pasta `webscraping/`, um nível acima, pois é
> compartilhado com os outros projetos do módulo.

---

## Como executar

```bash
python coletor.py
```

Imprime a quantidade de vagas encontradas e, em seguida, cada `(título, empresa)`.

---

## Autor

**Rafael Nunes de Campos**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-nunes-de-campos/)

---

<div align="center">

Projeto educacional · Feito com carinho no 🇧🇷

</div>
