import platform
import psutil
try:
    import cpuinfo
except ImportError:
    cpuinfo = None

def get_spec():
    info = {}
    info['OS'] = platform.platform()
    info['CPU'] = platform.processor() or (cpuinfo.get_cpu_info()['brand_raw'] if cpuinfo else 'Unknown')
    info['CPU Cores'] = psutil.cpu_count(logical=False)
    info['CPU Threads'] = psutil.cpu_count(logical=True)
    info['CPU Frequency'] = f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else 'Unknown'
    info['Memory'] = f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    info['Disk'] = f"{psutil.disk_usage('/').total / (1024**3):.2f} GB"
    return info

def print_spec():
    spec = get_spec()
    print("=== Computer Specification ===")
    for k, v in spec.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    print_spec()
import platform
import psutil
try:
    import cpuinfo
except ImportError:
    cpuinfo = None

def get_spec():
    info = {}
    info['OS'] = platform.platform()
    info['CPU'] = platform.processor() or (cpuinfo.get_cpu_info()['brand_raw'] if cpuinfo else 'Unknown')
    info['CPU Cores'] = psutil.cpu_count(logical=False)
    info['CPU Threads'] = psutil.cpu_count(logical=True)
    info['CPU Frequency'] = f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else 'Unknown'
    info['Memory'] = f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    info['Disk'] = f"{psutil.disk_usage('/').total / (1024**3):.2f} GB"
    return info

def print_spec():
    spec = get_spec()
    print("=== Computer Specification ===")
    for k, v in spec.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    print_spec()
