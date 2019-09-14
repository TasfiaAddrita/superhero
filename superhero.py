import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        pass

    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        pass

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    my_hero.add_ability(ability)
    print(my_hero.abilities)

    ability2 = Ability("Flying", 50)
    my_hero.add_ability(ability2)
    print(my_hero.abilities)
