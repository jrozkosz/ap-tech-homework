import time
from device_monitor import DeviceMonitor
from devices.device_from_file import DeviceFromFile

def run_simulation():
    """Test function running DeviceMonitor simulation"""

    device1 = DeviceFromFile()
    device1.set_parameters("devices/device_parameters.json")

    monitor = DeviceMonitor()
    monitor.add_monitored_devices([device1])

    monitor.start()

    for _ in range(10):
        print(monitor.get_statuses())
        time.sleep(1)

    monitor.stop()

if __name__ == "__main__":
    run_simulation()
