import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = int(max_block)

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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def attack(self):
        total_damage = 0
        if len(self.abilities) != 0:
            ability = self.abilities[random.randint(0, len(self.abilities)-1)]
            total_damage = ability.attack()
            print(f"{self.name} used '{ability.name}' that caused {total_damage} damage!")
            return total_damage
        return 0

    def defend(self):
        if len(self.armors) != 0:
            armor = self.armors[random.randint(0, len(self.armors)-1)]
            print(f"{self.name} used '{armor.name}' that protected them from {armor.block()} damage!")
            return armor.block()
        return 0

    def take_damage(self, damage):
        damage_total = damage - self.defend()
        if damage_total < 0:
            damage_total = 0
        self.current_health -= damage_total

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        print(f"{self.name}'s starting health is {self.starting_health}.")
        print(f"{opponent.name}'s starting health is {opponent.starting_health}.\n")
        # if len(self.abilities) == 0 and len(opponent.abilities) == 0:
        #     return print("Draw!")
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            if self.is_alive():
                print(f"{self.name} current health is {self.current_health}.")
            else:
                print(f"{self.name} died.\n")
                break
            opponent.take_damage(self.attack())
            if opponent.is_alive():
                print(f"{opponent.name} current health is {opponent.current_health}.\n")
            else:
                print(f"{opponent.name} died.\n")
        if self.is_alive() == False:
            self.add_death(1)
            opponent.add_kill(1)
            print(f"{opponent.name} won!")
            print(f"{self.name} lost.\n")
        else:
            self.add_kill(1)
            opponent.add_death(1)
            print(f"{self.name} won!")
            print(f"{opponent.name} lost.\n")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.heroes_died = 0

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
        hero_fighting_alive = False
        opponent_fighting_alive = False

        while (hero_fighting_alive == False):
            hero_fighting = self.heroes[random.randint(0, len(self.heroes)-1)]
            hero_fighting_alive = hero_fighting.is_alive()

        while (opponent_fighting_alive == False):
            opponent_fighting = other_team.heroes[random.randint(0, len(other_team.heroes)-1)]
            opponent_fighting_alive = opponent_fighting.is_alive()

        hero_fighting.fight(opponent_fighting)

        if hero_fighting.is_alive() == False:
            self.heroes_died += 1
        if opponent_fighting.is_alive() == False:
            other_team.heroes_died += 1

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

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability_name = input("Name of ability: ")
        ability_max_damage = input(f"What is the max damage of {ability_name}: ")
        new_ability = Ability(ability_name, ability_max_damage)
        return new_ability

    def create_weapon(self):
        weapon_name = input("Name of weapon: ")
        weapon_max_damage = input(f"What is the max damage of {weapon_name}: ")
        new_weapon = Ability(weapon_name, weapon_max_damage)
        return new_weapon

    def create_armor(self):
        armor_name = input("Name of armor: ")
        armor_max_damage = input(f"What is the max damage of {armor_name}: ")
        new_armor = Armor(armor_name, armor_max_damage)
        return new_armor

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\n")
            # if add_item not in range(1, 5):
            #     print("Please enter a value between 1-4")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        team_name = input("Team 1 name: ")
        team_one = Team(team_name)
        num_heroes = int(input("Number of heroes in Team 1: "))
        for index in range(num_heroes):
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one

    def build_team_two(self):
        team_name = input("Team 2 name: ")
        team_two = Team(team_name)
        num_heroes = int(input("Number of heroes in Team 2: "))
        for index in range(num_heroes):
            hero = self.create_hero()
            team_two.add_hero(hero)
        self.team_two = team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        round = 1
        while(len(self.team_one.heroes) != self.team_one.heroes_died and len(self.team_two.heroes) != self.team_two.heroes_died):
            print(f"---------- ROUND {round} ----------\n")
            self.team_one.attack(self.team_two)
            round += 1

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        print("---------- BATTLE STATISTICS ----------\n")
        team_one_alive_count = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                team_one_alive_count += 1

        team_two_alive_count = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                team_two_alive_count += 1

        if team_one_alive_count > team_two_alive_count:
            print("Team 1 won!\n")
        else:
            print("Team 2 won!\n")

        team_one_kills = 0
        team_one_deaths = 0

        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths

        team_one_average_kills = team_one_kills / len(self.team_one.heroes)
        team_one_average_deaths = team_one_deaths / len(self.team_one.heroes)

        team_two_kills = 0
        team_two_deaths = 0

        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths

        team_two_average_kills = team_two_kills / len(self.team_two.heroes)
        team_two_average_deaths = team_two_deaths / len(self.team_two.heroes)

        print(f"Team 1's average kill/death: {team_one_average_kills}/{team_one_average_deaths}")
        print(f"Team 2's average kill/death: {team_two_average_kills}/{team_two_average_deaths}\n")

        print("Surviving heroes in Team 1: ")
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"- {hero.name}")
        if team_one_alive_count == 0:
            print("No one survived.")

        print("\nSurviving heroes in Team 2: ")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"- {hero.name}")
        if team_two_alive_count == 0:
            print("No one survived.")

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

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    arena = Arena()
    arena.build_team_one()
    arena.team_one.view_all_heroes()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
