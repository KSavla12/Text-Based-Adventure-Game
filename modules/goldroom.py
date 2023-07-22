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
            Armed with your trusty lantern, you cautiously descend into the cellar, its dark depths illuminated 
            by the light. A narrow stone corridor stretches before you, leading you deeper underground. You 
            follow the passageway for what feels like an eternity until you finally arrive in a sizable room. In 
            the center lies a captivating sight—a heap of gleaming gold coins. Above, a crevice reveals itself, 
            seemingly a pathway back to the surface resembling a wishing well.

            However, your attention is swiftly diverted as you catch the sound of heavy footsteps resonating 
            across the room. As the source of the sound steps into the light, a monstrous troll emerges, wielding 
            a massive wooden club. 
                
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
            print(dedent("""
            You stand victorious, catching your breath, as the room falls into a silence broken only by your 
            own heartbeat. The pile of gold coins serves as a testament to your triumph over the formidable 
            foe.
            """))
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