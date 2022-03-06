import sys
import bpy
from pathlib import Path
import random
import bpy_extras
from mathutils import Euler, Vector
from math import radians, tan, atan

sys.path.append(r'.importer.py')


obj = bpy.context.scene.objects['Suzanne']
cam = bpy.data.objects['Camera']
scene = bpy.context.scene
mat = obj.matrix_world

def distance(a,b):
    d = a.location - b.location
    for i in range(len(d)):
        d[i] = abs(d[i])        
    return d

def convert2(x1,y1,x2,y2, shape):
    x = ((x1 + x2) / 2) / shape[1]
    y = ((y1 + y2) / 2) / shape[0]
    h = abs(y1 - y2) / shape[0]
    w = abs(x2 - x1) / shape[1]
    return x, y, w, h


def getAngles(camera):    
    frame = camera.data.view_frame(scene = scene)
    x = abs(frame[0][0])
    y = abs(frame[0][1])
    z = abs(frame[0][2])
    angleX = atan(x/z)
    angleY = atan(y/z)
    return angleX, angleY

def save():
    renderScale = scene.render.resolution_percentage / 100
    width = int(scene.render.resolution_x * renderScale)
    height = int(scene.render.resolution_y * renderScale)
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

    # Coordenates dont exceed the image
    p1 = (max(p1[0], 0), max(p1[1], 0))
    p2 = (min(p2[0], width), min(p2[1], height))

    print(p1,p2)
    x, y, w, h = convert2(p1[0], p1[1], p2[0], p2[1], (height, width))

    print(x, y, w, h)

    bpy.context.scene.render.filepath = 'E:/Devs/Python/readyolo/monkey.jpg'
    with open ('E:/Devs/Python/readyolo/monkey.txt', 'w') as f:
        f.write(f'0 {x} {y} {w} {h}')
        
    bpy.ops.render.render(write_still = True)

def move(obj):        
    data = obj.data.copy()
    data.name = obj.data.name
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
    obj.location = Vector((randX, randY, randZ))

    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)     
    save()
    obj.data = data
        
def rotate(obj):
    data = obj.data.copy()
    data.name = obj.data.name 
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
    obj.data = data

    
def scale(obj):
    data = obj.data.copy()
    data.name = obj.data.name
    scale = random.uniform(0.1, 1.5)
    scl = [scale for _ in range(3)]
    obj.scale = scl
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    save()    
    obj.data = data

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


if __name__ == '__main__':
    # move(obj)
    show()