import scenes

class Map(object):

    # scenes = {
    # 'town' : opening(),
    # 'first_forest' : forest(),
    # 'boaty_boat' : boat(),
    # 'hole' : cave(),
    # 'swampy_swamp' : swamp(),
    # 'plains' : field(),
    # 'kingdom' : castle()
    # }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# a_map = Map('town')
# a_game = Engine(a_map)
# a_game.play()
