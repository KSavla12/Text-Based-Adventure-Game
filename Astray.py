from modules.house import House
from modules.hallway import Hallway
from modules.cellar import Cellar
from modules.kitchen import Kitchen
from modules.goldroom import GoldRoom
from modules.stairway import Stairway
from modules.rooms import Room1, Room2
from modules.scenes import Scene

class Map(object):

    scenes = {                                
        'house': House(),
        'hallway': Hallway(),
        'cellar': Cellar(),
        'kitchen': Kitchen(),
        'goldroom': GoldRoom(),
        'stairway': Stairway(),
        'room1': Room1(),
        'room2': Room2(),
        }

    title = {                                
        'hallway': "\n[Hallway]",
        'cellar': "\n[Cellar]",
        'kitchen': "\n[Kitchen]",
        'stairway': "\n[Upstairs]",
        'room1': "\n[Bedroom]",
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)     
        title1 = Map.title.get(scene_name)
        if title1 == None:
            pass
        else:
            print(title1)
        return val                           

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')     # currently not in use

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene                  # currently not in use
        current_scene.enter()



a_map = Map('house')    #Set a_map to an instance of class Map
a_game = Engine(a_map)  #Set a_game to an instance of class Engine
a_game.play()           #From a_game get the play function
