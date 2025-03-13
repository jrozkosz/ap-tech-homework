"""Module providing implementation for DeviceFromFile class"""

import json
from typing import Dict
from devices.device_interface import Device

class DeviceFromFile(Device):
    """Class representing a device which parameters are provided in a file"""

    def __init__(self, file_path):
        self.parameters = {}
        self.file_path = file_path

    def get_parameters(self) -> Dict[str, object]:
        """Function returning device's parameters list"""
        self.__read_parameters()
        return self.parameters

    def __read_parameters(self):
        """Function reading device's parameters list"""
        with open(self.file_path, 'r', encoding="utf-8") as file:
            self.parameters = json.load(file)
