import random

class Space_Body:

    def __init__(self, name, texture, coordinates, scale, all_objects_on_screen):
        self.name = name
        self.texture = texture
        self.coordinates = coordinates
        self.scale = scale

        all_objects_on_screen.append(self)
    

    def change_coordinates(self, offset):
        x_offset = offset[0]
        y_offset = offset[1]
        
        self.coordinates[0] += x_offset
        self.coordinates[1] += y_offset



class Star(Space_Body):

    def __init__(self, coordinates, all_objects_on_screen):

        possible_textures = []
        rand_tex = random.randint(0, len(possible_textures)-1)

        possible_names = []
        rand_name = random.randint(0, len(possible_names)-1)

        super().__init__(possible_names[rand_name], possible_textures[rand_tex], coordinates, [400, 200], all_objects_on_screen)

class Buildable_Space_Body(Space_Body):

    def __init__(self, name, texture, coordinates, scale, all_objects_on_screen):
        super().__init__(name, texture, coordinates, scale, all_objects_on_screen)

class Planet(Buildable_Space_Body):

    def __init__(self, coordinates, all_objects_on_screen):

        possible_textures = ["textures\\space_objects_textures\\planet_textures\\Venus.png",
                             "textures\\space_objects_textures\\planet_textures\\Lava_Planet.png"
                             ]
        rand_tex = random.randint(0, len(possible_textures)-1)

        possible_names = ["Epsilon Eridani b"]
        rand_name = random.randint(0, len(possible_names)-1)



        super().__init__(possible_names[rand_name], possible_textures[rand_tex], coordinates, [1500, 750], all_objects_on_screen)


class Asteroid(Buildable_Space_Body):

    def __init__(self, coordinates, all_objects_on_screen):

        possible_textures = []
        rand_tex = random.randint(0, len(possible_textures)-1)

        possible_names = []
        rand_name = random.randint(0, len(possible_names)-1)

        super().__init__(possible_names[rand_name], possible_textures[rand_tex], coordinates, [250, 125], all_objects_on_screen)