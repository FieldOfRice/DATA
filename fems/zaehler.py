
# VLS 20250120 zaehler auslesen per bitshake Air/WIFI Lesekopf

import json
import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv

yesterday_value: datetime = datetime.now()
yesterday_prefix: str = yesterday_value.strftime('%Y%m%d_%M%H%S')

debug: bool = False
error: str
spreadsheet_path: str
result_filename: str
tasmota_uri: str
params: str = dict(cmnd='status+10')


def yet() -> str:
  return datetime.now().strftime("%Y%m%d %H%M%S.%f")


# get request to TOASMOTA_URL, which might be http://192.168.178.42/cm?cmnd=status%2010
# list of commands are at https://tasmota.github.io/docs/Commands/#management 
def calculate():
    response = requests.get(url=tasmota_uri,params=params)
    if debug: print(f"{yet()} <<< {response}")
    data=json.loads(response.content)
    if debug: print(f"{yet()} <<< {data}")
    datetime=data['StatusSNS']['Time']
    if debug: print(f"{yet()} <<< {datetime}")
    used_energy=data['StatusSNS']['Itron']['E_in']
    if debug: print(f"{yet()} <<< {used_energy}")
    given_energy=data['StatusSNS']['Itron']['E_out']
    if debug: print(f"{yet()} <<< {given_energy}")
#   power=data['StatusSNS']['Itron']['Power']
#   if debug: print(f"{yet()} <<< {power}")
    with open(result_filename, "w") as file:
        file.write(f"{datetime} {used_energy:.2f} {given_energy:.2f}")


def load_settings() -> bool:
    load_dotenv()
    global spreadsheet_path, result_filename, tasmota_uri, error
    spreadsheet_path = os.getenv('SPREADSHEET_PATH')
    tasmota_uri = os.getenv('TASMOTA_URI')
    prefix = 'Nothing was done. Check your .env file, these are undefined: '
    error = prefix
    if not tasmota_uri:
        error += "TASMOTA_URI "
    if not spreadsheet_path:
        spreadsheet_path=""
        error += "SPREADSHEET_PATH "
    result_filename = spreadsheet_path + datetime.now().strftime('%Y%m%d_%H%M%S_') + 'zaehler.txt'
    return len(error) <= len(prefix)

if __name__ == "__main__":
    if load_settings():
        calculate()
    else:
        print(error)
