# Projeto Selenium — Automação de vagas no InfoJobs

Automação em Python que faz login no InfoJobs, busca vagas por palavra-chave,
raspa os cards de resultado (título, empresa, local e link), salva tudo em CSV
e demonstra o fluxo de candidatura em uma vaga escolhida.

## Fluxo

1. `login.py` — carrega as credenciais do `.env`, aceita cookies e faz login.
2. `buscar_vagas.py` — fecha o pop-up, pesquisa por descrição, raspa os cards
   (com scroll para carregamento incremental) e salva em `dados/vagas_selenium.csv`.
3. `candidatar.py` — abre a vaga escolhida por índice, clica em candidatar,
   confirma que a página pós-candidatura carregou e volta à página anterior.
4. `main.py` — orquestra tudo, com logs em `logs/app.log` e captura de
   screenshot em `logs/snapshots/` quando algo falha.

## Requisitos

- Python 3.10+
- Google Chrome instalado (o Selenium gerencia o driver automaticamente)
- Conta no InfoJobs

## Instalação

```bash
pip install -r ../requirements.txt
```

> O `requirements.txt` fica na pasta `webscraping/`, um nível acima, pois é
> compartilhado com os outros projetos do módulo.

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

## Como executar

```bash
python main.py
```

Opções de linha de comando:

```bash
python main.py --busca "data engineer" --vaga 2 --pausar-no-erro
```

- `--busca` — termo pesquisado no campo de vagas (padrão: `python`).
- `--vaga` — índice do card para candidatura. **Sem este argumento, nenhuma
  candidatura é feita** — o script apenas busca, raspa e salva o CSV.
- `--pausar-no-erro` — em caso de falha, mantém o navegador aberto para
  inspeção até pressionar Enter (apenas em execuções interativas).
