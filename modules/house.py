from .myimports import *
from modules.scenes import *
from modules.attributes import Inventory
# from modules.hallway import Hallway


class House(Scene):

    def __init__(self):
        self.scene = Scene()

    def intro(self):
        dialogue = dedent("""
            As you regain consciousness, you find yourself lying on the ground, encircled by towering trees. The 
            details of how you arrived at this forest center elude your memory. Tracing a faint path, you stumble 
            upon an uninhabited house. Evidently deserted for a considerable duration, the windows are 
            barricaded, and the doormat bears the word "LEAVE." With the sun descending and your need for shelter 
            growing, it seems worth a shot to explore your chances there.  
            """)
        self.scene.text_roll(dialogue)
        Scene.intro_house = True
        return House.enter(self)

    def enter(self):
        if Scene.intro_house == False:
            return House.intro(self)

        key = False
        extra_dialogue = 0

        while True:
            action = input("> ")

            if action == "knock":
                print(dedent("""
                You knock on the door hoping for an answer, but to no avail. Maybe I can try to find a way in...
                """))

            elif action == "check doormat" or action == "lift doormat" or action == "move doormat":
                print(dedent("""
                You lift the doormat, revealing a key concealed beneath it.  -obtained key-
                """))
                key = True
                extra_dialogue = 0

            elif (action == "open door" or action == "unlock door" or action == "use key") and key == True:
                print(dedent("""
                You unlock the front door.
                """))
                return "hallway"

            elif action == "open door":
                print(dedent("""
                The door is locked, if only I had a key...
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
                
            extra_dialogue += 0.5
            if extra_dialogue == 3.5:
                time.sleep(0.8)
                print(dedent("""
                The sun is starting to set, you hear howling echoing from the woods. I better get a move on.
                """))

            elif extra_dialogue == 8:
                time.sleep(0.8)
                print(dedent("""
                You can't help but notice that the doormat appears surprisingly pristine, considering the 
                abandoned state of the house... 
                """))

