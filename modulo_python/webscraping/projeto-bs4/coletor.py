"""
Automação com beatifulsoup para extrair vagas de programador python na Infojobs
"""

import requests
from bs4 import BeautifulSoup



def baixar_pagina(url: str) -> str:
    """Faz a requisição do html da página com erro"""

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36" }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    return response


def extrair_vagas(card) -> tuple[str]:
    """Extrai os dados principais de um card de vaga."""

    title = card.select_one('h2.js_vacancyTitle')
    empresa = card.select_one('a.text-body')
    empresa = empresa.get_text(strip=True, separator=' ') if empresa else 'Empresa Confidencial'

    return (title.get_text(strip=True), empresa)


def coletar_vagas() -> list[str]:
    """Baixa a página, encontra os cards e devolve uma lista de vagas."""

    url = "https://www.infojobs.com.br/vagas-de-programador-python"
    response = baixar_pagina(url=url)

    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select("div.js_vacancyLoad")
    vagas = []

    for card in cards:
        info = extrair_vagas(card)
        vagas.append(info)

    return vagas

if __name__ == '__main__':

    vagas = coletar_vagas()
    print(len(vagas))
    for vaga in vagas:
        print(vaga)
