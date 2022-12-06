from .myimports import *
from modules.scenes import *
from modules.attributes import Inventory
# from modules.hallway import Hallway


class House(Scene):

    def __init__(self):
        self.scene = Scene()

    def intro(self):
        dialogue = dedent("""
            You awaken, lying on the ground, surrounded by trees towering above you. You are unable to recall how 
            you’ve ended up here in the centre of a forest. Following a faint trail, you find an abandoned house. 
            It does not seem like anyone has lived here for quite some time. The windows are boarded up, and 
            imprinted on the doormat "LEAVE". The sun is setting and are in need of shelter. It won't hurt to try 
            your luck.  
            """)
        self.scene.text_roll(dialogue)
        Scene.intro_house = True
        return House.enter(self)

    def enter(self):
        if Scene.intro_house == False:
            return House.intro(self)

        key = False
        ex = 0

        while True:
            action = input("> ")

            if action == "knock":
                print(dedent("""
                You knock on the door hoping for an answer but to no avail. Maybe I can try to find a way in...
                """))

            elif action == "check doormat" or action == "lift doormat" or action == "move doormat":
                print(dedent("""
                You move the door mat revealing a key concealed underneath.  -obtained key-
                """))
                key = True
                ex = 0

            elif (action == "open door" or action == "unlock door") and key == True:
                print(dedent("""
                You unlock the front door.
                """))
                return "hallway"

            elif action == "open door":
                print(dedent("""
                The door is locked, there must be another way in...
                """))

            elif action == "open window":
                print(dedent("""
                The windows are boarded shut.
                """))

            elif action == "zzz":
                print(dedent("""
                YOU CHEATER
                """))
                Scene.stairs = True
                Inventory.invent.append("snack")
                Inventory.invent.append("water")
                return "goldroom"

            else:
                self.scene.unknown()
                
            ex += 0.5
            if ex == 3.5:
                time.sleep(0.8)
                print(dedent("""
                The sun is starting to set, you hear howling echoing from the woods. I better get a move on.
                """))

            elif ex == 8:
                time.sleep(0.8)
                print(dedent("""
                This doormat looks suspiciously clean.
                """))

