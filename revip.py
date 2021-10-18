#!/usr/bin/env python3

import requests
import os
import threading
import json
from socket import gethostbyname
from colorama import Fore, Back, Style

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

def RevIP():
	
	Agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
	
	print(cyan)
	print('''
	
   ____                                ___ ____  
   |  _ \ _____   _____ _ __ ___  ___  |_ _|  _ \ 
   | |_) / _ \ \ / / _ \ '__/ __|/ _ \  | || |_) |
   |  _ <  __/\ V /  __/ |  \__ \  __/  | ||  __/ 
   |_| \_\___| \_/ \___|_|  |___/\___| |___|_|    
   
          By : Wan5550
          Github : github.com/wannazid
                                   
	''')
	print(batas)                 
	input_list = input(tai+'[!] List > ')
	input_save = input(tai+'[!] Save Result .txt > ')
	print(batas)
	
	kosong = []
	op = open(input_list,"r").read().splitlines()
	for wans in op:
		if wans not in kosong:
			kosong += [wans]
		else:
			pass
	open(input_list,"w").write("")
	for wans in kosong:
		open(input_list,"a").write(wans+"\n")
		
	dom_ip = open(input_list,'r').read().splitlines()
	for ips in dom_ip:
		try:
			ke_ip = gethostbyname(ips)
			savefile = open('result_ip.txt','a').write(ke_ip+'\n')
		except:
			pass
	open_ip = open('result_ip.txt','r').read().splitlines()
	for ip in open_ip:
		try:
			req = requests.get('https://sonar.omnisint.io/reverse/'+ip,headers=Agent).text
			parse = json.loads(req)
			print(f"{hijau}[#] Reverse {ip} > [{str(len(parse))} Domain]")
			for sampah in parse:
				hapus = sampah.replace("www.", "").replace('error:Invalid IPv4 address','').replace('api.', '').replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('ns3.','').replace('ns4.','').replace('autodiscover.', '')
				open(input_save,'a').write(hapus+'\n')
		except:
			print(f'{merah}[#] Reverse {ip} > Error')
	os.remove('result_ip.txt')
	print(batas)
t = threading.Thread(target=RevIP)
t.start()