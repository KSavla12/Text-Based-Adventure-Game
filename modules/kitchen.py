from .myimports import *
from modules.scenes import Scene
from modules.attributes import Inventory


class Kitchen(Scene):

    def __init__(self):
        self.scene = Scene()
        self.inventory = Inventory()

    def enter(self):

        dialogue = dedent("""
            Feeling famished you proceed down the hallway and enter the kitchen. Surprisingly, you spot a 
            bottle of water sitting on the countertop, providing a glimmer of relief for your parched throat. 
            Additionally, an untouched snack lying upon the dinner table.          
            
            The discovery brings a mix of gratitude and curiosity as you ponder who or what might have left 
            these provisions behind in this desolate place.
            """)
        self.scene.text_roll(dialogue)

        wat = False
        snk = False

        while True:

            action = input("> ")

            if action == "inventory":
                self.inventory.inventory_check()

            elif (action == "take water" or action == "water") and wat == False:
                print(dedent("""
                You take the bottle of water. -obtained bottle of water-
                """))
                Inventory.stock.remove('water')
                Inventory.invent.append('water')
                wat = 1

            elif (action == "take snack" or action == "snack") and snk == False:
                print(dedent("""
                You take the snack. -obtained snack-
                """))
                Inventory.stock.remove('snack')
                Inventory.invent.append('snack')
                snk = True

            elif ((action == "take snack" or action == "snack") and 'snack' not in Inventory.stock) or ((action == "take water" or action == "water") and 'water' not in Inventory.stock):
                print("\nI already got that.\n")

            elif action == "leave room" or action == "go back" or action == "hallway":
                return "hallway"

            else:
                self.scene.unknown()