import sys
import bpy
from pathlib import Path
import bpy_extras

sys.path.append(r'C:/Users/Roger/Documents/synthetic_dataset')

from transformations import transform

def convertYolo(x1,y1,x2,y2, shape):
    x = ((x1 + x2) / 2) / shape[1]
    y = ((y1 + y2) / 2) / shape[0]
    h = abs(y1 - y2) / shape[0]
    w = abs(x2 - x1) / shape[1]
    return x, y, w, h


def save(obj):
    renderScale = scene.render.resolution_percentage / 100
    width  = int(scene.render.resolution_x * renderScale)
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
    x, y, w, h = convertYolo(p1[0], p1[1], p2[0], p2[1], (height, width))

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

def useObject(obj):
    data = obj.data.copy()
    data.name = obj.data.name
    transform(obj, cam)
    save(obj)
    obj.data = data

if __name__ == '__main__':
    obj   = bpy.context.scene.objects['Suzanne'] 
    cam   = bpy.data.objects['Camera']
    scene = bpy.context.scene
    mat   = obj.matrix_world

    useObject(obj)