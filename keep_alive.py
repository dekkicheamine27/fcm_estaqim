import time
import requests
from notifications import sendPush
from const import mixlr_urls, mixlr_titles




previous_status = False
msg = ""




def is_radio_live():
    urls = mixlr_urls
    global msg
    sum = 0
    for key in urls:
        response = requests.get(urls[key])
        sum +=1
        print(sum)
        if response.status_code == 200:
            data = response.json()
            if data.get('is_live', False):
                msg = mixlr_titles[key]
                return True
    
    return False


    
def keep_alive():

    while (True):
        current_status = is_radio_live()

        if current_status and not previous_status:
            
            sendPush("الآن درس مباشر", msg )
        
        
        previous_status = current_status

        time.sleep(5) 