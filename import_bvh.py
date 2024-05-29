import bpy
import sys

# Get the BVH file path from command line arguments
bvh_file_path = sys.argv[sys.argv.index("--") + 1]

# Import BVH file
bpy.ops.import_anim.bvh(filepath=bvh_file_path)
