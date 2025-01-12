import paho.mqtt.client as mqtt
import ssl
import json
import subprocess
import re


class ExecuteClient:
    def __init__(self, hostname: str, access_code: str, serial: str):
        self.hostname = hostname
        self.access_code = access_code
        self.serial = serial
        self.client = self.__setup_mqtt_client()

    def __setup_mqtt_client(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        client.username_pw_set("bblp", self.access_code)
        client.tls_set(tls_version=ssl.PROTOCOL_TLS, cert_reqs=ssl.CERT_NONE)
        client.tls_insecure_set(True)
        client.connect(self.hostname, 8883, 60)
        return client

    def disconnect(self):
        self.client.disconnect()

    def send_command(self, payload):
        self.client.loop_start()
        self.client.publish(f"device/{self.serial}/request", payload)
        self.client.loop_stop()

    def send_gcode(self, gcode: str):
        if not isinstance(gcode, str):
            raise ValueError("The 'gcode' parameter must be a string.")
        payload = f'{{"print": {{"command": "gcode_line", "sequence_id": 2006, "param": "{gcode} \n"}}, "user_id":"1234567890"}}'
        self.send_command(payload)

    # this dumps all the printer stats, for minor print updates the printer will send them automatically.
    def dump_info(self):
        payload = f'{{"pushing": {{ "sequence_id": 1, "command": "pushall"}}, "user_id":"1234567890"}}'
        self.send_command(payload)

    # when using this, choose the send to printer option in bambu or cura slicer. Provide the file name (no path)
    def start_print(self, file: str):
        if not isinstance(file, str):
            raise ValueError("The 'file' parameter must be a string.")
        payload = json.dumps(
            {
                "print": {
                    "sequence_id": 13,
                    "command": "project_file",
                    "param": "Metadata/plate_1.gcode",
                    "subtask_name": f"{file}",
                    "url": f"ftp://{file}",
                    "bed_type": "auto",
                    "timelapse": False,
                    "bed_leveling": True,
                    "flow_cali": False,
                    "vibration_cali": True,
                    "layer_inspect": False,
                    "use_ams": False,
                    "profile_id": "0",
                    "project_id": "0",
                    "subtask_id": "0",
                    "task_id": "0",
                }
            }
        )
        self.send_command(payload)
