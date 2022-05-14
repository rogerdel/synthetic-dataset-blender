# Initial data
images_per_class = 1000
filenameSize     = 10
saveDir          = 'D:/dataset_shyntethic'
imgDir           = 'D:/Devs/python/images/background'
prob_many_objs   = 0.3
prob_add_obj     = 0.5

# transformation
# scale
prob_scale       = 0.7
scale_min        = 1
scale_max        = 1.5

# rotation (x, y, z) between -360 and 360
prob_roate       = 0.9
minrot           = [-80, 0, 0]
maxrot           = [80, 360, 360]

# background
background_min_y = 0
background_max_y = 6

objData = {
    'bag': {
        'garbagebags': 0.1,
        'transparent bag': 0.7
    },
    'bottle': {
        'sameColorProb': 0.9,
        'Plastic_transparent': 0.3,
        'lid': 1,
        'label': 1,
        'inner label': 0
    },
    'container': {
        'Plastic_transparent': 0.005,
    },
    'cup': {
        'Plastic_transparent': 0.005
    },
    'gloves': {
        'gloves': 0.8,
        'colors' : [[0.238398, 0.341915, 0.904661], [0.208637, 0.558341, 0.930111], [0.027321, 0.114435, 0.327778], [0.871367, 0.83077, 0.708376]]
    },
    'spoon': {
        'spoon': 0.5,
    },
    'straw': {
        'straw': 1,
    }
}
