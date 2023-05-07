import pygame
from pygame_gui import UIManager, elements
import csv
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "My Game"
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

# Initialize the UI manager
ui_manager = UIManager(WINDOW_SIZE)

# Define some constants
TILE_SIZE = 32
MOVE_SPEED = 5
BATTLE_DELAY = 1000
ITEM_HEAL_AMOUNT = 20
MAX_CREATURES_IN_PARTY = 6

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(WHITE)
        self.creatures = []
        self.inventory = {"Potion": 3}

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def add_creature_to_party(self, creature):
        if len(self.creatures) < MAX_CREATURES_IN_PARTY:
            self.creatures.append(creature)
            ui_manager.remove_ui_element(ui_manager.get_top_layer())
            ui_manager.add_ui_element(elements.UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text=f"{creature.name} was added to your party!"))
        else:
            ui_manager.remove_ui_element(ui_manager.get_top_layer())
            ui_manager.add_ui_element(elements.UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text=f"Your party is full!"))

    def use_item(self, item_name):
        if item_name in self.inventory and self.creatures:
            creature = self.creatures[0]
            if creature.hp < creature.max_hp:
                creature.hp = min(creature.max_hp, creature.hp + ITEM_HEAL_AMOUNT)
                self.inventory[item_name] -= 1
                ui_manager.remove_ui_element(ui_manager.get_top_layer())
                ui_manager.add_ui_element(elements.UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text=f"{creature.name} was healed!"))
            else:
                ui_manager.remove_ui_element(ui_manager.get_top_layer())
                ui_manager.add_ui_element(elements.UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text=f"{creature.name} is already at full health!"))
        else:
            ui_manager.remove_ui_element(ui_manager.get_top_layer())
            ui_manager.add_ui_element(elements.UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text="You don't have any potions or creatures!"))

# Define the Creature class
class Creature:
    def __init__(self, name, max_hp, attack, defense, x, y):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.x = x
        self.y = y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(WHITE)

    def draw(self, surface):
        if self.x.isdigit() and self.y.isdigit():
            x = int(self.x)
            y = int(self.y)
            surface_width, surface_height = surface.get_size()
            if x >= 0 and x < surface_width and y >= 0 and y < surface_height:
                surface.blit(self.image, (x, y))

# Load the map data from a CSV file
with open("map.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    map_data = [[int(cell) for cell in row] for row in reader]

# Load the creature data from a CSV file
with open("creatures.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    creature_data = [row for row in reader]

# Create the Player and Creatures objects
player = Player(0, 0)
creatures = [Creature(*row) for row in creature_data]

# Define the game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -MOVE_SPEED)
            elif event.key == pygame.K_DOWN:
                player.move(0, MOVE_SPEED)
            elif event.key == pygame.K_LEFT:
                player.move(-MOVE_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(MOVE_SPEED, 0)
            elif event.key == pygame.K_a:
                if creatures:
                    creature = creatures[0]
                    player.add_creature_to_party(creature)
                    creatures.pop(0)
            elif event.key == pygame.K_h:
                player.use_item("Potion")

    # Draw the map
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell == 0:
                pygame.draw.rect(screen, BLACK, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw the Player and Creatures
    player.draw(screen)
    for creature in creatures:
        creature.draw(screen)

    # Update the display
    ui_manager.update(clock.tick(60)/1000.0)
    pygame.display.update()

# Quit Pygame
pygame.quit()