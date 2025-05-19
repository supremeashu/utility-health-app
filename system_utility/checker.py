import platform
import subprocess

def is_disk_encrypted():
    system = platform.system()
    try:
        if system == "Windows":
            output = subprocess.check_output("manage-bde -status", shell=True).decode()
            return "Percentage Encrypted: 100%" in output
        elif system == "Darwin":
            output = subprocess.check_output(["fdesetup", "status"]).decode()
            return "FileVault is On." in output
        elif system == "Linux":
            return subprocess.call(["lsblk", "-o", "NAME,TYPE,MOUNTPOINT"]) == 0
    except Exception:
        return False

def is_system_updated():
    try:
        system = platform.system()
        if system == "Windows":
            return True
        elif system == "Darwin":
            return True
        elif system == "Linux":
            result = subprocess.run(["apt", "list", "--upgradable"], stdout=subprocess.PIPE)
            return b"upgradable" not in result.stdout
    except Exception:
        return False

def has_antivirus():
    try:
        system = platform.system()
        if system == "Windows":
            output = subprocess.check_output("powershell Get-MpComputerStatus", shell=True).decode()
            return "RealTimeProtectionEnabled" in output
        elif system == "Darwin":
            return True
        elif system == "Linux":
            output = subprocess.getoutput("systemctl is-active clamav-daemon")
            return "active" in output
    except Exception:
        return False

def get_sleep_timeout():
    try:
        if platform.system() == "Windows":
            output = subprocess.getoutput("powercfg /q")
            return "VIDEOIDLE" in output
        elif platform.system() == "Darwin":
            output = subprocess.getoutput("pmset -g | grep sleep")
            return output
        elif platform.system() == "Linux":
            return "Check with `gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout`"
    except Exception:
        return "Unknown"

def get_system_status():
    return {
        "disk_encrypted": is_disk_encrypted(),
        "system_updated": is_system_updated(),
        "antivirus_present": has_antivirus(),
        "sleep_settings": get_sleep_timeout(),
    }
