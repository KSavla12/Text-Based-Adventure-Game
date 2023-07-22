from .myimports import *
from modules.scenes import Scene


class Stairway(Scene):

    def __init__(self):
        self.scene = Scene()

    def intro(self):

        Scene.checkpoint = 'stairway'

        dialogue = dedent("""
            As you reach the top of the staircase, a flicker of movement catches your attention. 
            Out of the corner of your eye, you witness the door to your left abruptly shutting, without a sound.              
            Was it a figment of your imagination, or something more unsettling? The door is labelled 
            "Storage Room". There is an old cabinet beside it and ahead of you lies what looks to be a bedroom.
            """)
        self.scene.text_roll(dialogue)
        Scene.intro_stairway = True
        return Stairway.enter(self)

    def enter(self):
        if Scene.intro_stairway == False:
            return Stairway.intro(self)

        while True:
            action = input("> ")

            if action == ("bedroom") or action == ("enter bedroom"):
                return "room1"

            elif (action == "left room" or action == "storage room") and Scene.cabinet == False:
                return "room2"

            elif (action == ("move cabinet") or action == ("push cabinet") or action == ("block door")) and Scene.cabinet == False:
                print(dedent("""
                You move the cabinet blocking the room from whatever is in there from coming out. You find a knife
                inside the cabinet. This might come in handy.  -obtained knife-
                """))
                Scene.cabinet = True

            else:
                self.scene.unknown()

