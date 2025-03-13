"""Module providing unit tests for DeviceFromFile class"""

from unittest.mock import mock_open, patch
import json
from devices.device_from_file import DeviceFromFile


def test_empty_initials_parameters():
    """Test checking whether parameters are set correctly while initializing"""
    device = DeviceFromFile("dummy.json")
    assert device.parameters == {}
    assert device.file_path == "dummy.json"

def test_get_parameters():
    """Test checking if get_parameters correctly reads data from a file"""
    mock_data = {"param1": 111, "param2": False, "param3": "aaa"}
    mock_json_data = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        device = DeviceFromFile("random_path.json")
        device.get_parameters()
        assert device.get_parameters() == {
            "param1": 111,
            "param2": False,
            "param3": "aaa"
        }
