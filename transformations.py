import bpy
import random
from math import radians
from mathutils import Euler
from objOps import select
from camera import camBox
from data import scale_min, scale_max, minrot, maxrot, prob_roate, prob_scale

def move(obj):
    maxY = bpy.context.scene.objects['Plane'].location[1] - obj.dimensions[1]
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
    if random.random() < prob_roate:
        rx = radians(random.randint(minrot[0], maxrot[0]))
        ry = radians(random.randint(minrot[1], maxrot[1]))
        rz = radians(random.randint(minrot[2], maxrot[2])) 
        obj.rotation_euler = Euler((rx, ry, rz), 'XYZ')
    
def scale(obj):
    if random.random() < prob_scale:
        scale = random.uniform(scale_min, scale_max)
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