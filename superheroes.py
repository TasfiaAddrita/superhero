import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def defend(self):
        total_blocks = 0
        for armor in self.armors:
            total_blocks += armor.block()
        return total_blocks

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities):
            return print("Draw!")
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.is_alive() == False:
            self.add_death(1)
            opponent.add_kill(1)
            return print(f"{opponent.name} won!")
        else:
            self.add_kill(1)
            opponent.add_death(1)
            return print(f"{self.name} won!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, param_hero):
        for hero in self.heroes:
            if hero.name == param_hero:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        if len(self.heroes) > 0:
            hero_fighting = self.heroes[random.randint(0, len(self.heroes)-1)]
        # else:
        #     return 0

        if len(other_team.heroes) > 0:
            opponent_fighting = other_team.heroes[random.randint(0, len(other_team.heroes)-1)]
        # else:
        #     return 0

        hero_fighting.fight(opponent_fighting)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.starting_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(f"Kills/deaths: {hero.kills}/{hero.deaths}")

if __name__ == "__main__":
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    #
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # my_hero.add_ability(ability)
    # print(my_hero.abilities)
    #
    # ability2 = Ability("Flying", 50)
    # my_hero.add_ability(ability2)
    # print(my_hero.abilities)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
