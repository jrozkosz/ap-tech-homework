"""Test script running a simulation of devices monitoring"""

import time
from device_monitor import DeviceMonitor
from devices.device_from_file import DeviceFromFile

def run_simulation():
    """Test function running DeviceMonitor simulation"""

    device1 = DeviceFromFile("devices/device_parameters.json")

    monitor = DeviceMonitor()
    monitor.add_monitored_devices([device1])

    monitor.start()

    for _ in range(20):
        time.sleep(1)
        print(monitor.get_statuses())

    monitor.stop()

if __name__ == "__main__":
    run_simulation()
