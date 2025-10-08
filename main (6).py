def adicionar_gostos(pessoas: list, gostos: list) -> list:
    mapa = {g["id"]: g["gostos"] for g in gostos}
    
    for pessoa in pessoas:
        pessoa_id = pessoa.get("id")
        pessoa["gostos"] = mapa.get(pessoa_id, [])
    
    return pessoas[:5]  


pessoas = [
    {"id": 1, "nome": "Alice"},
    {"id": 2, "nome": "Bruno"},
    {"id": 3, "nome": "Carla"},
    {"id": 4, "nome": "Gabriel"},
    {"id": 5, "nome": "Paulo"},
    {"id": 6, "nome": "Pedro"},
]

gostos = [
    {"id": 1, "gostos": ["futebol", "cinema"]},
    {"id": 2, "gostos": ["leitura"]},
    {"id": 3, "gostos": ["natação", "jogos"]},
    {"id": 4, "gostos": ["dança"]},
    {"id": 5, "gostos": ["música", "pintura"]},
    {"id": 6, "gostos": ["teatro"]}
]


pessoas = adicionar_gostos(pessoas, gostos)

for pessoa in pessoas:
    print(pessoa)