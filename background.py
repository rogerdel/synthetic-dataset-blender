import bpy
import random
from transformations import camBox
from camera import adjustResolution, camBox

plane = bpy.context.scene.objects['Plane']
def movePlane():
    plane.location = (0, random.randint(10, 25), 0)

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