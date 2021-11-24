from os import system as sys
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS
import random
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
all_col = [red,green,orange,cyan,lightgrey,lightred,lightgreen,yellow,lightcyan]
ran = random.choice(all_col)
sys('clear')


class ip:
    def banner(self):
        print (ran ,'''
   ________        __            .___        
  /  _____/  _____/  |_          |   |_____  
 /   \  ____/ __ \   __\  ______ |   \____ \ 
 \    \_\  \  ___/|  |   /_____/ |   |  |_> >
  \______  /\___  >__|           |___|   __/ 
         \/     \/                   |__|    
______________________________________________
''')

        print(ran,"\n\n","---"*3," [+] Follow me on instagram @saadkhan041 ","---"*3,"\n\n")
        print(ran,"\n\n","---"*3," [+] V_2.0 ","---"*3,"\n\n")

    def public_ip(self):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
        url = Request('https://www.myip.com/',headers=headers)
        openurl = urlopen(url).read(99999)
        soup = BS(openurl , 'html.parser')
        for i in soup.findAll('span',{'id':'ip'}):
            print (f'{ran} [+] Public Ip > {i.text}')

    def privet_ip(self):
        sys("printf ' [+] Privet Ip > ';ifconfig wlan0 | grep 'netmask' | awk -F ' ' '{print $2}'")

    def localhost(self):
        print(ran," [+] LocalHost > 127.0.0.1\n")

ip = ip()
ip.banner()
ip.public_ip()
ip.privet_ip()
ip.localhost()

    
    
