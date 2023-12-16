from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json


@dataclass
class Upload:
    status: str
    progress: int
    message: str


@dataclass
class Online:
    ahb: bool
    rfid: bool
    version: int


@dataclass
class AMS:
    ams: List[Any]
    ams_exist_bits: str
    tray_exist_bits: str
    tray_is_bbl_bits: str
    tray_tar: str
    tray_now: str
    tray_pre: str
    tray_read_done_bits: str
    tray_reading_bits: str
    version: int
    insert_flag: bool
    power_on_flag: bool


@dataclass
class IPCam:
    ipcam_dev: str
    ipcam_record: str
    timelapse: str
    mode_bits: int


@dataclass
class VTTray:
    id: str
    tag_uid: str
    tray_id_name: str
    tray_info_idx: str
    tray_type: str
    tray_sub_brands: str
    tray_color: str
    tray_weight: str
    tray_diameter: str
    tray_temp: str
    tray_time: str
    bed_temp_type: str
    bed_temp: str
    nozzle_temp_max: str
    nozzle_temp_min: str
    xcam_info: str
    tray_uuid: str
    remain: int
    k: float
    n: int


@dataclass
class LightsReport:
    node: str
    mode: str


@dataclass
class UpgradeState:
    sequence_id: int
    progress: str
    status: str
    consistency_request: bool
    dis_state: int
    err_code: int
    force_upgrade: bool
    message: str
    module: str
    new_version_state: int
    new_ver_list: List[Any]


@dataclass
class PrinterStatus:
    upload: Upload
    nozzle_temper: float
    nozzle_target_temper: float
    bed_temper: float
    bed_target_temper: float
    chamber_temper: float
    mc_print_stage: str
    heatbreak_fan_speed: str
    cooling_fan_speed: str
    big_fan1_speed: str
    big_fan2_speed: str
    mc_percent: int
    mc_remaining_time: int
    ams_status: int
    ams_rfid_status: int
    hw_switch_state: int
    spd_mag: int
    spd_lvl: int
    print_error: int
    lifecycle: str
    wifi_signal: str
    gcode_state: str
    gcode_file_prepare_percent: str
    queue_number: int
    queue_total: int
    queue_est: int
    queue_sts: int
    project_id: str
    profile_id: str
    task_id: str
    subtask_id: str
    subtask_name: str
    gcode_file: str
    stg: List[Any]
    stg_cur: int
    print_type: str
    home_flag: int
    mc_print_line_number: str
    mc_print_sub_stage: int
    sdcard: bool
    force_upgrade: bool
    mess_production_state: str
    layer_num: int
    total_layer_num: int
    s_obj: List[Any]
    fan_gear: int
    hms: List[Any]
    online: Online
    ams: AMS
    ipcam: IPCam
    vt_tray: VTTray
    lights_report: List[LightsReport]
    upgrade_state: UpgradeState
    command: str
    msg: int
    sequence_id: str

    def __init__(self, **data):
        self.upload = Upload(**data["upload"]) if "upload" in data else None
        self.nozzle_temper = data.get("nozzle_temper", 0.0)
        self.nozzle_target_temper = data.get("nozzle_target_temper", 0.0)
        self.bed_temper = data.get("bed_temper", 0.0)
        self.bed_target_temper = data.get("bed_target_temper", 0.0)
        self.chamber_temper = data.get("chamber_temper", 0.0)
        self.mc_print_stage = data.get("mc_print_stage", "")
        self.heatbreak_fan_speed = data.get("heatbreak_fan_speed", "")
        self.cooling_fan_speed = data.get("cooling_fan_speed", "")
        self.big_fan1_speed = data.get("big_fan1_speed", "")
        self.big_fan2_speed = data.get("big_fan2_speed", "")
        self.mc_percent = data.get("mc_percent", 0)
        self.mc_remaining_time = data.get("mc_remaining_time", 0)
        self.ams_status = data.get("ams_status", 0)
        self.ams_rfid_status = data.get("ams_rfid_status", 0)
        self.hw_switch_state = data.get("hw_switch_state", 0)
        self.spd_mag = data.get("spd_mag", 0)
        self.spd_lvl = data.get("spd_lvl", 0)
        self.print_error = data.get("print_error", 0)
        self.lifecycle = data.get("lifecycle", "")
        self.wifi_signal = data.get("wifi_signal", "")
        self.gcode_state = data.get("gcode_state", "")
        self.gcode_file_prepare_percent = data.get("gcode_file_prepare_percent", "")
        self.queue_number = data.get("queue_number", 0)
        self.queue_total = data.get("queue_total", 0)
        self.queue_est = data.get("queue_est", 0)
        self.queue_sts = data.get("queue_sts", 0)
        self.project_id = data.get("project_id", "")
        self.profile_id = data.get("profile_id", "")
        self.task_id = data.get("task_id", "")
        self.subtask_id = data.get("subtask_id", "")
        self.subtask_name = data.get("subtask_name", "")
        self.gcode_file = data.get("gcode_file", "")
        self.stg = data.get("stg", [])
        self.stg_cur = data.get("stg_cur", 0)
        self.print_type = data.get("print_type", "")
        self.home_flag = data.get("home_flag", 0)
        self.mc_print_line_number = data.get("mc_print_line_number", "")
        self.mc_print_sub_stage = data.get("mc_print_sub_stage", 0)
        self.sdcard = data.get("sdcard", False)
        self.force_upgrade = data.get("force_upgrade", False)
        self.mess_production_state = data.get("mess_production_state", "")
        self.layer_num = data.get("layer_num", 0)
        self.total_layer_num = data.get("total_layer_num", 0)
        self.s_obj = data.get("s_obj", [])
        self.fan_gear = data.get("fan_gear", 0)
        self.hms = data.get("hms", [])
        self.online = Online(**data["online"]) if "online" in data else None
        self.ams = AMS(**data["ams"]) if "ams" in data else None
        self.ipcam = IPCam(**data["ipcam"]) if "ipcam" in data else None
        self.vt_tray = VTTray(**data["vt_tray"]) if "vt_tray" in data else None
        self.lights_report = [
            LightsReport(**lr) for lr in data.get("lights_report", [])
        ]
        self.upgrade_state = (
            UpgradeState(**data["upgrade_state"]) if "upgrade_state" in data else None
        )
        self.command = data.get("command", "")
        self.msg = data.get("msg", 0)
        self.sequence_id = data.get("sequence_id", "")
