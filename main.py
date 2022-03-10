from re import X
import sys
import bpy
from pathlib import Path
import bpy_extras
import numpy as np
import time 

sys.path.append(r'C:/Users/Roger/Documents/synthetic_dataset')

from transformations import transform, move, distance

def convertYolo(x1,y1,x2,y2, shape):
    x = ((x1 + x2) / 2) / shape[1]
    y = ((y1 + y2) / 2) / shape[0]
    h = abs(y1 - y2) / shape[0]
    w = abs(x2 - x1) / shape[1]
    return x, y, w, h

def boundingBox(obj, yoloFormat = False):
    renderScale = scene.render.resolution_percentage / 100
    width  = int(scene.render.resolution_x * renderScale)
    height = int(scene.render.resolution_y * renderScale)
    mat   = obj.matrix_world
    
    x, y, _ = bpy_extras.object_utils.world_to_camera_view(scene, cam, obj.data.vertices[0].co)
    left = right = x
    top = bottom = y

    for i in obj.data.vertices:
        glob = mat @ i.co
        x, y, _  = bpy_extras.object_utils.world_to_camera_view(scene, cam, glob)
        left = min(left, x)
        right = max(right, x)
        top = max(top, y)
        bottom = min(bottom, y)

    p1 = (int(left * width), height - int(top *  height))
    p2 = (int(right * width), height - int(bottom * height))  
   # if coordenates exceed the frame then corop the boundingBox
    p1 = (max(p1[0], 0), max(p1[1], 0))
    p2 = (min(p2[0], width), min(p2[1], height))
    if yoloFormat:
        return convertYolo(p1[0], p1[1], p2[0], p2[1], (height, width))
    return p1,p2 

def save(obj):
    x, y, w, h = boundingBox(obj, True)
    bpy.context.scene.render.filepath = 'E:/Devs/Python/readyolo/monkey.jpg'
    with open ('E:/Devs/Python/readyolo/monkey.txt', 'w') as f:
        f.write(f'0 {x} {y} {w} {h}')        
    bpy.ops.render.render(write_still = True)

def changeBackground(path):
    image = bpy.data.images.load(path)
    bpy.data.materials['Background'].node_tree.nodes['Image Texture'].image = image


def renderMany():
    directory = Path('C:/Users/Roger/Documents/Backgrounds')
    outputPath = Path('E:/images')
    i = 0
    for f in directory.iterdir():
        changeBackground(str(f))
        bpy.context.scene.render.filepath = str(outputPath / f'{str(i).zfill(6)}.png')
        bpy.ops.render.render(write_still = True)
        i += 1
def intersersct(obj1,obj2):
    # Boundingbox the objects
    o1p1, o1p2 = boundingBox(obj1)
    o2p1, o2p2  = boundingBox(obj2)
    return o1p1[0] < o2p2[0] and o1p2[0] > o2p1[0] and o1p1[1] < o2p2[1] and o1p2[1] > o2p1[1] 

def useObject(object):
    obj = object.copy()
    obj.data = object.data.copy()
    bpy.context.scene.collection.objects.link(obj)
    obj = bpy.context.scene.objects[obj.name]
    obj.hide_render = False   
    transform(obj, cam)
    save(obj)
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.object.delete()
    

if __name__ == '__main__':
    cam   = bpy.data.objects['Camera']
    scene = bpy.context.scene

    objs =[i.name for i in bpy.data.collections['Objects'].all_objects]
    
    for i in objs:
        bpy.context.scene.objects[i].hide_render = True
    
    for i in objs:
        obj = bpy.context.scene.objects[i]
        useObject(obj) 