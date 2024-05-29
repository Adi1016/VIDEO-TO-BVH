import bpy

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='ARMATURE')
bpy.ops.object.delete()
