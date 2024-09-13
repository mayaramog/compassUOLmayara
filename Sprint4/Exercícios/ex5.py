"""
round, map e sorted.

Processar um arquivo csv com o nome e 5 notas
dos estudantes. O código deve imprimir o nome,
as tres maiores notas em ordem decrescente e a 
media das tres maiores notas com duas casas
decimais de precisão.

"""


def processar_arquivo(csv):
    with open(csv, "r") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.readlines()

    def processar_linha(linha):
        # Divide as informações das linhas e transforma em inteiro as notas
        divs = linha.strip().split(",")
        nome = divs[0]
        notas = list(map(int, divs[1:]))
        
        # Ordena decrescente as notas e seleciona os 3 maiores
        tres_maiores = sorted(notas, reverse=True)[:3]

        media = round(sum(tres_maiores) / 3, 2)

        # Retorna um dicionario
        return {
            "Nome": nome,
            "Notas": tres_maiores,
            "Media": media
        }
    
    
    # Usa a funcao e transforma em lista o resultado das linhas
    estudantes = list(map(processar_linha, linhas))
    
    # Ordena os estudantes pelo seu nome
    est_ordenados = sorted(estudantes, key=lambda x: x["Nome"])
    
    for estudante in est_ordenados:
        print(f"Nome: {estudante['Nome']} Notas: {estudante['Notas']} Média: {estudante['Media']}")


processar_arquivo("estudantes.csv")
