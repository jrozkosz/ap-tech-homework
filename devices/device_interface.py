from typing import Dict

class Device:
    """Interface representing a device"""

    def get_parameters(self) -> Dict[str, object]:
        """Function returning device's parameters list"""
        raise NotImplementedError()
