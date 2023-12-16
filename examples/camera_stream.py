from bambu_connect import BambuClient
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your actual details
hostname = os.getenv('HOSTNAME')
access_code = os.getenv('ACCESS_CODE')
serial = os.getenv('SERIAL')
output_file = "latest_frame.jpg"


def save_latest_frame(img):
    """Save the latest frame to a file."""
    with open(output_file, "wb") as f:
        f.write(img)


def main():
    bambu_client = BambuClient(hostname, access_code, serial)

    try:
        print("Starting camera stream...")
        bambu_client.start_camera_stream(save_latest_frame)

        # Run indefinitely until manually stopped
        input("Press Enter to stop the stream...\n")
    finally:
        bambu_client.stop_camera_stream()
        print("Camera stream stopped.")


if __name__ == "__main__":
    main()
