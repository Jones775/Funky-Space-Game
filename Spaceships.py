
class Destination():
    
    def __init__(self, coordinates, ship, all_objects_on_screen):
        self.coordinates = coordinates
        self.scale = [100, 50]
        #The ship this Destination belongs to
        self.ship = ship
        self.texture = "textures\\other_textures\\Destination_peaceful.png"
        

        all_objects_on_screen.append(self)

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

    def fly(self, destination, all_objects_on_screen):

        if isinstance(destination, Destination):
            pass
            #TODO Here you should move the ship towards the destination 
        else:

            return Destination(destination, self, all_objects_on_screen)




    def change_coordinates(self, offset):
        x_offset = offset[0]
        y_offset = offset[1]
        
        self.coordinates[0] += x_offset
        self.coordinates[1] += y_offset




class Cargo_Vessel(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Cargo Vessel", 0, 1, 30, "textures\\spaceship_textures\\Cargo_Vessel.png", coordinates, [100,50], all_objects_on_screen)
        



class Small_Starfighter(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Small Starfighter", 5, 3, 50, "textures\\spaceship_textures\\Small_Starfighter.png", coordinates, [100,50], all_objects_on_screen)


class Battle_Cruiser(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Battle Cruiser", 5, 20, 35, "textures\\spaceship_textures\\Battle_Cruiser.png", coordinates, [200,100], all_objects_on_screen)

class Blockade_Runner(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen):
        super().__init__("Blockade Runner", 5, 40, 50, "textures\\spaceship_textures\\Blockade_Runner.png", coordinates, [150, 75], all_objects_on_screen)
        

class Battle_Ship(Spaceship):

    def __init__(self, coordinates):
        super().__init__("Battle Ship", 10, 60, 20)
        self.texture = "Bitte Pfad der Textur angeben"
        self.coordinates = coordinates

class Carrier_Ship(Spaceship):

    def __init__(self, coordinates, all_objects_on_screen, ships):
        super().__init__("Carrier Ship", 7, 60, 10, "textures\\spaceship_textures\\Carrier_Ship.png", coordinates, [400, 200], all_objects_on_screen)
        self.ships = ships

    def deploy_spaceships():
        pass

class Great_Battleship(Spaceship):

    def __init__(self, coordinates, ships):
        super().__init__("Great Battleship", 20, 200, 5)
        self.texture = "Bitte Pfad der Textur angeben"
        self.coordinates = coordinates
        self.ships = ships

    def deploy_spaceships():
        pass