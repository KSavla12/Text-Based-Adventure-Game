from .myimports import *
from modules.scenes import *
# from modules.hallway import Hallway

class Cellar(Scene):

    def __init__(self):
        self.scene = Scene()

    def enter(self):
        dialogue = dedent("""
            You open the door to the cellar. There is a stairway leading downward into the darkness.
            """)
        self.scene.text_roll(dialogue)

        if Scene.stairs == 0:
            print(dedent("""
            Perhaps it's better to first find a light source.
            """))
            return "hallway"

        elif Scene.stairs == True:
            print(dedent("""
            Would you like to proceed? [yes] or [no]
            """))

            while True:
                action = input("> ")

                if action == ("no"):
                    print("\n[Hallway]\n")
                    return "hallway"

                elif action == ("yes"):
                    return "goldroom"

                else:
                    self.scene.unknown()

