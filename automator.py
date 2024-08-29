from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote

import os
import sys
import csv

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")

if sys.platform == "win32":
   options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")
else:
   options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")


os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Anirudh Bagri     ******")
print("*****           www.github.com/anirudhbagri         ******")
print("*****           Enhanced by Ricardo J. Nunes        ******")
print("*****          www.github.com/ricardo-jnunes        ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

f = open("message.txt", "r", encoding="iso-8859-1")
original_message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + original_message)
print("\n" + style.RESET)

dict = {}
line_count = 0
with open('numbers.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        message = original_message.replace("{...}",row[0].strip())
        dict[row[1].strip()] = quote(message)
        print(style.CYAN + 'Personalizing message for: ' + row[0].strip()  + ' number: ' + row[1].strip() + style.RESET)
        line_count += 1

print(style.RED + 'We found ' + str(line_count) + ' numbers in the file' + style.RESET)

delay = 30
driver = webdriver.Chrome( service=ChromeService(ChromeDriverManager().install()), options=options )
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, (number, message) in enumerate(dict.items()):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), line_count, number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']")))
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
driver.close()
