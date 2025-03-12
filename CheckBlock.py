from instagrapi import Client
from instagrapi.exceptions import UserNotFound,ClientError
from telegram import Bot
import time
import random
import requests
from art import text2art


print(text2art(";) Check Block "))
time.sleep(0.5)
print(text2art("Programmed    by"))
time.sleep(0.5)
print(text2art(" heho.9 "))


token_bot = input("\nEnter Token Bot here : ")
time.sleep(0.5)
chat_id = input("\nEnter chat id here : ")
time.sleep(0.5)
username = input("\nEnter Username : ")
time.sleep(0.5)
Password = input("\nEnter Password : ")
time.sleep(0.5)
targetuser = input("Target User : ")
s = requests.session()
# proxy = [
#         f"http://{username}:{Password}@23.227.38.246:80",
#         ]
api_bot1 = token_bot
def send_masseg(text):
        url = f"https://api.telegram.org/bot{api_bot1}/sendMessage?chat_id={chat_id}&text={text}"
        time.sleep(2)
        requests.get(url)
cl = Client()
userAgent = [
    f"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
]
def safe_check():

            
            try:

                cl.delay_range = [2,3]
                print( cl.login(username=username,password=Password))
                
                
                cl.user_info_by_username_v1(targetuser)
                
                print(f"Not Bloked {targetuser} ")
                
                send_masseg(f"{targetuser}\tالحساب فك الحظر")
            except UserNotFound as e:
            
                send_masseg(f"{targetuser}\tالحساب حاظرك")
                print(f"{e}Acc Bloked")
                
                
            except ClientError as e:
                if "User not found" in str(e):
                    print("محظور او غير موجود الحساب")
                else:
                    print(f"{e}\nfiled error\n);")
        
if __name__ =="__main__":
    while True:
        safe_check()
        time.sleep(60)
# send_masseg("Hi")


    