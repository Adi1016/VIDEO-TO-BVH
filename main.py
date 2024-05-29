import subprocess

def run_blender(blender_executable, blender_script, rokoko, blender, render):
    cmd = [
        blender_executable,
        "--python", blender_script,
        "--python", rokoko,
        "--python", blender,
        "--python", render,
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    blender_executable = r"C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe" # Use a raw string here
    blender_script = r"E:\CODE SPACE\v2bvh\blender_script.py"  # Use a raw string here
    rokoko = r"E:\CODE SPACE\v2bvh\rokoko.py"
    blender = r"E:\CODE SPACE\v2bvh\blender.py"
    render = r"E:\CODE SPACE\v2bvh\render.py"  # Align this with other variable assignments
    run_blender(blender_executable, blender_script, rokoko, blender, render)
