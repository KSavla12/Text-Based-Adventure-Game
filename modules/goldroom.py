from .myimports import *
from modules.scenes import Scene
from modules.attributes import Inventory
from modules.attributes import Health
from modules.attributes import Combat
from modules.death import Death

class GoldRoom(Scene):

    def __init__(self):
        self.scene = Scene()
        self.inventory = Inventory()
        self.combat = Combat().combat
        self.death = Death()

    def enter(self):

        Scene.checkpoint = 'hallway'

        dialogue = dedent("""
            Using your lantern to illuminate the darkness you head down into the cellar where there is a narrow
            corridor carved out in stone. You follow it down a long way until you reach a big room with a pile of
            gold coins in the centre. High up from the spot is a crevice leading up above ground, what looks
            to be a wishing well.

            As you walk towards the centre you hear heavy footsteps coming towards you from across the room. As
            it comes into the light you see a monstrous troll standing before you, welding a big wooden club.

            You prepare for battle.
            """)
        self.scene.text_roll(dialogue)

        while Health.player_hp > 0 and Health.troll_hp > 0:

            time.sleep(0.8)
            print("-" * 31)
            print("Player HP:", Health.player_hp, '----', "Troll HP:", Health.troll_hp)
            print("-" * 31)

            action = input("> ")
            time.sleep(0.8)

            # Health:
            if (action == "water" and 'water' in Inventory.invent):
                print(dedent("""
                Your health has increased by 8.
                """))
                Health.player_hp += 8
                Inventory.invent.remove("water")
                time.sleep(0.8)
                Troll.troll(self)

            elif (action == "snack" and 'snack' in Inventory.invent):
                print(dedent("""
                Your health has increased by 8.
                """))
                Health.player_hp += 8
                Inventory.invent.remove("snack")
                time.sleep(0.8)
                Troll.troll(self)

            elif action == "water" and 'water' != Inventory.invent:
                print(dedent("""
                You have no water left...
                """))

            elif action == "snack" and 'snack' != Inventory.invent:
                print(dedent("""
                You have no snacks left...
                """))

            # Combat:
            elif action == "attack" or action == "hit":
                print(dedent("""
                You stab him with your knife.                           )xxxxx[;;;;;;;;;>
                * You deal
                """), self.combat['Player_attack'], "points of damage.")
                time.sleep(0.8)
                Health.troll_hp -= self.combat['Player_attack']
                if Health.troll_hp < 0:
                    Health.troll_hp = 0
                Troll.troll(self)

            elif action == "throw lantern":        
                print(dedent("""
                You throw your lantern at him in desperation. Is does nothing.
                """))
                time.sleep(0.8)
                Troll.troll(self)

            elif action == "inventory":
                self.inventory.inventory_check()

            else:
                self.scene.unknown()

        # End of Combat:
        print("-" * 31)
        print("Player HP:", Health.player_hp, '----', "Troll HP:", Health.troll_hp)
        print("-" * 31)

        if Health.player_hp <= 0 and Health.troll_hp <= 0:
            print("You killed each other...")
            return self.death.death(self.scene.checkpoint)

        elif Health.player_hp <= 0:
            print("You died")
            return self.death.death(Scene.checkpoint)

        elif Health.troll_hp <= 0:
            print("You win!")
            print("bla bla bla")
            print("TO BE CONTINUED...")
            print("\nPress any key to quit")
            i = input(">")
            quit()


class Troll(object):

    def __init__(self):
        self.scene = Scene()
        self.combat = Combat()
        
    # Combat:
    def troll(self):

        chance = randint(1,3)                          

        if chance <= 2:                       
            #Troll's options:::
            #Troll attack - normal (2 in 3 chance)
            print(dedent("""
            The troll swings it's club at you.                      ====(xxxxxXXXXXX)             
            * You take
            """), self.combat['Troll_attack'], "points of damage." )
            Health.player_hp -= self.combat['Troll_attack']
            if Health.player_hp < 0:
                Health.player_hp = 0

        elif chance == 3:                        
            #Troll attack - hard (1 in 3 chance)
            print(dedent("""
            With both hands the troll slams you with it's club.     ====(xxxxxXXXXXX)*
            * You take
            """), self.combat['Troll_big_attack'], "points of damage!")
            Health.player_hp -= self.combat['Troll_big_attack']
            if Health.player_hp < 0:
                Health.player_hp = 0