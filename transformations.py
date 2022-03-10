import bpy
import random
from math import tan, atan, radians
from mathutils import Euler

def distance(a,b):
    d = a.location - b.location
    for i in range(len(d)):
        d[i] = abs(d[i])        
    return d

def getAngles(camera):
    scene = scene = bpy.context.scene    
    frame = camera.data.view_frame(scene = scene)
    x = abs(frame[0][0])
    y = abs(frame[0][1])
    z = abs(frame[0][2])
    angleX = atan(x/z)
    angleY = atan(y/z)
    return angleX, angleY

def move(obj, cam):
    randY = random.uniform(-1,20)
    obj.location[1] = randY 
    angleX, angleY = getAngles(cam)
    distanceY = distance(obj, cam)[1]
    width  = tan(angleX) * distanceY
    height = tan(angleY) * distanceY
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

def transform(obj, cam):
    rotate(obj)
    scale(obj)
    move(obj,cam)
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)