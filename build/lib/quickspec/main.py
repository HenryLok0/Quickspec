import sys
from datetime import datetime
def get_detail():
    detail = {}
    if wmi:
        c = wmi.WMI()
        # 主機板型號
        try:
            board = c.Win32_BaseBoard()[0]
            detail['Motherboard'] = f"{board.Manufacturer} {board.Product}"
        except Exception:
            detail['Motherboard'] = 'Unknown'
        # BIOS 版本
        try:
            bios = c.Win32_BIOS()[0]
            detail['BIOS'] = f"{bios.Manufacturer} {bios.SMBIOSBIOSVersion} ({bios.ReleaseDate})"
        except Exception:
            detail['BIOS'] = 'Unknown'
        # 網路卡資訊
        try:
            nics = c.Win32_NetworkAdapter()
            nic_list = [nic.Name for nic in nics if nic.PhysicalAdapter]
            detail['Network Adapters'] = ', '.join(nic_list) if nic_list else 'None'
        except Exception:
            detail['Network Adapters'] = 'Unknown'
        # 顯示器解析度
        try:
            screens = c.Win32_DesktopMonitor()
            res_list = [f"{s.ScreenWidth}x{s.ScreenHeight}" for s in screens if s.ScreenWidth and s.ScreenHeight]
            detail['Display Resolution'] = ', '.join(res_list) if res_list else 'Unknown'
        except Exception:
            detail['Display Resolution'] = 'Unknown'
        # 系統開機時間
        try:
            os = c.Win32_OperatingSystem()[0]
            boot_time = datetime.strptime(os.LastBootUpTime.split('.')[0], "%Y%m%d%H%M%S")
            uptime = datetime.now() - boot_time
            detail['Boot Time'] = boot_time.strftime('%Y-%m-%d %H:%M:%S')
            detail['Uptime'] = str(uptime).split('.')[0]
        except Exception:
            detail['Boot Time'] = 'Unknown'
            detail['Uptime'] = 'Unknown'
        # 處理器快取（L2/L3）
        try:
            cpu = c.Win32_Processor()[0]
            detail['CPU Cache'] = f"L2: {cpu.L2CacheSize} KB, L3: {cpu.L3CacheSize} KB"
        except Exception:
            detail['CPU Cache'] = 'Unknown'
        # 虛擬化支援
        try:
            cpu = c.Win32_Processor()[0]
            detail['Virtualization'] = 'Enabled' if getattr(cpu, 'VirtualizationFirmwareEnabled', False) else 'Disabled'
        except Exception:
            detail['Virtualization'] = 'Unknown'
        # 電池資訊（筆電）
        try:
            batteries = c.Win32_Battery()
            if batteries:
                bat = batteries[0]
                detail['Battery'] = f"{bat.Name}, {bat.EstimatedChargeRemaining}%"
            else:
                detail['Battery'] = 'No Battery'
        except Exception:
            detail['Battery'] = 'Unknown'
    else:
        detail['Detail'] = 'WMI not available on this system.'
    return detail
def print_detail():
    detail = get_detail()
    print("=== Computer Detail Information ===")
    for k, v in detail.items():
        print(f"{k}: {v}")
import platform
import psutil

try:
    import cpuinfo
except ImportError:
    cpuinfo = None
import importlib
GPUtil = None
gputil_import_error = None
try:
    GPUtil = importlib.import_module('GPUtil')
except Exception as e:
    gputil_import_error = str(e)

# WMI for Windows GPU detection
wmi = None
wmi_import_error = None
try:
    wmi = importlib.import_module('wmi')
except Exception as e:
    wmi_import_error = str(e)

def get_spec():
    info = {}
    info['OS'] = platform.platform()
    if cpuinfo:
        cpu = cpuinfo.get_cpu_info()
        cpu_name = cpu.get('brand_raw', 'Unknown')
    else:
        cpu_name = platform.processor() or 'Unknown'
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    info['CPU'] = f"{cpu_name} ({cpu_cores} Cores + {cpu_threads} Threads)"
    info['CPU Frequency'] = f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else 'Unknown'
    mem = psutil.virtual_memory()
    mem_used = mem.used / (1024**3)
    mem_total = mem.total / (1024**3)
    mem_percent = mem.percent
    info['Memory'] = f"{mem_used:.2f} GB / {mem_total:.2f} GB ({mem_percent:.1f}%)"

    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024**3)
    disk_free = disk.free / (1024**3)
    disk_used = disk_total - disk_free
    disk_percent = disk.percent
    info['Disk'] = f"{disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent:.1f}%)"
    # GPU 資訊（優先使用 wmi，支援所有 Windows 顯示卡）
    gpu_list = []
    if wmi:
        try:
            c = wmi.WMI()
            for gpu in c.Win32_VideoController():
                name = gpu.Name
                ram = int(gpu.AdapterRAM) // (1024**2) if gpu.AdapterRAM else 'Unknown'
                gpu_list.append(f"{name} ({ram}MB)")
        except Exception as e:
            gpu_list.append(f"WMI error: {e}")
    elif wmi_import_error:
        gpu_list.append(f"WMI import error: {wmi_import_error}")
    # 若 wmi 無法使用，則用 GPUtil
    elif GPUtil:
        gpus = GPUtil.getGPUs()
        if gpus:
            for idx, gpu in enumerate(gpus):
                gpu_list.append(f"{gpu.name} ({gpu.driver}) {gpu.memoryTotal}MB")
        else:
            gpu_list.append('No GPU detected')
    elif gputil_import_error:
        gpu_list.append(f'GPUtil import error: {gputil_import_error}')
    else:
        gpu_list.append('No GPU detected')
    # 顯示所有 GPU
    for idx, gpu_info in enumerate(gpu_list):
        info[f'GPU {idx+1}'] = gpu_info
    return info

def print_spec():
    spec = get_spec()
    print("=== Computer Specification ===")
    # 顯示順序：OS, CPU, CPU Frequency, GPU, Memory, Disk
    order = [
        'OS',
        'CPU',
        'CPU Frequency',
    ]
    # GPU 可能有多個
    gpu_keys = [k for k in spec.keys() if k.startswith('GPU')]
    order.extend(gpu_keys)
    order.extend([
        'Memory',
        'Disk',
    ])
    for k in order:
        if k in spec:
            print(f"{k}: {spec[k]}")

if __name__ == "__main__":
    if '--detail' in sys.argv:
        print_spec()
        print()
        print_detail()
        print()
    else:
        print_spec()
