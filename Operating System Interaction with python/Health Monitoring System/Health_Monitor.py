import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    perc = du.free / du.total *100
    return perc > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 20


if not check_disk_usage("/") or not check_cpu_usage():
    print("Unhealthy Condition")
else:
    print("HEALTHY")