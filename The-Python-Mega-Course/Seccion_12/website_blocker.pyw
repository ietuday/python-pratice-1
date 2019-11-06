#To be able to run the script background, we change the file extension to .pyw
import time
from datetime import datetime as dt
#dt is kinda an alias to datime
host_path = r"C:\Windows\System32\drivers\etc\hosts"
#r before a string indicates that it's a raw string. No special characters

#This variable was used to test the script
#host_temp = "hosts"


#such like \n
redirect = "127.0.0.1"
websites_list = ["www.facebook.com","facebook.com", "youtube.com", "www.youtube.com"]

while True:
    #check if the current time is between working hours
    if (dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16)):
        print("working hours")
        with open(host_path, 'r+') as file:
            content =file.read()
            for website in websites_list:
                if(website in content):
                    pass
                else:
                    line = redirect+"   "+website+"\n"
                    file.write(line)
    else:
        print("Not working hours")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in websites_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
