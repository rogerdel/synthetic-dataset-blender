import bpy
import random
from math import atan, tan
cam =  bpy.data.objects['Camera']

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

def camBox(obj):
    angleX, angleY = getAngles(cam)
    distanceY = distance(obj, cam)[1]
    width  = tan(angleX) * distanceY
    height = tan(angleY) * distanceY
    return width, height

def adjustResolution(img):
    width, height = img.size
    bpy.context.scene.render.resolution_x = width
    bpy.context.scene.render.resolution_y = height
    bpy.context.scene.render.resolution_percentage = random.randint(10, 50) if width > 3000 or height > 3000 else 100
