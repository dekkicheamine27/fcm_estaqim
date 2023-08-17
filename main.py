
import time
import requests
from notifications import sendPush



mixlr_api_url = "https://api.mixlr.com/users/8687532?source=embed"
previous_status = False
def is_radio_live():
    response = requests.get(mixlr_api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('is_live', False)
    return False


while (True):
    current_status = is_radio_live()

    if current_status and not previous_status:
        sendPush("Tazgait", "dars is live" )
    
    
    previous_status = current_status

    time.sleep(5) 


   