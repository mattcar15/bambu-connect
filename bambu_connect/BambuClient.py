from .CameraClient import CameraClient
from .WatchClient import WatchClient
from .ExecuteClient import ExecuteClient
from .FileClient import FileClient
from .utils.models import PrinterStatus
from typing import Callable, Dict, Optional, Any


class BambuClient:
    def __init__(self, hostname: str, access_code: str, serial: str):
        self.cameraClient = CameraClient(hostname, access_code)
        self.watchClient = WatchClient(hostname, access_code, serial)
        self.executeClient = ExecuteClient(hostname, access_code, serial)
        self.fileClient = FileClient(hostname, access_code, serial)

    ############# Camera Wrappers #############
    def start_camera_stream(self, img_callback):
        self.cameraClient.start_stream(img_callback)

    def stop_camera_stream(self):
        self.cameraClient.stop_stream()

    def capture_camera_frame(self):
        return self.cameraClient.capture_frame()

    ############# WatchClient Wrappers #############
    def start_watch_client(
        self,
        message_callback: Optional[Callable[[PrinterStatus], None]] = None,
        on_connect_callback: Optional[Callable[[], None]] = None,
    ):
        self.watchClient.start(message_callback, on_connect_callback)

    def stop_watch_client(self):
        self.watchClient.stop()

    ############# ExecuteClient Wrappers #############
    def send_gcode(self, gcode):
        self.executeClient.send_gcode(gcode)

    def dump_info(self):
        self.executeClient.dump_info()

    def start_print(self, file):
        self.executeClient.start_print(file)

    ############# FileClient Wrappers #############
    def get_files(self, path="/", extension=".3mf"):
        return self.fileClient.get_files(path, extension)
    
    def download_file(self, local_path: str, remote_path="/timelapse", extension="", verbose=True):
        return self.fileClient.download_file(remote_path, local_path=local_path, verbose=verbose)
