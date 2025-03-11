import json
from typing import Dict
from devices.device_interface import Device

class DeviceFromFile(Device):
    """Class representing a device which parameters are provided in a file"""

    def __init__(self):
        self.parameters = {}

    def get_parameters(self) -> Dict[str, object]:
        """Function returning device's parameters list"""
        return self.parameters

    def set_parameters(self, file_path: str):
        """Function setting device's parameters list"""
        with open(file_path, 'r', encoding="utf-8") as file:
            self.parameters = json.load(file)
