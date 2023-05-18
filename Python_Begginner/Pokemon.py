import random

class Creature:
    def __init__(self, name, type, max_hp, attack, defense):
        self.name = name
        self.type = type
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            
    def is_alive(self):
        return self.hp > 0

    def attack_creature(self, creature):
        damage = int(self.attack * random.uniform(0.8, 1.2))
        damage -= int(creature.defense * random.uniform(0.0, 0.2))
        creature.take_damage(damage)
        print(f"{self.name} attacks {creature.name} for {damage} damage!")
        
    def __repr__(self):
        return f"{self.name} ({self.hp}/{self.max_hp})"
        
class Trainer:
    def __init__(self, name):
        self.name = name
        self.creatures = []
        self.items = {"Potion": 5, "Super Potion": 10}
        
    def add_creature(self, creature):
        if len(self.creatures) < 6:
            self.creatures.append(creature)
        else:
            print("Sorry, you cannot carry more than 6 creatures.")

    def use_item(self, item, creature):
        if item in self.items and creature.hp > 0:
            if self.items[item] > 0:
                if item == "Potion":
                    creature.hp += 20
                    if creature.hp > creature.max_hp:
                        creature.hp = creature.max_hp
                elif item == "Super Potion":
                    creature.hp += 50
                    if creature.hp > creature.max_hp:
                        creature.hp = creature.max_hp
                self.items[item] -= 1
                print(f"{self.name} uses {item} on {creature.name}")
            else:
                print(f"You don't have any {item}s left!")
        else:
            print(f"You can't use {item} on {creature.name} right now.")
        
    def __repr__(self):
        return f"{self.name} ({len(self.creatures)} creatures)"
        
# Create some creatures
pikachu = Creature("Pikachu", "Electric", 100, 20, 10)
charmander = Creature("Charmander", "Fire", 80, 30, 5)
squirtle = Creature("Squirtle", "Water", 120, 15, 20)

# Create a trainer
ash = Trainer("Ash")
ash.add_creature(pikachu)
ash.add_creature(charmander)
ash.add_creature(squirtle)

# Create another trainer
misty = Trainer("Misty")
misty.add_creature(squirtle)
misty.add_creature(charmander)

# Ash battles Misty
print(f"{ash.name} challenges {misty.name} to a battle!")
ash_creature = ash.creatures[0]
misty_creature = misty.creatures[0]
print(f"{ash.name} sends out {ash_creature.name}!")
print(f"{misty.name} sends out {misty_creature.name}!")

# Battle loop
while ash_creature.is_alive() and misty_creature.is_alive():
    # Ash's turn
    print(f"{ash_creature.name} has {ash_creature.hp}/{ash_creature.max_hp} HP")
    action = input("Choose an action (attack, item): ")
    if action == "attack":
        ash_creature.attack_creature(misty_creature)
    elif action == "item":
        item = input("Choose an item (Potion, Super Potion): ")
        ash.use_item(item, ash_creature)
    else:
        print("Invalid action")

    # Misty's turn
    if misty_creature.is_alive():
        print(f"{misty_creature.name} has {misty_creature.hp}/{misty_creature.max_hp} HP")
        misty_creature.attack_creature(ash_creature)

# Print the winner
if ash_creature.is_alive():
    print(f"{ash.name} wins!")
else:
    print(f"{misty.name} wins!")