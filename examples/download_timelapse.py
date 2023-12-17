from bambu_connect import BambuClient
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your actual details
hostname = os.getenv('HOSTNAME')
access_code = os.getenv('ACCESS_CODE')
serial = os.getenv('SERIAL')

local_path="./timelapses/"

def convert_avi_to_mp4(avi_file_path, output_dir):
    clip = VideoFileClip(avi_file_path)
    output_file_path = os.path.join(output_dir, os.path.basename(avi_file_path).replace('.avi', '.mp4'))
    clip.write_videofile(output_file_path)

def main():
    bambu_client = BambuClient(hostname, access_code, serial)

    # List files on the printer
    files = bambu_client.get_files("/timelapse/", ".avi")
    print(files)

    if (len(files) == 0):
        print("There are no timelapse videos. Select timelapse when printing and they will show up here.")

    bambu_client.download_file(remote_path="/timelapse/" + files[0], local_path=local_path)

    local_file_path = os.path.join(local_path, os.path.basename(files[0]))
    convert_avi_to_mp4(local_file_path, local_path)


if __name__ == "__main__":
    main()