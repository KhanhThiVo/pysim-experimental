import sys
from direct.showbase.ShowBase import ShowBase

"""
class Application(ShowBase):

    def __init__(self):
        # Notice that you must not call ShowBase.__init__ (or super), the
        # render pipeline does that for you. If this is unconvenient for you,
        # have a look at the other initialization possibilities.

        # Insert the pipeline path to the system path, this is required to be
        # able to import the pipeline classes. In case you placed the render
        # pipeline in a subfolder of your project, you have to adjust this.
        sys.path.insert(0, "../../")
        sys.path.insert(0, "../../RenderPipeline")

        # Import the main render pipeline class
        from rpcore import RenderPipeline

        # Construct and create the pipeline
        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        # Done! You can start setting up your application stuff as regular now.

        from rpcore import SpotLight
        my_light = SpotLight()
        # set desired properties, see below
        my_light.color = (0, 0.5, 0)
        my_light.pos = (5, 5, 5)
        my_light.color = (0.2, 0.6, 1.0)
        my_light.energy = 1.0
        my_light.ies_profile = self.render_pipeline.load_ies_profile("x_arrow.ies")
        my_light.casts_shadows = True
        my_light.shadow_map_resolution = 512
        my_light.near_plane = 0.2
        self.render_pipeline.add_light(my_light)
"""
import sys
from direct.showbase.ShowBase import ShowBase

# Insert the pipeline path to the system path, this is required to be
# able to import the pipeline classes. In case you placed the render
# pipeline in a subfolder of your project, you have to adjust this.
sys.path.insert(0, "../../RenderPipeline")
sys.path.insert(0, "../../")

# Import render pipeline classes
from rpcore import RenderPipeline

# Construct and create the pipeline
render_pipeline = RenderPipeline()
#render_pipeline.pre_showbase_init()

# Construct and create the ShowBase


#from ursina import *
import ursina as urs
from ursina.shaders import basic_lighting_shader
#from ursina.prefabs import Button

#from ursina.prefabs.first_person_controller import FirstPersonController

# create a window
app = urs.Ursina()


urs.window.title = 'Ball on Beam'                # The window title
#urs.window.size = 5
urs.window.borderless = False               # Show a border
urs.window.fullscreen = False               # Do not go Fullscreen
urs.window.exit_button.visible = False      # Do not show the in-game red X that loses the window
urs.window.fps_counter.enabled = True
#camera.orthographic = False
urs.EditorCamera()
# adding some light
#urs.Light(type='directional', color=(0.3,0.3,0.3,1), direction=(1,1,1))
# most things in ursina are Entities. An Entity is a thing you place in the world.
# you can think of them as GameObjects in Unity or Actors in Unreal.
# the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# ursina includes some basic models like 'cube', 'sphere' and 'quad'.

# the next parameter tells us the model's color should be orange.

# 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# in ursina, positive x is right, positive y is up, and positive z is forward.

r_ball=0.1  # ball radius [m]
m_beam=3.0  # beam mass [kg]
l_beam=2.0  # beam length [m]
d_beam=0.1  # beam thickness [m]
#x = float(self.state[0])


beam = urs.Entity(model='cube', color=urs.color.green, scale=(l_beam, d_beam, 2*d_beam), shader=basic_lighting_shader)

ball = urs.Entity(model='sphere', color=urs.color.red, scale=(r_ball, r_ball, r_ball), position=(0, d_beam/2.0 + r_ball, 0), shader=basic_lighting_shader)

#txt = urs.Text(text="some text", origin=(.1,-.5))
# create a function called 'update'.
# this will automatically get called by the engine every frame.

def update():

    #beam.x += held_keys['d'] * time.dt
    #beam.x -= held_keys['a'] * time.dt
    if beam.x > 1:
        beam.rotation_z -= urs.time.dt * 100  # Rotate every time update is called
    else:
        beam.rotation_z += 1 *1
        #txt.text += " 1"
    #beam.animate_rotation(0.1)

    #ball.x += held_keys['d'] * time.dt
    #ball.x -= held_keys['a'] * time.dt

    #ball.y += time.dt * 1  # Rotate every time update is called


    # this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.
#base = ShowBase()
#render_pipeline.create(app)

#Application().run()
# start running the game
app.run()

#vr = VideoRecorder()



"""
from ursina import *                    # this will import everything we need from ursina with just one line.
import random                           # Import the random library

random_generator = random.Random()      # Create a random number generator
texoffset = 0.0                         # define a variable that will keep the texture offset
texoffset2 = 0.0                        # define a variable that will keep the texture offset

def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 5        # Rotate all the cubes every time update is called
    if held_keys['q']:                          # If q is pressed
        camera.position += (0, time.dt, 0)      # move up vertically
    if held_keys['a']:                          # If a is pressed
        camera.position -= (0, time.dt, 0)      # move down vertically

    global texoffset                            # Inform we are going to use the variable defined outside
    global texoffset2                           # Inform we are going to use the variable defined outside
    texoffset += time.dt * 0.2                  # Add a small number to this variable
    setattr(cube, "texture_offset", (0, texoffset))    # Assign as a texture offset
    texoffset2 += time.dt * 0.3                        # Add a small number to this variable
    setattr(cube2, "texture_offset", (0, texoffset2))  # Assign as a texture offset

    if mouse.hovered_entity == cube:
        info.visible = True
    else:
        info.visible = False


def input(key):
    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        cube.color = color.rgb(red, green, blue)

    if key == 'c':
        x = random_generator.random() * 10 - 5     # Value between -5 and 5
        y = random_generator.random() * 10 - 5     # Value between -5 and 5
        z = random_generator.random() * 10 - 5     # Value between -5 and 5
        s = random_generator.random() * 1          # Value between 0 and 1
        newcube = Entity(parent=cube, model='cube', color=color.white, position=(x, y, z), scale=(s,s,s), texture="crate")
        cubes.append(newcube)
        '''Create another child cube and add it to the list but using the newcube as the parent, keep the same colour, make it smaller'''
        childcube = Entity(parent=newcube, model='cube', color=color.white, position=(1, 0, 0), scale=(s/2, s/2, s/2), texture="crate")
        cubes.append(childcube)

app = Ursina()

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Go Fullscreen
window.exit_button.visible = False      # Show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

cubes = []                              # Create the list
cube = Entity(model='cube', color=color.white, scale=(2,6,2), texture="waterfall", collider="box")
cube2 = Entity(model='cube', color=color.rgba(255,255,255,128), scale=(2.5,6,2.5), texture="waterfall")
cubes.append(cube)                      # Add the cube to the list
cubes.append(cube2)                     # Add the cube to the list

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="A powerful waterfall roaring on the mountains")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = False                    # Do not show this text

app.run()                               # opens a window and starts the game.
"""

