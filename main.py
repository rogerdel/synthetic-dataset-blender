import sys
import time
import bpy
import random
import os
import string

sys.path.append(r'C:/Users/Roger/Documents/synthetic_dataset')
from transformations import transform
from objOps import delete
from background import changeBackground
from camera import boundingBox, changeFocalLength
from utils import init, progress
from data import filenameSize, saveDir, imgDir, images_per_class, prob_many_objs, prob_add_obj
from color import shiftColor

def save(objs, colls):
    filename = randomFilename()
    bpy.context.scene.render.filepath = f'{filename}'
    with open (f'{filename}.txt', 'w') as f:
        ln = len(objs)
        for i in range(len(objs)):
            x, y, w, h = boundingBox(objs[i], True)
            f.write(f'{names[colls[i]]} {x} {y} {w} {h}')
            if i != ln - 1 :
                f.write('\n')  
    bpy.ops.render.render(write_still = True)

def intersersct(obj1,obj2):
    # Boundingbox the objects
    o1p1, o1p2 = boundingBox(obj1)
    o2p1, o2p2  = boundingBox(obj2)
    return o1p1[0] < o2p2[0] and o1p2[0] > o2p1[0] and o1p1[1] < o2p2[1] and o1p2[1] > o2p1[1] 

def randomFilename():
    letters = string.ascii_lowercase + string.ascii_uppercase
    name = ''.join(random.choice(letters) for _ in range(filenameSize))
    return f'{saveDir}/{name}'
        
def chooseObjs(collection):
    collectionsNames = [collection.name]
    renderObjs = [random.choice(collection.all_objects).name]
    if random.random() < prob_many_objs:
        for i in collections:
            if random.random() < prob_add_obj:
                renderObjs.append(random.choice(i.all_objects).name)
                collectionsNames.append(i.name)
    return renderObjs, collectionsNames

def useCollection(collection):
    changeFocalLength()
    renObjs, colls = chooseObjs(collection)
    objects = []
    materials = []
    global imgIndex
    img = changeBackground(imgs[imgIndex])
    imgIndex = (imgIndex + 1) % len(imgs)
    for i in renObjs:
        objc = bpy.context.scene.objects[i].copy()
        objc.data = bpy.context.scene.objects[i].data.copy()
        bpy.context.scene.collection.objects.link(objc)
        objc.hide_render = False
        transform(objc)
        materials += shiftColor(objc, bpy.context.scene.objects[i].users_collection[0].name) 
        b = True
        for j in range(100):
            for o in objects:
                b = b and not intersersct(o, objc)            
            if b:
                objects.append(objc)
                break
            elif j != 99:
                objc.data = bpy.context.scene.objects[i].data.copy()
                transform(objc)
                b = True
        if not b:
            delete(objc)
    save(objects, colls)
    for obj in objects:
        delete(obj)
    bpy.data.images.remove(img)
    for material in materials:
        bpy.data.materials.remove(material)

def main(n):
    for i in collections:
        for j in range(n):
            useCollection(i)
            progress(i.name, j+1, n)
        progress(i.name)

if __name__ == '__main__':
    startTime = time.time()
    imgIndex       = 0
    imgs           = [os.path.join(imgDir, i) for i in os.listdir(imgDir)]
    collections    = bpy.data.collections['Objects'].children
    names          = init(collections, saveDir)
    main(images_per_class)
    totalTime =  time.time() - startTime    
    print('Total time:', totalTime)