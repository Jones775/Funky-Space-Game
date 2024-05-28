
class Spaceship():

    def __init__(self, name, damage, hp, velocity, texture, coordinates, scale, all_objects_on_screen):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.velocity = velocity
        self.texture = texture
        self.coordinates = coordinates
        self.scale = scale


        all_objects_on_screen.append(self)


    def die():
        pass

    def attack(target):
        pass

    def loose_hp():
        pass




class Cargo_Vessel(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Cargo Vessel", 0, 1, 30, "textures\\spaceship_textures\\Cargo_Vessel.png", coordinates, [200,100], all_objects_on_screen)
        



class Small_Starfighter(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Small Starfighter", 5, 3, 50, "textures\\spaceship_textures\\Small_Starfighter.png", coordinates, [200,100], all_objects_on_screen)


class Battle_Cruiser(Spaceship):

    def __init__(self, coordinates):
        super().__init__("Battle Cruiser", 5, 20, 35)
        self.texture = "textures\\spaceship_textures\\Battle_Cruiser.png"
        self.coordinates = coordinates

class Blockade_Runner(Spaceship):

    def __init__(self, coordinates):
        super().__init__("Blockade Runner", 5, 40, 50)
        self.texture = "Bitte Pfad der Textur angeben"
        self.coordinates = coordinates

class Battle_Ship(Spaceship):

    def __init__(self, coordinates):
        super().__init__("Battle Ship", 10, 60, 20)
        self.texture = "Bitte Pfad der Textur angeben"
        self.coordinates = coordinates

class Carrier_Ship(Spaceship):

    def __init__(self, coordinates, ships):
        super().__init__("Carrier Ship", 7, 60, 10)
        self.texture = "textures\\spaceship_textures\\Carrier_Ship.png"
        self.coordinates = coordinates
        self.ships = ships

    def deploy_spaceship():
        pass

class Great_Battleship(Spaceship):

    def __init__(self, coordinates, ships):
        super().__init__("Great Battleship", 20, 200, 5)
        self.texture = "Bitte Pfad der Textur angeben"
        self.coordinates = coordinates
        self.ships = ships

    def deploy_spaceships():
        pass