from .myimports import *

class Scene(object):

    intro_house = False
    intro_hallway = False
    intro_stairway = False

    cabinet = False
    stairs = False

    checkpoint = 'house'

    def enter(self):
        print("Will just act as inheritance override.")

        if action == ("hint"):
            print("help")

    def text_roll(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

    def unknown(self):
        print("\nI do not understand\n")


