import threading
import pytest
from unittest.mock import patch, MagicMock
from device_monitor import DeviceMonitor
from devices.device_interface import Device

@pytest.fixture
def mock_device():
    """Function mocking device"""
    device = MagicMock(spec=Device)
    device.get_parameters.return_value = {"param1": 111, "param2": "active"}
    return device

def test_initial_parameters():
    """Test checking whether initials attributes of an object were set properly"""
    monitor = DeviceMonitor()
    assert not monitor.devices
    assert not monitor.statuses
    assert not monitor.thread
    assert monitor.running is False
    assert isinstance(monitor.lock, type(threading.Lock()))

@patch("threading.Thread")
def test_start_not_running(mock_thread):
    """Test checking whether start method creates a thread and sets running flag"""
    monitor = DeviceMonitor()
    assert monitor.running is False
    monitor.start()
    assert monitor.running is True
    mock_thread.assert_called_once()
    mock_thread.return_value.start.assert_called_once()

@patch("threading.Thread")
def test_start_running(mock_thread):
    """Test checking wheter start method does not create many threads when called again"""
    monitor = DeviceMonitor()
    monitor.start()
    created_thread = monitor.thread
    monitor.start()

    assert monitor.running is True
    assert monitor.thread == created_thread
    mock_thread.assert_called_once()

@patch.object(threading.Thread, "join")
def test_stop_when_running(_):
    """Test checking whether stop method terminates thread and sets running flag to negative"""
    monitor = DeviceMonitor()
    monitor.running = True
    monitor.thread = MagicMock()
    monitor.stop()
    assert not monitor.running
    monitor.thread.join.assert_called_once()


@patch.object(threading.Thread, "join")
def test_stop_when_not_running(mock_join):
    """Test checking whether stop method does not stop a thread when there isn't one"""
    monitor = DeviceMonitor()
    monitor.running = False
    monitor.thread = None
    monitor.stop()
    assert not monitor.running
    mock_join.assert_not_called()

def test_get_statuses():
    """Test checking whether get_statuses method returns devices statuses"""
    monitor = DeviceMonitor()
    mock_statuses = {
        1: {'aaa': 14, 'bbb': 300},
        2: {'aaa': 14, 'bbb': 300}
    }
    monitor.statuses = mock_statuses
    assert monitor.get_statuses() == mock_statuses

def test_adding_devices_to_be_monitored():
    """Test checking wheter devices are added properly"""
    monitor = DeviceMonitor()
    monitor.add_monitored_devices([None, None, None])
    assert monitor.get_devices() == {
        1: None,
        2: None,
        3: None
    }

def test_read_devices_parameters(mock_device):
    """Test checking wheter read_devices_parameters method works correctly"""
    monitor = DeviceMonitor()

    mock_device.get_parameters.return_value = {"param1": 111, "param2": "active"}

    monitor.devices = {1: mock_device}
    monitor.statuses = {}
    monitor.running = True
    monitor._read_devices_parameters()

    assert monitor.statuses[0] == {"param1": 111, "param2": "active"}
