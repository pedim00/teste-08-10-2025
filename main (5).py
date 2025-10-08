import pandas as pd

def exportar_csv(pessoas: list, nome_arquivo: str):
    pessoas_ajustadas = []
    for pessoa in pessoas:
        pessoa_copy = pessoa.copy()
        if isinstance(pessoa_copy.get("gostos"), list):
            pessoa_copy["gostos"] = ", ".join(pessoa_copy["gostos"])
        pessoas_ajustadas.append(pessoa_copy)

    df = pd.DataFrame(pessoas_ajustadas)
    df.to_csv(nome_arquivo, index=False)

pessoas = [
    {
        "nome": "Pedro",
        "idade": 28,
        "gostos": ["música", "cinema", "viagens"]
    },
    {
        "nome": "Paulo",
        "idade": 35,
        "gostos": ["futebol", "churrasco"]
    },
    {
        "nome": "Mcrataodaleste",
        "idade": 22,
        "gostos": ["leitura", "arte"]
    },
    {
        "nome": "Adonai",
        "idade": 40,
        "gostos": ["matematica", "ir a ascola"]
    },
    {
        "nome": "ELONMUSK",
        "idade": 30,
        "gostos":["construir foguetes", "colonizar marte"]
    }
]

exportar_csv(pessoas, "pessoas.csv")