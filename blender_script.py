import bpy

# Set the file paths
blend_file_path = "E:\\FF\\sign lang easy.blend"
bvh_file_path = "E:\\OLD DOWNLOADS\\sign language\\ru fine.bvh"

# Open the Blender file
bpy.ops.wm.open_mainfile(filepath=blend_file_path)

# Import BVH file
bpy.ops.import_anim.bvh(filepath=bvh_file_path)

#
bpy.ops.wm.context_set_int(data_path="area.type", value=4)
bpy.ops.screen.header()