import time
from bambu_connect import BambuClient, PrinterStatus
from dataclasses import asdict
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your actual details
hostname = os.getenv('HOSTNAME')
access_code = os.getenv('ACCESS_CODE')
serial = os.getenv('SERIAL')


def custom_callback(msg: PrinterStatus):
    printer_status_dict = asdict(msg)
    pprint.pprint(printer_status_dict)


def on_watch_client_connect():
    print("WatchClient connected, Waiting for connection...")
    time.sleep(1)  # Waits for 1 second
    print("Executing dump_info.")
    bambu_client.dump_info()


bambu_client = BambuClient(hostname, access_code, serial)
bambu_client.start_watch_client(custom_callback, on_watch_client_connect)

try:
    while True:
        time.sleep(1)  # Just keep the main thread alive
except KeyboardInterrupt:
    print("Streaming stopped by user.")

# Stop the client
bambu_client.stop()
