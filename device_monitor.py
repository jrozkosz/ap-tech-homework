"""Module providing implementation for DeviceMonitor class"""

import threading
import time
from typing import Dict
from devices.device_interface import Device

class DeviceMonitor:
    """Class representing monitoring of devices"""
    def __init__(self):
        self.devices = {}
        self.statuses = {}
        self.thread = None
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        """Function starting monitoring devices in another thread"""
        with self.lock:
            if not self.running:
                self.running = True
                self.thread = threading.Thread(target=self._read_devices_parameters)
                self.thread.start()

    def stop(self):
        """Function stopping monitoring devices"""
        with self.lock:
            self.running = False
        if self.thread:
            self.thread.join()

    def get_statuses(self) -> Dict[int, Dict[str, object]]:
        """Function getting devices' statuses"""
        with self.lock:
            return self.statuses

    def get_devices(self) -> Dict[int, Device]:
        """Function getting devices that are monitored"""
        return self.devices

    def add_monitored_devices(self, devices: list[Device]):
        """Function adding devices to be monitored"""
        device_id = list(self.devices.keys())[-1] + 1 if len(self.devices) > 0 else 1
        for device in devices:
            self.devices[device_id] = device
            device_id += 1

    def _read_devices_parameters(self):
        """Function reading devices parameters"""
        while self.running:
            with self.lock:
                self._get_device_parameters()

            time.sleep(1)

    def _get_device_parameters(self):
        for device_id, device in self.devices.items():
            self.statuses[device_id] = device.get_parameters()
