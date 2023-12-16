from bambu_connect import BambuClient
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your actual details
hostname = os.getenv('HOSTNAME')
access_code = os.getenv('ACCESS_CODE')
serial = os.getenv('SERIAL')


def main():
    bambu_client = BambuClient(hostname, access_code, serial)

    # List files on the printer
    printer_files = bambu_client.get_files()
    print("Files on the printer:")
    for file in printer_files:
        print(file)

    # IMPORTANT: Before executing gcode make sure the print bed is clear.
    #            The code is commented out to ensure you read this before executing it and possibly harming the printer

    # Example G-code for homing the printer
    gcode_command = "G28"

    print(f"Sending G-code command: {gcode_command}")
    bambu_client.send_gcode(gcode_command)


if __name__ == "__main__":
    main()
