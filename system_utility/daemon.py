import time
import json
from checker import get_system_status
from sender import send_report
from config import DAEMON_INTERVAL_MINUTES

def run_daemon():
    last_status = None
    while True:
        current_status = get_system_status()
        if json.dumps(current_status, sort_keys=True) != json.dumps(last_status, sort_keys=True):
            print("Change detected. Sending update...")
            send_report(current_status)
            last_status = current_status
        else:
            print("No change.")
        time.sleep(DAEMON_INTERVAL_MINUTES * 60)
