import subprocess
import time

def run_blender_command(command):
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def import_bvh(file_path):
    run_blender_command(["C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe", "--background", "--python",
                    "clear_scene.py"])

    run_blender_command(["C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe", "--background", "--python",
                    "import_bvh.py", "--", file_path])


if __name__ == "__main__":
    blend_file_path = r'E:\FF\sign lang easy.blend'
    bvh_file_path = r'E:\OLD DOWNLOADS\sign language\ru fine.bvh'

    run_blender_command(["C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe", blend_file_path])

    time.sleep(5)

    import_bvh(bvh_file_path)
