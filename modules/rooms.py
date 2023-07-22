from .myimports import *
from modules.scenes import Scene
from modules.death import Death

class Room1(Scene):  #bedroom

    def __init__(self):
        self.scene = Scene()
        self.death = Death()

    def enter(self):

        dialogue = dedent("""
            You enter the bedroom, and notice the window open. It is already pitch-black outside. You spot a
            lantern on the bedside table.
            """)
        self.scene.text_roll(dialogue)

        while True:
            action = input("> ")

            if action == "take lantern" and Scene.cabinet == True:
                print(dedent("""
                You take lantern and begin to head outwards when you hear loud thudding sounds coming from the other
                room. You hurry back downstairs.  -obtained lantern-
                """))
                Scene.stairs = True
                return "hallway"

            elif action == "leave room" or action == "go back" or action == "leave":
                print(dedent("""
                You exit the room.
                """))
                return "stairway"

            elif action == "take lantern":
                print(dedent("""
                As you reach for the lantern and prepare to make your way out, a sudden chill runs down your spine. 
                Before you stands a mysterious figure, draped in a dark hood, effectively obstructing your path. He
                draws a knife. -obtained lantern-
                """))

                while True:
                    action = input("> ")

                    if action == ("jump out window") or action == ("jump window"):
                        print(dedent("""
                        You jump out the open window only to fall and break your legs.

                        - DEAD -
                        """))
                        return "stairway"

                    elif action == ("use lantern"):
                        print(dedent("""
                        For some reason you decide to light the lantern to see your killer before you die. Only to find an old
                        looking guy with a crooked nose and a scar across his face. He lunges at you.

                        - DEAD -
                        """))
                        print(Scene.checkpoint)
                        return self.death.death(Scene.checkpoint)

                    elif action == ("throw lantern"):
                        print(dedent("""
                        You throw the lantern at the dark hooded figure, causing him to stagger backwards and fall down the
                        staircase. You follow suit only to find him already disappeared down below. As you reach the bottom of
                        the stairs you find his knife and a trail of blood towards the front door. You try to open it but it
                        is locked shut.  -obtained knife-
                        """))

                        Scene.stairs = True
                        return "hallway"

                    elif action == ("close door"):
                        print(dedent("""
                        You close the door, holding it shut. You hear the door lock on the other side. Unable to get out you
                        die of starvation.

                        - DEAD -
                        """))
                        return "stairway"

                    else:
                        self.scene.unknown()

            else:
                self.scene.unknown()


    def take_lantern(self):
        
        print(dedent("""
        You take the lantern and turn to head out when a dark hooded figure appears, blocking your path. He
        draws a knife.  -obtained lantern-
        """))

        while True:
            action = input("> ")

            if action == ("jump out window") or action == ("jump window"):
                print(dedent("""
                You jump out the open window only to fall and break your legs.

                - DEAD -
                """))
                return "stairway"

            elif action == ("use lantern"):
                print(dedent("""
                For some reason you decide to light the lantern to see your killer before you die. Only to find an old
                looking guy with a crooked nose and a scar across his face. He lunges at you.

                - DEAD -
                """))
                return "stairway"

            elif action == ("throw lantern"):
                print(dedent("""
                You throw the lantern at the dark hooded figure, causing him to stagger backwards and fall down the
                staircase. You follow suit only to find him already disappeared down below. As you reach the bottom of
                the stairs you find his knife and a trail of blood towards the front door. You try to open it but it
                is locked shut.  -obtained knife-
                """))

                Scene.stairs = True
                return "hallway"

            elif action == ("close door"):
                print(dedent("""
                You close the door, holding it shut. You hear the door lock on the other side. Unable to get out you
                die of starvation.

                - DEAD -
                """))
                return "stairway"

            else:
                self.scene.unknown()


class Room2(Scene):

    def __init__(self):
        self.scene = Scene()

    def enter(self):
        dialogue = dedent("""
            As you enter the pitch-black room, a sudden dread envelops you. Before you can react, an arm emerges 
            from behind, swiftly covering your mouth, cutting off your ability to call for help. A 
            wave of dizziness washes over you, and your vision fades as you gradually lose 
            consciousness.
                          
            - DEAD -
            """)
        self.scene.text_roll(dialogue)
        return "stairway"