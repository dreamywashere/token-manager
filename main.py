'''
██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗███████╗
██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████╗
██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ███████║
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
'''

import requests, os, json, random, time, threading, colorama, subprocess, base64, ctypes, websocket, aiosonic, asyncio, re, sys
from random import choice
from colorama import init, Fore, Style
from requests.api import head
from PIL import Image
from discord_webhook import DiscordWebhook
from tasksio import TaskPool
from concurrent.futures import ThreadPoolExecutor


'''
██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
██║   ██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
██║   ██║███████║██████╔╝██║███████║██████╔╝██║     █████╗  ███████╗
╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
 ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██████╔╝███████╗███████╗███████║
  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
'''
init()
thread1 = []
p = []
a = []
count = 0
errors = 0
cyan = Fore.CYAN
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
reset = Fore.RESET

for line in open("Data/tokens.txt"):
    p.append(line.strip("\n"))

with open('config.json') as f:
    data = json.load(f)

folder=r"Data/Avatars"
amounttokens = open("Data/tokens.txt").read().splitlines()
proxies = open("Data/proxies.txt").read().splitlines()
username = open("Data/usernames.txt", encoding="cp437", errors='ignore').read().splitlines()
bio = open("Data/bios.txt", encoding="cp437", errors='ignore').read().splitlines()
loaded_tokens = len(amounttokens)
current = data['tokens_current_password']
email_password_token = data['email_password_token']
#key = data['license-key']


def clear():
    os.system("cls||clear")
'''
██╗   ██╗██╗
██║   ██║██║
██║   ██║██║
██║   ██║██║
╚██████╔╝██║
 ╚═════╝ ╚═╝
'''

def ui():
    motd = requests.get("https://tokenmanager.one/motd.txt").text
    text = f'''{Style.BRIGHT}
    {Fore.LIGHTBLUE_EX}                             ╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╔╦╗╔═╗╔╗╔╔═╗╔═╗╔═╗╦═╗
    {Fore.LIGHTCYAN_EX}                              ║ ║ ║╠╩╗║╣ ║║║  ║║║╠═╣║║║╠═╣║ ╦║╣ ╠╦╝
    {Fore.LIGHTBLUE_EX}                              ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝╚═╝╩╚═
    '''
    print(f'''
    {text}
                                {cyan}github.com/{reset}dreamywashere / {yellow}Thank you for all the support{reset}\n
                                        {green}MOTD:{reset} {blue}{motd}{reset}\n\n

                  [{red}1{reset}] Change Tokens Password    {Fore.LIGHTBLUE_EX}<>{reset}     [{red}6{reset}] HypeSquad Changer (RANDOM)
                  [{red}2{reset}] Change Tokens Username    {Fore.LIGHTBLUE_EX}<>{reset}
                  [{red}3{reset}] Change Tokens Avatar      {Fore.LIGHTBLUE_EX}<>{reset}
                  [{red}4{reset}] Change Bio/About Me       {Fore.LIGHTBLUE_EX}<>{reset}
                  [{red}5{reset}] Scrape Proxies (HTTP)     {Fore.LIGHTBLUE_EX}<>{reset}

        [{yellow}!{reset}] Modules like change username is using the "tokens_current_password" variable from config.json!
        [{yellow}!{reset}] Make sure you scrape proxies before executing any module!
''')
    if email_password_token == True:
        print(f'[{yellow}!{reset}] You are using email:password:token mode!\n\n')
    else: pass

def randomproxy():
    return random.choice(proxies)

def randomusername():
    return random.choice(username)

def randombio():
    return random.choice(bio)

'''

 █████╗ ██╗   ██╗████████╗██╗  ██╗
██╔══██╗██║   ██║╚══██╔══╝██║  ██║
███████║██║   ██║   ██║   ███████║
██╔══██║██║   ██║   ██║   ██╔══██║
██║  ██║╚██████╔╝   ██║   ██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝

'''

def auth():
    print(f'[{green}+{reset}] {cyan}Auth{reset} > Logged in!')
    time.sleep(1)

# auth removed

'''
███╗   ███╗ ██████╗ ██████╗ ███████╗     ██╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝    ███║
██╔████╔██║██║   ██║██║  ██║█████╗      ╚██║
██║╚██╔╝██║██║   ██║██║  ██║██╔══╝       ██║
██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗     ██║
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═╝
                                            
'''

def changepassword2(new):
    global count
    with open('Data/tokens.txt', 'r') as f:
        for line in f:
            y = line.split(":")
            token = y[2].replace('\n', '')
            password = y[1].replace('\n', '')
            email = y[0].replace('\n', '')
            url = 'https://discord.com/api/v6/users/@me'
            headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/users/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
            payload = {"password": password, "new_password": new}
            try:
                print(f'[{blue}+{reset}] Using > {email}:{password}:{token}')
                r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()}).json()
                newtoken = r['token']
                if r['verified'] == False:
                    print(f'{token[:20]} Failed, token is locked!')
                print(f'[{green}+{reset}] New > {email}:{new}:{newtoken[:20]}.. Saved to {cyan}Data/new_tokens.txt{reset}')
                count+=1
                os.system(f'title Changed Password for {count}/{loaded_tokens} tokens.')
                savenew = open('Data/new_tokens.txt', 'a+')
                savenew.write(f'\n{email}:{new}:{newtoken}')
                savenew.close()
            except Exception as e:
                print(f'[{red}!{reset}] {r}')

def changeuser2():
    global count
    with open('Data/tokens.txt', 'r') as f:
        for line in f:
            y = line.split(":")
            token = y[2].replace('\n', '')
            password = y[1].replace('\n', '')
            email = y[0].replace('\n', '')
            url = 'https://discord.com/api/v6/users/@me'
            headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/users/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
            payload = {"password": password, "username": f'{randomusername()}'}
            try:
                r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'https://' + randomproxy()})
                a = r.json()
                tok = a['token']
                print(f'[{green}+{reset}] Changed username for {tok[:20]}...')
                count+=1
                if a['verified'] == False:
                    print(f'{tok[:20]} Failed, token is locked!')
                else:
                    pass
                os.system(f'title Changed Username for {count}/{loaded_tokens} tokens.')
            except:
                print(f'[{red}!{reset}] {r}')

def changeavatar2():
    global count
    with open('Data/tokens.txt', 'r') as f:
        for line in f:
            y = line.split(":")
            token = y[2].replace('\n', '')
            #password = y[1].replace('\n', '')
            #email = y[0].replace('\n', '')
            url = 'https://discord.com/api/v9/users/@me'
            headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/users/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
            try:
                a=random.choice(os.listdir(folder))
                avatar = folder+'\\'+a
                imgg = base64.b64encode(open(f"{avatar}", "rb").read()).decode('ascii')
                r = requests.patch(url=url, headers=headers, json={"avatar": f"data:image/png;base64,{imgg}"}, proxies={"http": 'http://' + randomproxy()}).json()
                tok = r['token']
                print(f'[{green}+{reset}] Changed avatar for {tok[:20]}...')
                count+=1
                if r['verified'] == False:
                    print(f'{tok[:20]} Failed, token is locked!')
                os.system(f'title Changed Avatar for {count}/{loaded_tokens} tokens.')
            except Exception as e:
                print(f'[{red}!{reset}] {r}')

def changebio2():
    global count
    with open('Data/tokens.txt', 'r') as f:
        for line in f:
            y = line.split(":")
            token = y[2].replace('\n', '')
            #password = y[1].replace('\n', '')
            #email = y[0].replace('\n', '')
            url = 'https://discord.com/api/v9/users/@me'
            headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/users/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
            payload = {"bio": f'{randombio()}'}
            try: 
                r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()}).json()
                tok = r['token']
                print(f'[{green}+{reset}] Changed bio for {tok[:20]}...')
                count+=1
                if r['verified'] == False:
                    print(f'{tok[:20]} Failed, token is locked!')
                os.system(f'title Changed Bio for {count}/{loaded_tokens} tokens.')
            except Exception as e:
                print(f'[{red}!{reset}] {r}')

def hypesquad2():
    global count
    with open('Data/tokens.txt', 'r') as f:
        for line in f:
            y = line.split(":")
            token = y[2].replace('\n', '')
            #password = y[1].replace('\n', '')
            #email = y[0].replace('\n', '')
            url = "https://discord.com/api/v9/hypesquad/online"
            headers = {"Authorization": token}
            payload = {'house_id': f'{random.randint(1, 3)}'}
            try:
                r = requests.post(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()})
                print(f'[{green}+{reset}] Changed hypesquad')
                count+=1
                os.system(f'title Changed HypeSquad for {count}/{loaded_tokens} tokens.')
                if r['verified'] == False:
                    print(f'Failed, token is locked!')
            except Exception as e:
                pass


'''

███╗   ███╗ ██████╗ ██████╗ ███████╗    ██████╗ 
████╗ ████║██╔═══██╗██╔══██╗██╔════╝    ╚════██╗
██╔████╔██║██║   ██║██║  ██║█████╗       █████╔╝
██║╚██╔╝██║██║   ██║██║  ██║██╔══╝      ██╔═══╝ 
██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗    ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚══════╝
                                                
'''


def changepassword(tokens, old, new):
    global count
    url = 'https://discord.com/api/v6/users/@me'
    headers = {
    "Authorization": tokens,
    "accept": "*/*",
    "accept-language": "en-US",
    "connection": "keep-alive",
    "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
    "DNT": "1",
    "origin": "https://discord.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://discord.com/users/@me",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
    payload = {"password": old, "new_password": new}
    try:
        r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()}).json()
        newtoken = r['token']
        if r['verified'] == False:
            print(f'{tokens[:20]} Failed, token is locked!')
        print(f'[{green}+{reset}] New token > {newtoken[:20]}.. Saved to {cyan}Data/new_tokens.txt{reset}')
        savenew = open('Data/new_tokens.txt', 'a+')
        savenew.write(f'\n{newtoken}')
        savenew.close()
        count+=1
        os.system(f'title Changed Password for {count}/{loaded_tokens} tokens.')
    except Exception as e:
        print(f'[{red}!{reset}] {r}')

def changeuser(tokens):
    global count
    url = 'https://discord.com/api/v6/users/@me'
    headers = {
    "Authorization": tokens,
    "accept": "*/*",
    "accept-language": "en-US",
    "connection": "keep-alive",
    "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
    "DNT": "1",
    "origin": "https://discord.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://discord.com/users/@me",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
    payload = {"password": current, "username": f'{randomusername()}'}
    try:
        r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()}).json()
        tok = r['token']
        print(f'[{green}+{reset}] Changed username for {tok[:20]}...')
        count+=1
        if r['verified'] == False:
            print(f'{tok[:20]} Failed, token is locked!')
        else:
            pass
        os.system(f'title Changed Username for {count}/{loaded_tokens} tokens.')
    except Exception as e:
        print(f'[{red}!{reset}] {r}')

def changeavatar(tokens):
    global count
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
    "Authorization": tokens,
    "accept": "*/*",
    "accept-language": "en-US",
    "connection": "keep-alive",
    "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
    "DNT": "1",
    "origin": "https://discord.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://discord.com/users/@me",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
    try:
        a=random.choice(os.listdir(folder))
        avatar = folder+'\\'+a
        imgg = base64.b64encode(open(f"{avatar}", "rb").read()).decode('ascii')
        r = requests.patch(url=url, headers=headers, json={"avatar": f"data:image/png;base64,{imgg}"}, proxies={"http": 'http://' + randomproxy()}).json()
        tok = r['token']
        print(f'[{green}+{reset}] Changed avatar for {tok[:20]}...')
        count+=1
        if r['verified'] == False:
            print(f'{tok[:20]} Failed, token is locked!')
        os.system(f'title Changed Avatar for {count}/{loaded_tokens} tokens.')
    except Exception as e:
        print(f'[{red}!{reset}] {r}')

def changebio(tokens):
    global count
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
    "Authorization": tokens,
    "accept": "*/*",
    "accept-language": "en-US",
    "connection": "keep-alive",
    "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
    "DNT": "1",
    "origin": "https://discord.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://discord.com/users/@me",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
    payload = {"bio": f'{randombio()}'}
    try: 
        r = requests.patch(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()}).json()
        tok = r['token']
        print(f'[{green}+{reset}] Changed bio for {tok[:20]}...')
        count+=1
        if r['verified'] == False:
            print(f'{tok[:20]} Failed, token is locked!')
        os.system(f'title Changed Bio for {count}/{loaded_tokens} tokens.')
    except Exception as e:
        print(f'[{red}!{reset}] {r}')

def scrapeproxy():
    r1 = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt")
    f = open("Data/proxies.txt", 'wb')
    f.write(r1.content)
    print(f"[{yellow}!{reset}] Scraped successfully, saved to Data/proxies.txt!")
    time.sleep(2)

def hypesquad(tokens):
    global count
    url = "https://discord.com/api/v9/hypesquad/online"
    headers = {"Authorization": tokens}
    payload = {'house_id': f'{random.randint(1, 3)}'}
    try:
        r = requests.post(url=url, headers=headers, json=payload, proxies={"http": 'http://' + randomproxy()})
        print(f'[{green}+{reset}] Changed hypesquad')
        count+=1
        os.system(f'title Changed HypeSquad for {count}/{loaded_tokens} tokens.')
        if r['verified'] == False:
            print(f'Failed, token is locked!')
    except Exception as e:
        pass


'''
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                          
'''

auth()


def menu():
    while True:
        clear()
        print(f'Loaded {cyan}{len(amounttokens)}{reset} tokens.')
        print(f'Loaded {cyan}{len(proxies)}{reset} proxies.')
        print(f'Loaded {cyan}{len(username)}{reset} usernames.')
        print(f'Loaded {cyan}{len(bio)}{reset} bios/about me')
        print(f'Loaded {cyan}{len(os.listdir(folder))}{reset} avatars\n')
        os.system(f'title Token Manager - Main Menu')
        ui()
        answer = input("> ")
        if answer == "1":
            if email_password_token == True:
                print(f'[{yellow}!{reset}] Using email:password:token module!')
                new = input('New Password: ')
                changepassword2(new)
                input("Process done, press enter to return to main menu!")
                time.sleep(3)
            else:
                old = input('Password: ')
                new = input('New Password: ')
                for tokens in p:
                    thread = threading.Thread(target=changepassword, args=(tokens,old,new), daemon=True)
                    thread.start()
                    time.sleep(0.40)
                    input("Process done, press enter to return to main menu!")
                time.sleep(3)
        elif answer == "2":
            if email_password_token == True:
                print(f'[{yellow}!{reset}] Using email:password:token module!')
                changeuser2()
                input("Process done, press enter to return to main menu!")
                time.sleep(3)
            else:
                for tokens in p:
                    thread = threading.Thread(target=changeuser, args=(tokens,), daemon=True)
                    thread.start()
                    time.sleep(0.50)
            input("Process done, press enter to return to main menu!")
            time.sleep(3)
        elif answer == "3":
            if email_password_token == True:
                print(f'[{yellow}!{reset}] Using email:password:token module!')
                print(f'[{yellow}!{reset}] If is slow, this depends on your internet connection')
                changeavatar2()
                input("Process done, press enter to return to main menu!")
                time.sleep(3)
            else:
                print(f'[{yellow}!{reset}] If is slow, this depends on your internet connection')
                for tokens in p:
                    thread = threading.Thread(target=changeavatar, args=(tokens,), daemon=True)
                    thread.start()
                    time.sleep(0.40)
            input("Process done, press enter to return to main menu!")
        elif answer == "4":
            if email_password_token == True:
                print(f'[{yellow}!{reset}] Using email:password:token module!')
                changebio2()
                input("Process done, press enter to return to main menu!")
                time.sleep(3)
            else:
                for tokens in p:
                    thread = threading.Thread(target=changebio, args=(tokens,), daemon=True)
                    thread.start()
                    time.sleep(0.40)
            input("Process done, press enter to return to main menu!")
            time.sleep(3)
        elif answer == "5":
            scrapeproxy()
            input("Process done, press enter to return to main menu!")
        elif answer == "6":
            if email_password_token == True:
                print(f'[{yellow}!{reset}] Using email:password:token module!')
                hypesquad2()
                print('Process done, press enter to return to main menu!')
                input("")
            for tokens in p:
                thread = threading.Thread(target=hypesquad, args=(tokens,), daemon=True)
                thread.start()
                time.sleep(0.10)
            print('Process done, press enter to return to main menu!')
            input('')
        else:
            print(f'[{yellow}!{reset}] Invalid Choice!')
            input("")
            time.sleep(2)

menu()

# I made that project cuz i was bored and still had 60+ customers lmfao
# Note that i post the src cuz i dont have time to code anymore
# Maybe is a little buggy, try to add new features to it cuz is not hard