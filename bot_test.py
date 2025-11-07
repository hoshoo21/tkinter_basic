# from dotenv import load_dotenv
# import os 
# import requests

# load_dotenv()

# telegram_token = os.getenv("BOT_TELEGRAM_TOKEN")

# tel_group_id = "@testgroup_nav" 

# url = f"https://api.telegram.org/bot{telegram_token}/getUpdates"
# data = {"chat_id": tel_group_id, "text": "test message"}

# respone = requests.request('get',url=url,data=data)

# print (respone)

import requests

r = requests.get("https://api.telegram.org")
print(r.status_code)

url = "https://api.telegram.org/bot8278695614:AAENtMMG16xETYg6tWR7tT4kmi5VNBnKJ0g/getUpdates"

payload = {}
headers = {}

response = requests.get( url)

print(response.text)