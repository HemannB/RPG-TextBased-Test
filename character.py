class Character:
    def __init__(self, name, race, char_class):
        self.name = name,
        self.race = race,
        self.char_class = char_class
        self.level = 1
        self.xp = 0
        self.attributes = {
            "strength" : 0,
            "agility" : 0,
            "intelligence" : 0,
        }
        self.points_to_allocate = 6

    def allocate_points(self, attribute, points):
        if points <= self.points_to_allocate:
            self.attributes[attribute] += points
            self.points_to_allocate -= points
        else:
            print("Você não tem pontos para distribuir")

    def level_up(self):
        self.level += 1
        self.points_to_allocate += 2
        print(f'{self.name} subiu para o nível {self.level}')

