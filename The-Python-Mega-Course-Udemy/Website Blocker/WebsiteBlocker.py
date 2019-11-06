# host file directory /etc/hosts
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"/etc/hosts"## r implies that we are passing a raw string as in \n is not treated as a newline character
website_list = ["www.facebook.com", "facebook.com"]
redirect = "127.0.0.1"
while True:
	if False: #dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working hours..")
		with open(hosts_path, 'r+') as file: #r+ means reading and writing both can take place
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("Fun Hours...")
	time.sleep(5)
