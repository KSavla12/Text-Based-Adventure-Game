from .myimports import *
from modules.scenes import Scene
from modules.attributes import Inventory

class Hallway(Scene):

    def __init__(self):
        self.scene = Scene()
        self.inventory = Inventory()

    def intro(self):
        dialogue = dedent("""
            You enter the house into the hallway. You find to your surprise the lights are on, emitting a dim
            glow. The place is old and tattered and you feel an eerie vibe in the atmosphere. You hear a creaking
            of the floor board from up above, perhaps it was just a rat?

            There seems to be a kitchen straight down the hallway. On the left is a door with a sign labelled
            "cellar", and a staircase leading upwards to your right.
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
