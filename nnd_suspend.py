import datetime
import time
import requests

import pytz  # Import thư viện pytz để làm việc với múi giờ

from time import sleep
from random import randint

suspended = '🟣Vietnam is still closed'

api_telegram_TOKEN = '6699284669:AAG2DgdsdGy3f16jh1yAI5yn1fTTLolx1qY' #Bot New Zealand
vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')

def send_to_telegram(text):
	# Lấy thời gian hiện tại
	now = datetime.datetime.now(vietnam_timezone)
	date_str = now.strftime("%d/%m/%Y")
	time_str = now.strftime("%H:%M:%S")

	# Tạo nội dung tin nhắn với thời gian
	text_with_timestamp = f"{text}\n🟣{date_str} {time_str}"

	url_req = f"https://api.telegram.org/bot{api_telegram_TOKEN}/sendMessage?chat_id={'-1001841805787'}&text={text_with_timestamp}"
	results = requests.get(url_req)
	#print(results.json())

def send_msg_admin(text):
	# Lấy thời gian hiện tại
	now = datetime.datetime.now(vietnam_timezone)
	date_str = now.strftime("%d/%m/%Y")
	time_str = now.strftime("%H:%M:%S")

	# Tạo nội dung tin nhắn với thời gian
	text_with_timestamp = f"{text}\n🟣{date_str} {time_str}"

	url_req = f"https://api.telegram.org/bot{api_telegram_TOKEN}/sendMessage?chat_id={'-994892357'}&text={text_with_timestamp}"
	results = requests.get(url_req)
	#print(results.json())

def send_suspended(suspended):
	while True:
		start_time = time.time()
		send_to_telegram(suspended)
		print(suspended)
		while True:
			x = randint(1,6)
			print('So s de auto click: {}'.format(x))
			sleep(x)
			elapsed_time = time.time() - start_time
			#print("elapsed_time:{0}".format(elapsed_time) + " [sec]")
			if elapsed_time > 59:
				print('1 minutes of notice and delete. Continue!')
				break
		print("elapsed_time:{0}".format(elapsed_time) + " [sec]")

while True:
	try:
		send_suspended(suspended)
	except Exception as ex:
		print('Exception block: Try send suspended', ex)
		send_msg_admin('🔴Exception block: Try send suspended')
		time.sleep(10)








