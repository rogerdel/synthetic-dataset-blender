# Initial data
images_per_class = 1
filenameSize     = 10
saveDir          = 'E:/Devs/Python/readyolo/dataset/'
imgDir           = 'C:/Users/Roger/Documents/Backgrounds'
prob_many_objs   = 0.4
prob_add_obj     = 0.5

# transformation
# scale
prob_scale       = 0.7
scale_min        = 1
scale_max        = 2

# rotation (x, y, z) between -360 and 360
prob_roate       = 0.9
minrot           = [-90, 0, -90]
maxrot           = [90, 360, 90]

# background
background_min_y = 5
background_max_y = 15