import os 


def convertYolo(x1,y1,x2,y2, shape):
    x = ((x1 + x2) / 2) / shape[1]
    y = ((y1 + y2) / 2) / shape[0]
    h = abs(y1 - y2) / shape[0]
    w = abs(x2 - x1) / shape[1]
    return x, y, w, h

def distance(a,b):
    d = a.location - b.location
    for i in range(len(d)):
        d[i] = abs(d[i])        
    return d

def init(collections, path):
    if not os.path.exists(path):
        os.mkdir(path)
    names = {}
    ln = len(collections)
    with open(os.path.join(path, 'classes.txt'), 'w') as f:
        for i in range(ln):
            collections[i].hide_render = True
            f.write(collections[i].name)
            names[collections[i].name] = i
            if i != ln -1:
                f.write('\n')
    return names