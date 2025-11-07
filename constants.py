import pytz
import os
time_interval = 20
PINCODE = "801503"
msg = "Blank"
tele_auth_token = os.environ[''] 
     
IST = pytz.timezone('Asia/Karachi')           
slot_found =  False                 
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}

