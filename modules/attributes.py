from random import randint

class Health(object):

    troll_hp = 15
    player_hp = 15


class Inventory(object):

    stock = ['water', 'snack']
    invent = []

    def inventory_check(self):
        print("\nCurrent inventory:")
        for i in Inventory.invent:
            print(i)


class Combat(object):

    combat = {
    'Troll_big_attack' : 6,
    'Troll_attack' : randint(3, 5),
    'Player_attack' : randint(3, 5)
    }            