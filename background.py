import bpy
import random
from transformations import camBox
from camera import adjustResolution, camBox
from data import background_max_y, background_min_y

plane = bpy.context.scene.objects['Plane']
def movePlane():
    plane.location = (0, random.randint(background_min_y, background_max_y), 0)

def adjustBackground(img):
    img = bpy.data.images[img.name]
    adjustResolution(img)
    width, height = camBox(plane)    
    width  = width  * 2
    height = height * 2
    plane.dimensions = (width, 0, height)


def changeBackground(path):
    movePlane()
    image = bpy.data.images.load(path)
    bpy.data.materials['Background'].node_tree.nodes['Image Texture'].image = image
    adjustBackground(image)
    return image