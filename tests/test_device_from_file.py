from unittest.mock import mock_open, patch
import json
from devices.device_from_file import DeviceFromFile

def test_empty_initials_parameters():
    device = DeviceFromFile()
    assert device.get_parameters() == {}

def test_set_parameters():
    mock_data = {"param1": 111, "param2": False, "param3": "aaa"}
    mock_json_data = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        device = DeviceFromFile()
        device.set_parameters("random_path.json")
        assert device.get_parameters() == {
            "param1": 111,
            "param2": False,
            "param3": "aaa"
        }
