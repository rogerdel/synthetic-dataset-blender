import bpy
import random
from math import radians
from mathutils import Euler
from objOps import select
from camera import camBox

def move(obj):
    maxY = bpy.context.scene.objects['Plane'].location[1]
    randY = random.uniform(-1, maxY)
    obj.location[1] = randY 
    width, height = camBox(obj)
    owidth, _, oheight = obj.dimensions    
    owidth /= 2
    oheight /= 2
    x = width - owidth
    z = height - oheight
    randX = random.uniform(-x, x)
    randZ = random.uniform(-z , z)
    obj.location = (randX, randY, randZ)
        
def rotate(obj): 
    if random.random() < 0.9:
        rx = radians(random.randint(0, 360))
        ry = radians(random.randint(0, 360))
        rz = radians(random.randint(0, 360)) 
    else:
        rx = 0
        ry = 0
        rz = 0
    obj.rotation_euler = Euler((rx, ry, rz), 'XYZ')
    
def scale(obj):
    scale = random.uniform(0.1, 1.5)
    scl = [scale for _ in range(3)]
    obj.scale = scl

def transform(obj):
    rotate(obj)
    scale(obj)
    select(obj)
    bpy.ops.object.transform_apply(rotation=True, scale=True)
    move(obj)
    select(obj)
    bpy.ops.object.transform_apply(location=True)