import requests
import json

import random
import string

import os
import time

script_version = "3.0"
script_title   = "Spotify Account Creator By ALIILAPRO"
script_info    = f'''
	 ..: {script_title} :..
 
 [!] ABOUT SCRIPT:
 [-] With this script, you can register on Spotify.com
 [-] Version: {script_version}
 --------
 [!] ABOUT CODER:
 [-] ALIILAPRO, Programmer and developer from IRAN.
 [-] Github   : https://github.com/aliilapro
 [-] Project  : https://github.com/ALIILAPRO/spotify-account-creator
 [-] Telegram : https://t.me/aliilapro
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
				"Referer": "https://www.spotify.com/",
				"Accept-Encoding": "gzip, deflate, br",
				"accept-language": "en",
				"Host": "spclient.wg.spotify.com"
			}

			credentails     = self.gencredentailsmethod()
			data            = 'birth_day={0}&birth_month={1}&birth_year={2}&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={3}&email={4}&gender={5}&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={6}&password_repeat={7}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0'.format(credentails['birth_day'],credentails['birth_month'],credentails['birth_year'],credentails['username'],credentails['email'],credentails['gender'],credentails['password'],credentails['password'])
			req             = session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers=headers, data=data)
			if "login_token" in req.text:
				token = req.json()['login_token']
				self.settitle(script_title)
				self.clear(script_info)
				print('[>] ACCOUNT CREATED SUCCESSFULLY\n[-] Email:{0}\n[-] Password:{1}\n[-] Username:{2}\n[-] Gender:{3}\n[-] Birth year:{4}\n[-] Birth month:{5}\n[-] Birth day:{6}\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
				with open('ACCOUNT-SPOTIFY.txt','a') as f:
				    f.write('[INFO ACCOUNT]\nEmail: {0}\nPassword: {1}\nUsername: {2}\nGender: {3}\nBirth year: {4}\nBirth month: {5}\nBirth day: {6}\nToken: {7}\n___________________\n\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day'],token))

			else:
				print("[>] ERROR")		

		except Exception as e:
			print(e)

if __name__ == "__main__":
	main = Main()
	main.creator()
