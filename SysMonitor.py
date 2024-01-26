import platform
import datetime
import psutil
import os

def get_os_info():
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("OS Release:", platform.release())

def get_cpu_info():
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def get_memory_info():
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024.0 ** 3), 2)  # Convert to GB
    available = round(memory.available / (1024.0 ** 3), 2)
    used_percentage = memory.percent
    print(f"Total Memory: {total} GB")
    print(f"Available Memory: {available} GB")
    print(f"Used Memory Percentage: {used_percentage}%")

def get_disk_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"\tMountpoint: {partition.mountpoint}")
        print(f"\tFile system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"\tTotal Size: {round(partition_usage.total / (1024.0 ** 3), 2)} GB")
        print(f"\tUsed: {round(partition_usage.used / (1024.0 ** 3), 2)} GB")
        print(f"\tFree: {round(partition_usage.free / (1024.0 ** 3), 2)} GB")
        print(f"\tPercentage Used: {partition_usage.percent}%\n")

def get_time_info():
    print("Current Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def display_system_info():
    print("Gathering system information...\n")
    get_os_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_time_info()

if __name__ == "__main__":
    display_system_info()