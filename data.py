# Initial data
images_per_class = 2
filenameSize     = 10
saveDir          = 'E:/Devs/Python/readyolo/dataset/'
imgDir           = 'C:/Users/Roger/Documents/Backgrounds'
prob_many_objs   = 0.4

# transformation
# scale
prob_scale       = 0.9
scale_min        = 0.5
scale_max        = 1.5

# rotation (x, y, z) between -360 and 360
prob_roate       = 0.9
minrot           = [-90, 0, -90]
maxrot           = [90, 360, 90]

# background
background_min_y = 5
background_max_y = 30