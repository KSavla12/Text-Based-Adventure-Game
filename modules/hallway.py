from .myimports import *
from modules.scenes import Scene
from modules.attributes import Inventory

class Hallway(Scene):

    def __init__(self):
        self.scene = Scene()
        self.inventory = Inventory()

    def intro(self):
        dialogue = dedent("""
            You step inside the house and find yourself in a dimly lit hallway, illuminated by flickering lights 
            that catch you off guard. The worn-out and dilapidated state of the place creates an unsettling ambiance. 
            Suddenly, a creaking sound emanates from the floor above. You ponder whether it's merely a rat scurrying 
            about.

            Straight ahead, at the end of the hallway, you spot a kitchen. To your left, there's a door marked 
            "cellar," and to your right, a staircase ascends to the upper level.
            """)
        self.scene.text_roll(dialogue)
        Scene.intro_hallway = True
        return Hallway.enter(self)

    def enter(self):
        if Scene.intro_hallway == False:
            return Hallway.intro(self)

        while True:
            action = input("> ")

            if action == "stairs" and Scene.stairs == True:
                print("I've already been up there.")

            elif action == "stairs" or action == "staircase" or action == "go up stairs" or action == "upstairs" or action == "stairway":
                return "stairway"

            elif action == "kitchen" or action == "enter kitchen":
                return "kitchen"

            elif action == "cellar" or action == "enter cellar":
                return "cellar"

            elif action == "inventory":
                self.inventory.inventory_check()

            else:
                self.scene.unknown()
