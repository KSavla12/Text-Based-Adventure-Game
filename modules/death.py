from modules.scenes import Scene
from modules.attributes import Inventory
from modules.attributes import Health

class Death(object):

    def __init__(self):
        self.scene = Scene()

    def death(self, checkpoint):
        print("GAME OVER")

        # Reset variables
        Health.player_hp = 15
        Health.troll_hp = 15

        if checkpoint == 'hallway':
            # print("##########")
            Inventory.invent.clear()
            Inventory.stock.clear()
            Inventory.stock = ['water', 'snack']
            return Scene.checkpoint
        
        else:
            return Scene.checkpoint