import subprocess
import os

def render_animation(blend_file_path, output_path, frames=None, resolution=(1920, 1080)):
    """
    Render animation using Blender CLI.

    Args:
        blend_file_path (str): Path to the Blender file (.blend).
        output_path (str): Path where the rendered frames will be saved.
        frames (tuple): Tuple specifying start and end frames to render.
                        If None, it renders all frames.
        resolution (tuple): Tuple specifying the resolution of the rendered frames (width, height).

    Returns:
        None
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Define command to render animation
    cmd = [
        "C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe",
        "-b", blend_file_path,  # Run in background mode
        "-o", os.path.join(output_path, "frame_######.png"),  # Output format and path
        "-E", "BLENDER_EEVEE",  # Render engine (you can change this if needed)
        "--render-output", output_path,  # Render output path
               "-a"  # Render animation
    ]

    # If specific frames are specified, add them to the command
    if frames is not None:
        cmd.extend(["-s", str(frames[0]), "-e", str(frames[1])])

    # Run the Blender CLI command
    subprocess.run(cmd)

def convert_frames_to_video(frame_dir, output_video_path, fps=30, crf=20):
    """
    Convert rendered frames to a video using ffmpeg.

    Args:
        frame_dir (str): Directory containing rendered frames.
        output_video_path (str): Path where the output video will be saved.
        fps (int): Frames per second for the output video.
        crf (int): Constant Rate Factor (quality) for the output video. Range: 0-51. Lower value means better quality.

    Returns:
        None
    """
    ffmpeg_cmd = [
        "ffmpeg",
        "-framerate", str(fps),
        "-i", os.path.join(frame_dir, "frame_%06d.png"),
        "-c:v", "libx264",
        "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        output_video_path
    ]
    subprocess.run(ffmpeg_cmd)

if __name__ == "__main__":

    blend_file_path = r'E:\FF\sign lang easy.blend'
    output_frame_dir = r'E:\CODE SPACE\v2bvh\generated_images\Final'
    output_video_path = r'E:\CODE SPACE\v2bvh'
    frames_range = (1, 10)  # Example: render frames 1 to 250. Set to None to render all frames.

    render_animation(blend_file_path, output_frame_dir, frames_range)


