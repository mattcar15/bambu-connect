from .utils.models import PrinterStatus
import json
import ssl
from typing import Any, Callable, Dict, Optional

import paho.mqtt.client as mqtt


class WatchClient:
    def __init__(self, hostname: str, access_code: str, serial: str):
        self.hostname = hostname
        self.access_code = access_code
        self.serial = serial
        self.client = self.__setup_mqtt_client()
        self.values = {}
        self.printerStatus = None
        self.message_callback = None

    def __setup_mqtt_client(self) -> mqtt.Client:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        client.username_pw_set("bblp", self.access_code)
        client.tls_set(tls_version=ssl.PROTOCOL_TLS, cert_reqs=ssl.CERT_NONE)
        client.tls_insecure_set(True)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        return client

    def on_connect(self, client: mqtt.Client, userdata: Any, flags: Any, rc: int):
        client.subscribe(f"device/{self.serial}/report")
        if self.on_connect_callback:
            self.on_connect_callback()

    def start(
        self,
        message_callback: Optional[Callable[[PrinterStatus], None]] = None,
        on_connect_callback: Optional[Callable[[], None]] = None,
    ):
        self.message_callback = message_callback
        self.on_connect_callback = on_connect_callback
        self.client.connect(self.hostname, 8883, 60)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
        
    def on_message(self, msg: str):
        doc = json.loads(msg.payload)
        try:
            if not doc:
                return

            self.values = dict(self.values, **doc["print"])
            self.printerStatus = PrinterStatus(**self.values)

            if self.message_callback:
                self.message_callback(self.printerStatus)
        except KeyError:
            return
