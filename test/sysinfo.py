import platform
import psutil
import os
import time
from datetime import datetime

def get_system_info():
    info = {
        "Platform": platform.system(),
        "Platform Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3))} GB",
        "Memory Usage": f"{psutil.virtual_memory().percent} %"
    }
    return info

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    return processes

def display_system_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"System Information - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    print("\nRunning Processes:")
    print(f"{'PID':<10} {'Name':<25} {'CPU %':<10} {'Memory %':<10}")
    print("-"*80)
    processes = sorted(get_running_processes(), key=lambda p: p['cpu_percent'], reverse=True)[:10]
    for process in processes:
        try:
            print(f"{process['pid']:<10} {process['name']:<25} {process['cpu_percent']:<10.2f} {process['memory_percent']:<10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    while True:
        display_system_info()
        time.sleep(5)