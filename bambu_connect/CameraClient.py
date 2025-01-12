from datetime import datetime
import struct
import socket
import ssl
import threading
from typing import Callable


class CameraClient:
    def __init__(self, hostname: str, access_code: str, port: int = 6000):
        self.hostname = hostname
        self.port = port
        self.username = "bblp"
        self.auth_packet = self.__create_auth_packet__(self.username, access_code)
        self.streaming = False
        self.stream_thread = None

    def __create_auth_packet__(self, username, access_code):
        auth_data = bytearray()
        auth_data += struct.pack("<I", 0x40)  # '@'\0\0\0
        auth_data += struct.pack("<I", 0x3000)  # \0'0'\0\0
        auth_data += struct.pack("<I", 0)  # \0\0\0\0
        auth_data += struct.pack("<I", 0)  # \0\0\0\0
        for i in range(0, len(username)):
            auth_data += struct.pack("<c", username[i].encode('ascii'))
        for i in range(0, 32 - len(username)):
            auth_data += struct.pack("<x")
        for i in range(0, len(access_code)):
            auth_data += struct.pack("<c", access_code[i].encode('ascii'))
        for i in range(0, 32 - len(access_code)):
            auth_data += struct.pack("<x")
        return auth_data

    def __find_jpeg__(self, buf, start_marker, end_marker):
        start = buf.find(start_marker)
        end = buf.find(end_marker, start + len(start_marker))
        if start != -1 and end != -1:
            return buf[start : end + len(end_marker)], buf[end + len(end_marker) :]
        return None, buf

    def capture_frame(self):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        jpeg_start = bytearray([0xff, 0xd8, 0xff, 0xe0])
        jpeg_end = bytearray([0xff, 0xd9])
        read_chunk_size = 4096

        with socket.create_connection((self.hostname, self.port)) as sock:
            with ctx.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                ssock.write(self.auth_packet)
                buf = bytearray()
                while True:
                    dr = ssock.recv(read_chunk_size)
                    if not dr:
                        break
                    buf += dr
                    img, buf = self.__find_jpeg__(buf, jpeg_start, jpeg_end)
                    if img:
                        return bytes(img)

    def capture_stream(self, img_callback: Callable[[bytes], None]):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        jpeg_start = bytearray([0xff, 0xd8, 0xff, 0xe0])
        jpeg_end = bytearray([0xff, 0xd9])
        read_chunk_size = 4096

        with socket.create_connection((self.hostname, self.port)) as sock:
            with ctx.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                ssock.write(self.auth_packet)
                buf = bytearray()
                while self.streaming:
                    dr = ssock.recv(read_chunk_size)
                    if not dr:
                        break
                    buf += dr
                    img, buf = self.__find_jpeg__(buf, jpeg_start, jpeg_end)
                    if img:
                        img_callback(bytes(img))

    def start_stream(self, img_callback: Callable[[bytes], None]):
        if self.streaming:
            print("Stream already running.")
            return

        self.streaming = True
        self.stream_thread = threading.Thread(
            target=self.capture_stream, args=(img_callback,)
        )
        self.stream_thread.start()

    def stop_stream(self):
        if not self.streaming:
            print("Stream is not running.")
            return

        self.streaming = False
        self.stream_thread.join()
