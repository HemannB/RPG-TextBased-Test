from character import Character

def create_character():
    print("Bem vindo ao criador de personagem\n")
    name = input("Qual o seu nome? ")
    race = input("Escolha sua raça: anão, humano ou elfo? ")
    char_class = input("Escolha a classe: Guerreiro, Mago ou Ladino? ")

    player = Character(name,race,char_class)

    print(f"Você tem {player.points_to_allocate} pontos para alocar")
    for attribute in player.attributes:
        points = int(input(f"Quantos pontos você deseja alocar para o atributo {attribute}? "))
        player.allocate_points(attribute,points)

    print("\nSeu personagem foi criado com sucesso!")
    print(f"Nome: {player.name}, Raça: {player.race}, Classe: {player.char_class}")
    print(f"Atributos: {player.attributes}")
    return player

if __name__ == "__main__":
    player = create_character()