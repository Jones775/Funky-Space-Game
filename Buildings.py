

class Building:

    def __init__(self, name, hp, texture, coordinates, scale):
        self.name = name
        self.hp = hp
        self.texture = texture
        self.coordinates = coordinates
        self.scale = scale
    
    def loose_hp():
        pass

class Shipyard(Building):

    def __init__(self):
        super().__init__("Shipyard", 60)

    def build_ship():
        pass

    def open_dialogue():
        pass


class Mine(Building):

    def __init__(self):
        super().__init__("Mine", 40)

    def produce_ressource():
        pass

class Headquarter(Building):

    def __init__(self):
        super().__init__("Headquarter", 300)


class Base(Building):

    def __init__(self, damage):
        super().__init__("Base", 50, 10)

