import requests
import json

TBA_AUTH_KEY = "aFWGp51fGBjVwt1eHp2v5rPbe6OxmLTJlPnF91YfejPFQsH8miJVotJWkI55E19e"
TBA_BASE_ENDPOINT = "https://www.thebluealliance.com/api/v3"

def call_tba_api(url):
    r = requests.get(f"{TBA_BASE_ENDPOINT}/{url}", headers={"X-TBA-Auth-Key": TBA_AUTH_KEY})

    return r.json()


def update_event_json():
    with open(f"./2024mibat.json", "w+") as jsonFile:
        data = call_tba_api(f"/event/2024mibat/teams")
        print(json.dumps(data))
        jsonFile.write(json.dumps(data))

update_event_json()