import bpy
import random
from math import tan, atan, radians
from mathutils import Euler

cam = bpy.data.objects['Camera']

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
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        
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
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    
def scale(obj):
    scale = random.uniform(0.1, 1.5)
    scl = [scale for _ in range(3)]
    obj.scale = scl
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
