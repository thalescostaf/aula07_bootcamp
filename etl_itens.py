import csv

path_arquivo = 'vendas.csv'

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    '''
    Função que le um arquivo e retorna lista de dicionários
    '''
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='ISO-8859-1') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista

def filtrar_produtos(lista: list[dict]) -> list[dict]:
    '''
    Função que filtra os itens igual Bike
    '''
    lista_produtos_filtrados = []
    for item in lista:
        if item.get('False') == 'True':
            lista_produtos_filtrados.append(item)
    return lista_produtos_filtrados


lista_produtos = ler_csv(path_arquivo)
lista_produtos_filtrados = filtrar_produtos(lista_produtos)
print(lista_produtos_filtrados)