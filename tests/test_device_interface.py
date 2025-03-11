import pytest
from devices.device_interface import Device

def test_get_parameters():
    """Test checking whether calling Interface's method causes an error"""
    device = Device()
    with pytest.raises(NotImplementedError):
        device.get_parameters()
