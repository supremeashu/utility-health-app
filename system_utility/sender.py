import requests
from config import API_ENDPOINT, MACHINE_ID

def send_report(data):
    payload = {
        "machine_id": MACHINE_ID,
        "report": data,
    }
    try:
        res = requests.post(API_ENDPOINT, json=payload)
        return res.status_code == 200
    except requests.RequestException as e:
        print("Error sending data:", e)
        return False
