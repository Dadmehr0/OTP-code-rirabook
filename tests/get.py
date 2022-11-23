import requests


url = 'https://rirabook.com/wp-admin/admin-ajax.php'
json = {'accountkit': 0,
        'firebase': 0,
        'code': "1"}
data = {'action':'digits_check_mob',
        'countrycode':'+98',
        'mobileNo':9050756226,
        'csrf':'b89b7bcaa9',
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
        'dig_nounce':'b89b7bcaa9',
        'digits_redirect_page':'https://rirabook.com/'}

req = requests.get(url=url)
print(req)