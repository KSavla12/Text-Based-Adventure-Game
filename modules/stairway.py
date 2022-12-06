from .myimports import *
from modules.scenes import Scene


class Stairway(Scene):

    def __init__(self):
        self.scene = Scene()

    def intro(self):

        Scene.checkpoint = 'stairway'

        dialogue = dedent("""
            As you reach to the top of the staircase from the corner of your eye you catch a sudden glimpse of the
            door to your left close shut without a sound. Was that just your imagination? The door is labelled 
            "Storage Room". There is an old cabinet beside it and another room of a bedroom lies in front of you.
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

            elif action == (("left room") or action == ("storage room")) and Scene.cabinet == False:
                return "room2"

            elif (action == ("move cabinet") or action == ("push cabinet") or action == ("block door")) and Scene.cabinet == False:
                print(dedent("""
                You move the cabinet blocking the room from whatever is in there from coming out. You find a knife
                inside the cabinet. This might come in handy.  -obtained knife-
                """))
                Scene.cabinet = True

            else:
                self.scene.unknown()

