<div align="center">

# projeto-selenium

**Automação de vagas no InfoJobs — login, busca, raspagem e candidatura**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Chrome](https://img.shields.io/badge/Chrome-4285F4?logo=googlechrome&logoColor=white)](https://www.google.com/chrome/)
[![loguru](https://img.shields.io/badge/logs-loguru-blue)](https://github.com/Delgan/loguru)

</div>

---

## Visão geral

Automação em Python que faz **login** no InfoJobs, **busca** vagas por
palavra-chave, **raspa** os cards de resultado (título, empresa, local e link),
salva tudo em CSV e demonstra o **fluxo de candidatura** em uma vaga escolhida.

Ao contrário do [projeto-bs4](../projeto-bs4/README.md) — que lê apenas o HTML
estático — aqui um navegador real é dirigido pelo Selenium, o que permite passar
pelo login, fechar pop-ups e acionar o **scroll infinito** para carregar mais
vagas.

> ⚠️ **Projeto educacional.** Requer credenciais reais do InfoJobs; use com
> responsabilidade e apenas na sua própria conta. O `.env` nunca deve ser commitado.

---

## Fluxo

```
login → busca + scroll → raspagem dos cards → CSV → (opcional) candidatura
```

| Etapa | Módulo | O que faz |
|---|---|---|
| 1 | `login.py` | Carrega as credenciais do `.env`, aceita cookies e faz login. |
| 2 | `buscar_vagas.py` | Fecha o pop-up, pesquisa por descrição, raspa os cards (com scroll para carregamento incremental) e salva em `dados/vagas_selenium.csv`. |
| 3 | `candidatar.py` | Abre a vaga escolhida por índice, clica em candidatar, confirma que a página pós-candidatura carregou e volta à anterior. |
| 4 | `main.py` | Orquestra tudo, com logs em `logs/app.log` e screenshot em `logs/snapshots/` quando algo falha. |

---

## Requisitos

- Python 3.10+
- Google Chrome instalado (o Selenium gerencia o driver automaticamente)
- Conta no InfoJobs

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

## Configuração

Copie `.env.exemplo` para `.env` e preencha as credenciais:

```bash
cp .env.exemplo .env
```

```
INFOJOBS_EMAIL=seu-email@exemplo.com
INFOJOBS_SENHA=sua-senha
```

O `.env` está no `.gitignore` e nunca deve ser commitado.

---

## Como executar

```bash
python main.py
```

Opções de linha de comando:

```bash
python main.py --busca "data engineer" --vaga 2 --pausar-no-erro
```

| Opção | Descrição |
|---|---|
| `--busca` | Termo pesquisado no campo de vagas (padrão: `python`). |
| `--vaga` | Índice do card para candidatura. **Sem este argumento, nenhuma candidatura é feita** — o script apenas busca, raspa e salva o CSV. |
| `--pausar-no-erro` | Em caso de falha, mantém o navegador aberto para inspeção até pressionar Enter (apenas em execuções interativas). |

---

## Autor

**Rafael Nunes de Campos**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-nunes-de-campos/)

---

<div align="center">

Projeto educacional · Feito com carinho no 🇧🇷

</div>
