import scenes

class Engine(object):

    def __init__(self, start):
        self.start = start

    def play(self):
        current_scene = self.scene_map.enter()
        current_scene.enter()

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Map(object):
    scenes = {
    'town' : scenes.opening(),
    'first_forest' : scenes.forest(),
    'boaty_boat' : scenes.boat(),
    'hole' : scenes.cave(),
    'swampy_swamp' : scenes.swamp(),
    'plains' : scenes.field(),
    'kingdom' : scenes.castle()
    }
