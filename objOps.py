import bpy

def select(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
 
def delete(obj):
    select(obj)
    bpy.ops.object.delete()