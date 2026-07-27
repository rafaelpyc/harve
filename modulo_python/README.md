# Módulo Python

Repositório de estudos do módulo de Python, reunindo o material das aulas e os
projetos práticos. O conteúdo está dividido em duas grandes áreas: **análise de
dados com pandas** e **web scraping / automação**.

## Estrutura

```
pandas/         Aulas de manipulação e análise de dados com pandas
webscraping/    Projetos de coleta de dados e automação
```

### pandas

Notebooks e scripts que acompanham as aulas, cada uma em sua pasta
(`notebooks/`, `scripts/` e, quando há, `data/`):

- **aula_2** — inspeção de conteúdo, atribuição de dados, filtros e tratamento
  de dados faltantes e duplicados.
- **aula_3** — resumo estatístico e agrupamento (`groupby`).
- **aula_4** — concatenação e merge de dados, visualização e tópicos avançados,
  usando um conjunto de tabelas de exemplo e cotações da PETR4.

### webscraping

Projetos de coleta de dados e automação, cada um focado em uma ferramenta:

- **projeto-bs4** — coleta de dados com BeautifulSoup.
- **projeto-selenium** — automação de vagas no InfoJobs (login, busca, raspagem
  dos cards e fluxo de candidatura). Veja o
  [README do projeto](webscraping/projeto-selenium/README.md).
- **projeto-pyautogui** — automação de interface (mouse/teclado) com PyAutoGUI.
  Veja o [README do projeto](webscraping/projeto-pyautogui%20/README.md).
- **crewai-handoff** — evolução do projeto de vagas usando CrewAI.

## Requisitos

- Python 3.10+

As dependências de cada área ficam junto dos respectivos projetos. Recomenda-se
usar um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```
