"""Freebox component constants."""
from __future__ import annotations

import socket

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.cover import CoverDeviceClass, CoverEntityDescription
from homeassistant.components.camera import CameraEntityDescription
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import Platform, EntityCategory, PERCENTAGE

DOMAIN = "freebox_home"
SERVICE_REBOOT = "reboot"

APP_DESC = {
    "app_id": "hass",
    "app_name": "Home Assistant",
    "app_version": "0.109",
    "device_name": socket.gethostname(),
}
API_VERSION = "v6"

PLATFORMS = [
    Platform.DEVICE_TRACKER,
    Platform.SENSOR,
    Platform.BUTTON,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.COVER,
    Platform.CAMERA,
]

DEFAULT_DEVICE_NAME = "Unknown device"

# to store the cookie
STORAGE_KEY = DOMAIN
STORAGE_VERSION = 1

# Sensors
CONNECTION_SENSORS_KEYS = {"rate_down", "rate_up"}

HOME_NODE_BATTERY_SENSOR: SensorEntityDescription = SensorEntityDescription(
    key="battery",
    name="Battery",
    entity_category=EntityCategory.DIAGNOSTIC,
    device_class=SensorDeviceClass.BATTERY,
    state_class=SensorStateClass.MEASUREMENT,
    native_unit_of_measurement=PERCENTAGE,
)

HOME_NODE_REMOTE_BUTTON_SENSOR: SensorEntityDescription = SensorEntityDescription(
    key="pushed",
    name="Last action",
)

HOME_NODES_SENSORS: dict[str, SensorEntityDescription] = {
    "battery": HOME_NODE_BATTERY_SENSOR,
    "pushed": HOME_NODE_REMOTE_BUTTON_SENSOR,
}

# Binary Sensors
HOME_NODE_COVER_BINARY_SENSOR: BinarySensorEntityDescription = (
    BinarySensorEntityDescription(
        key="cover",
        name="Cover",
        entity_category=EntityCategory.DIAGNOSTIC,
        device_class=BinarySensorDeviceClass.OPENING,
    )
)

HOME_NODE_MOTION_BINARY_SENSOR: BinarySensorEntityDescription = (
    BinarySensorEntityDescription(
        key="motion",
        name="Motion",
        device_class=BinarySensorDeviceClass.MOTION,
    )
)

HOME_NODE_OPENING_BINARY_SENSOR: BinarySensorEntityDescription = (
    BinarySensorEntityDescription(
        key="opening",
        name="Status",
        device_class=BinarySensorDeviceClass.OPENING,
    )
)

HOME_NODES_BINARY_SENSORS: dict[str, BinarySensorEntityDescription] = {
    "cover": HOME_NODE_COVER_BINARY_SENSOR,
    "opening": HOME_NODE_OPENING_BINARY_SENSOR,
    "motion": HOME_NODE_MOTION_BINARY_SENSOR,
}

# Cover
HOME_NODE_SHUTTER_COVER: CoverEntityDescription = CoverEntityDescription(
    key="shutter",
    name="Shutter",
    device_class=CoverDeviceClass.SHUTTER,
)

# Basic Cover
HOME_NODE_BASIC_SHUTTER_COVER: CoverEntityDescription = CoverEntityDescription(
    key="basic_shutter", name="basic_shutter", device_class=CoverDeviceClass.SHUTTER
)

HOME_NODES_COVERS: dict[str, CoverEntityDescription] = {
    "shutter": HOME_NODE_SHUTTER_COVER,
    "basic_shutter": HOME_NODE_BASIC_SHUTTER_COVER,
}

# Camera
HOME_NODE_CAMERA: CameraEntityDescription = CameraEntityDescription(
    key="camera", name="camera"
)

# Alarm
HOME_NODES_ALARM_REMOTE_KEY: list[str] = [
    "Alarm 1 ON",
    "Alarm OFF",
    "Alarm 2 ON",
    "Not used",
]


# Icons
DEVICE_ICONS = {
    "freebox_delta": "mdi:television-guide",
    "freebox_hd": "mdi:television-guide",
    "freebox_mini": "mdi:television-guide",
    "freebox_player": "mdi:television-guide",
    "ip_camera": "mdi:cctv",
    "ip_phone": "mdi:phone-voip",
    "laptop": "mdi:laptop",
    "multimedia_device": "mdi:play-network",
    "nas": "mdi:nas",
    "networking_device": "mdi:network",
    "printer": "mdi:printer",
    "router": "mdi:router-wireless",
    "smartphone": "mdi:cellphone",
    "tablet": "mdi:tablet",
    "television": "mdi:television",
    "vg_console": "mdi:gamepad-variant",
    "workstation": "mdi:desktop-tower-monitor",
}
