from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json


@dataclass
class Upload:
    status: Optional[str] = None
    progress: Optional[int] = None
    message: Optional[str] = None


@dataclass
class Online:
    ahb: Optional[bool] = None
    rfid: Optional[bool] = None
    version: Optional[int] = None


@dataclass
class VTTray:
    id: Optional[str] = None
    tag_uid: Optional[str] = None
    tray_id_name: Optional[str] = None
    tray_info_idx: Optional[str] = None
    tray_type: Optional[str] = None
    tray_sub_brands: Optional[str] = None
    tray_color: Optional[str] = None
    tray_weight: Optional[str] = None
    tray_diameter: Optional[str] = None
    tray_temp: Optional[str] = None
    tray_time: Optional[str] = None
    bed_temp_type: Optional[str] = None
    bed_temp: Optional[str] = None
    nozzle_temp_max: Optional[str] = None
    nozzle_temp_min: Optional[str] = None
    xcam_info: Optional[str] = None
    tray_uuid: Optional[str] = None
    remain: Optional[int] = None
    k: Optional[float] = None
    n: Optional[int] = None
    cali_idx: Optional[int] = None

@dataclass
class AMSEntry:
    humidity: Optional[str] = None
    id: Optional[str] = None
    temp: Optional[str] = None
    tray: Optional[List[VTTray]] = None

@dataclass
class AMS:
    ams: Optional[List[AMSEntry]] = None
    ams_exist_bits: Optional[str] = None
    tray_exist_bits: Optional[str] = None
    tray_is_bbl_bits: Optional[str] = None
    tray_tar: Optional[str] = None
    tray_now: Optional[str] = None
    tray_pre: Optional[str] = None
    tray_read_done_bits: Optional[str] = None
    tray_reading_bits: Optional[str] = None
    version: Optional[int] = None
    insert_flag: Optional[bool] = None
    power_on_flag: Optional[bool] = None

@dataclass
class IPCam:
    ipcam_dev: Optional[str] = None
    ipcam_record: Optional[str] = None
    timelapse: Optional[str] = None
    resolution: Optional[str] = None
    tutk_server: Optional[str] = None
    mode_bits: Optional[int] = None
    resolution: Optional[str] = None
    tutk_server: Optional[str] = None


@dataclass
class LightsReport:
    node: Optional[str] = None
    mode: Optional[str] = None

@dataclass
class UpgradeState:
    sequence_id: Optional[int] = None
    progress: Optional[str] = None
    status: Optional[str] = None
    consistency_request: Optional[bool] = None
    dis_state: Optional[int] = None
    err_code: Optional[int] = None
    force_upgrade: Optional[bool] = None
    message: Optional[str] = None
    module: Optional[str] = None
    new_version_state: Optional[int] = None
    new_ver_list: Optional[List[Any]] = None
    cur_state_code: Optional[int] = None
    idx2: Optional[int] = None


@dataclass
class PrinterStatus:
    upload: Optional[Upload] = None
    nozzle_temper: Optional[float] = None
    nozzle_target_temper: Optional[float] = None
    bed_temper: Optional[float] = None
    bed_target_temper: Optional[float] = None
    chamber_temper: Optional[float] = None
    mc_print_stage: Optional[str] = None
    heatbreak_fan_speed: Optional[str] = None
    cooling_fan_speed: Optional[str] = None
    big_fan1_speed: Optional[str] = None
    big_fan2_speed: Optional[str] = None
    mc_percent: Optional[int] = None
    mc_remaining_time: Optional[int] = None
    ams_status: Optional[int] = None
    ams_rfid_status: Optional[int] = None
    hw_switch_state: Optional[int] = None
    spd_mag: Optional[int] = None
    spd_lvl: Optional[int] = None
    print_error: Optional[int] = None
    lifecycle: Optional[str] = None
    wifi_signal: Optional[str] = None
    gcode_state: Optional[str] = None
    gcode_file_prepare_percent: Optional[str] = None
    queue_number: Optional[int] = None
    queue_total: Optional[int] = None
    queue_est: Optional[int] = None
    queue_sts: Optional[int] = None
    project_id: Optional[str] = None
    profile_id: Optional[str] = None
    task_id: Optional[str] = None
    subtask_id: Optional[str] = None
    subtask_name: Optional[str] = None
    gcode_file: Optional[str] = None
    stg: Optional[List[Any]] = None
    stg_cur: Optional[int] = None
    print_type: Optional[str] = None
    home_flag: Optional[int] = None
    mc_print_line_number: Optional[str] = None
    mc_print_sub_stage: Optional[int] = None
    sdcard: Optional[bool] = None
    force_upgrade: Optional[bool] = None
    mess_production_state: Optional[str] = None
    layer_num: Optional[int] = None
    total_layer_num: Optional[int] = None
    s_obj: Optional[List[Any]] = None
    fan_gear: Optional[int] = None
    hms: Optional[List[Any]] = None
    online: Optional[Online] = None
    ams: Optional[AMS] = None
    ipcam: Optional[IPCam] = None
    vt_tray: Optional[VTTray] = None
    lights_report: Optional[List[LightsReport]] = None
    upgrade_state: Optional[UpgradeState] = None
    command: Optional[str] = None
    msg: Optional[int] = None
    sequence_id: Optional[str] = None

    def __init__(self, **data):
        self.upload = Upload(**data["upload"]) if "upload" in data else None
        self.nozzle_temper = data.get("nozzle_temper")
        self.nozzle_target_temper = data.get("nozzle_target_temper")
        self.bed_temper = data.get("bed_temper")
        self.bed_target_temper = data.get("bed_target_temper")
        self.chamber_temper = data.get("chamber_temper")
        self.mc_print_stage = data.get("mc_print_stage")
        self.heatbreak_fan_speed = data.get("heatbreak_fan_speed")
        self.cooling_fan_speed = data.get("cooling_fan_speed")
        self.big_fan1_speed = data.get("big_fan1_speed")
        self.big_fan2_speed = data.get("big_fan2_speed")
        self.mc_percent = data.get("mc_percent")
        self.mc_remaining_time = data.get("mc_remaining_time")
        self.ams_status = data.get("ams_status")
        self.ams_rfid_status = data.get("ams_rfid_status")
        self.hw_switch_state = data.get("hw_switch_state")
        self.spd_mag = data.get("spd_mag")
        self.spd_lvl = data.get("spd_lvl")
        self.print_error = data.get("print_error")
        self.lifecycle = data.get("lifecycle")
        self.wifi_signal = data.get("wifi_signal")
        self.gcode_state = data.get("gcode_state")
        self.gcode_file_prepare_percent = data.get("gcode_file_prepare_percent")
        self.queue_number = data.get("queue_number")
        self.queue_total = data.get("queue_total")
        self.queue_est = data.get("queue_est")
        self.queue_sts = data.get("queue_sts")
        self.project_id = data.get("project_id")
        self.profile_id = data.get("profile_id")
        self.task_id = data.get("task_id")
        self.subtask_id = data.get("subtask_id")
        self.subtask_name = data.get("subtask_name")
        self.gcode_file = data.get("gcode_file")
        self.stg = data.get("stg", [])
        self.stg_cur = data.get("stg_cur")
        self.print_type = data.get("print_type")
        self.home_flag = data.get("home_flag")
        self.mc_print_line_number = data.get("mc_print_line_number")
        self.mc_print_sub_stage = data.get("mc_print_sub_stage")
        self.sdcard = data.get("sdcard", False)
        self.force_upgrade = data.get("force_upgrade", False)
        self.mess_production_state = data.get("mess_production_state")
        self.layer_num = data.get("layer_num")
        self.total_layer_num = data.get("total_layer_num")
        self.s_obj = data.get("s_obj", [])
        self.fan_gear = data.get("fan_gear")
        self.hms = data.get("hms", [])
        self.online = Online(**data["online"]) if "online" in data else None
        self.ams = AMS(**data["ams"]) if "ams" in data else None
        self.ipcam = IPCam(**data["ipcam"]) if "ipcam" in data else None
        self.vt_tray = VTTray(**data["vt_tray"]) if "vt_tray" in data else None
        self.lights_report = [LightsReport(**lr) for lr in data.get("lights_report", [])]
        self.upgrade_state = UpgradeState(**data["upgrade_state"]) if "upgrade_state" in data else None
        self.command = data.get("command")
        self.msg = data.get("msg")
        self.sequence_id = data.get("sequence_id")
