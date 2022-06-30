import requests
import json

import random
import string

import os
import time

from threading import Thread, active_count


script_version = "2.0"
script_title   = "Spotify Account Creator By ALIILAPRO"
script_info    = f'''
	 ..: {script_title} :..
 
 [!] ABOUT SCRIPT:
 [-] With this script, you can register on Spotify.com
 [-] Version: {script_version}
 --------
 [!] ABOUT CODER:
 [-] ALIILAPRO, Programmer and developer from IRAN.
 [-] Website  : aliilapro.github.io
 [-] Telegram : aliilapro
 --------
'''
class Main:

	def clear(self, text):
		os.system('cls' if os.name == 'nt' else 'clear')
		print(text)

	def settitle(self, title_name:str):
		os.system("title {0}".format(title_name))

	def __init__(self):
		self.settitle(script_title)
		self.clear(script_info)
		self.email                 = input('[#] Enter Email: ')
		self.password              = input('[#] Enter Password: ')
		self.birth_year            = int(input('[#] Enter the birth year (only year): '))
		self.birth_month           = int(input('[#] Enter the birth month (1 - 12): '))
		self.birth_day             = int(input('[#] Enter the birth day (1 - 28): '))
		self.gender                = input('[#] Enter the gender (male or female): ')
		self.threads               = 10
		

	def gencredentailsmethod(self):
		credentails = {}
		credentails['gender']      = self.gender
		credentails['birth_year']  = self.birth_year
		credentails['birth_month'] = self.birth_month
		credentails['birth_day']   = self.birth_day
		credentails['password']    = self.password
		username                   = string.ascii_letters + string.digits
		username                   = ''.join(random.choice(username) for i in range(random.randint(7,11)))
		credentails['username']    = username
		credentails['email']       = self.email

		return credentails

	def creator(self):
		try:
			session = requests.Session()

			headers = {
				"Accept": "*/*",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4280.141 Safari/537.36",
				"Content-Type": "application/x-www-form-urlencoded",
				"Referer": "https://www.spotify.com/"
			}

			credentails     = self.gencredentailsmethod()
			data            = 'birth_day={0}&birth_month={1}&birth_year={2}&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={3}&email={4}&gender={5}&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={6}&password_repeat={7}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0'.format(credentails['birth_day'],credentails['birth_month'],credentails['birth_year'],credentails['username'],credentails['email'],credentails['gender'],credentails['password'],credentails['password'])
			req             = session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers=headers, data=data)
			if "login_token" in req.text:
				login_token = req.json()['login_token']

			else:
				return

			r = session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
			crsf = r.text.split('csrfToken":"')[1].split('"')[0]

			headers = {
				"Accept": "*/*",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
				"Content-Type": "application/x-www-form-urlencoded",
				"X-CSRF-Token": crsf,
				"Host": "www.spotify.com"
			}
			session.post("https://www.spotify.com/api/signup/authenticate", headers=headers, data="splot=" + login_token)
			headers = {
				"accept": "application/json",
				"Accept-Encoding": "gzip, deflate, br",
				"accept-language": "en",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
				"spotify-app-version": "1.1.52.204.ge43bc405",
				"app-platform": "WebPlayer",
				"Host": "open.spotify.com",
				"Referer": "https://open.spotify.com/"
			}

			r = session.get("https://open.spotify.com/get_access_token?reason=transport&productType=web_player", headers=headers)
			token = r.json()["accessToken"]
			self.settitle(script_title)
			self.clear(script_info)
			print('[>] ACCOUNT CREATED SUCCESSFULLY\n[-] Email:{0}\n[-] Password:{1}\n[-] Username:{2}\n[-] Gender:{3}\n[-] Birth year:{4}\n[-] Birth month:{5}\n[-] Birth day:{6}\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
			with open('ACCOUNT-SPOTIFY.txt','a') as f:
				f.write('[INFO ACCOUNT]\nEmail:{0}\nPassword:{1}\nUsername:{2}\nGender:{3}\nBirth year:{4}\nBirth month:{5}\nBirth day:{6}\nToken:{7}\n___________________\n\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day'],token))
		except Exception as e:
			print(e)

	def start(self):
		while True:
			if active_count() < self.threads:
				Thread(target=self.creator).start()

if __name__ == "__main__":
	main = Main()
	main.start()
