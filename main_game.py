import scenes


class Engine(object):
    def __init__(self, the_map):
        self.the_map = the_map

    def play(self):
        current_location = self.the_map.opening_scene()
        final_location = self.the_map.next_scene('fuck')

        while current_location != final_location:
            next_scene = current_location.enter()
            current_location = self.the_map.next_scene(next_scene_name)

class Locations(object):

    areas = {
    'town' : scenes.opening(),
    'first_forest' : scenes.forest(),
    'boaty_boat' : scenes.boat(),
    'hole' : scenes.cave(),
    'swampy_swamp' : scenes.swamp(),
    'plains' : scenes.field(),
    'kingdom' : scenes.castle()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        holder = Locations.areas.get(scene_name)
        return holder

    def opening_scene(self):
        return self.next_scene(self.start_scene)

the_map = Locations('town')
play_game = Engine(the_map)
play_game.play()
