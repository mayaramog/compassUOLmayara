# Lista de nomes de animais
animais = [
    "cachorro", "gato", "leão", "tigre", "elefante", "rinoceronte", "girafa",
    "urso", "panda", "zebra", "cavalo", "vaca", "ovelha", "coelho", "raposa",
    "lobo", "camelo", "baleia", "golfinho", "tartaruga"
]

# Ordena a lista em ordem crescente
animais.sort()

# Itera sobre os itens e imprime um a um
[print(animal) for animal in animais]

# Armazena o conteúdo em um arquivo CSV
with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")
