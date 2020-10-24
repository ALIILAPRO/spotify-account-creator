import requests
import json

import random
import string

import os
import time

from threading import Thread, active_count


script_version = "1.1"
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

	def readfile(self, filename, method):
		with open(filename,method) as f:
			content = [line.strip('\n') for line in f]
			return content

	def countfile(self, filename, method):
		file    = open(filename,method) 
		Counter = 0
		Content = file.read() 
		CoList  = Content.split("\n") 
		for i in CoList: 
			if i: 
				Counter += 1
			
		return Counter

	def getproxy(self):
		r = requests.get('https://xcoder.fun/p.php?r=y')
			
		with open('proxy.txt','w') as fd:
			fd.write(r.text.replace('\n',''))

	def getrandomproxy(self):
		proxies_file = self.readfile('proxy.txt','r')
		proxies = {
			"http":"http://{0}".format(random.choice(proxies_file)),
			"https":"https://{0}".format(random.choice(proxies_file))
		}

		return proxies

	def __init__(self):
		self.settitle(script_title)
		self.clear(script_info)
		self.getproxy()
		self.email                 = input('[#] Enter Email: ')
		self.password              = input('[#] Enter Password: ')
		self.birth_year            = int(input('[#] Enter the birth year (only year): '))
		self.birth_month           = int(input('[#] Enter the birth month (1 - 12): '))
		self.birth_day             = int(input('[#] Enter the birth day (1 - 28): '))
		self.gender                = input('[#] Enter the gender (male or female): ')
		self.threads               = self.countfile('proxy.txt','r')

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

			headers = {
				'User-agent': 'S4A/2.0.15 (com.spotify.s4a; build:201500080; iOS 13.4.0) Alamofire/4.9.0',
				'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
				'Accept': 'application/json, text/plain;q=0.2, */*;q=0.1',
				'App-Platform': 'IOS',
				'Spotify-App': 'S4A',
				'Accept-Language': 'en-TZ;q=1.0',
				'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
				'Spotify-App-Version': '2.0.15'
			}


			url             = 'https://spclient.wg.spotify.com/signup/public/v1/account'
			credentails     = self.gencredentailsmethod()
			data            = 'creation_point=lite_7e7cf598605d47caba394c628e2735a2&password_repeat={0}&platform=Android-ARM&iagree=true&password={1}&gender={2}&key=a2d4b979dc624757b4fb47de483f3505&birth_day={3}&birth_month={4}&email={5}&birth_year={6}'.format(credentails['password'],credentails['password'],credentails['gender'],credentails['birth_day'],credentails['birth_month'],credentails['email'],credentails['birth_year'])
			req             = requests.post(url=url, data=data, headers=headers, proxies=self.getrandomproxy(), timeout=5)
			json_data       = json.loads(req.text)


			if 'status' in json_data:
				if json_data['status'] == 1:
					username = json_data['username']
					if username != '':
						self.clear(script_info)
						print('[>] ACCOUNT CREATED SUCCESSFULLY\n[-] Email:{0}\n[-] Password:{1}\n[-] Username:{2}\n[-] Gender:{3}\n[-] Birth year:{4}\n[-] Birth month:{5}\n[-] Birth day:{6}\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
						with open('reg.txt','a') as f:
							f.write('[INFO ACCOUNT]\nEmail:{0}\nPassword:{1}\nUsername:{2}\nGender:{3}\nBirth year:{4}\nBirth month:{5}\nBirth day:{6}\n___________________\n\n'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
						time.sleep(self.threads)
					else:
						self.creator()
				else:
					self.creator()
			else:
				self.creator()
		except:
			self.creator()


	def start(self):
		while True:
			if active_count() <= self.threads:
				Thread(target=self.creator).start()


if __name__ == "__main__":
	main = Main()
	main.start()
