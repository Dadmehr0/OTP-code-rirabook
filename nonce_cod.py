def once_kid_suop(kid):
    #Import libraries
    import requests
    from bs4 import BeautifulSoup
    import os 


    #Request URL
    page = requests.get("https://rirabook.com/?login=true&page=1&redirect_to=https%3A%2F%2Frirabook.com%2F")

    #Fetch webpage
    soup = BeautifulSoup(page.content,"html.parser")

    nonce_code = soup.find("script",{"id":"digits-login-script-js-extra"}).text.replace("\n","").strip()
    print(nonce_code)
    print("                                   / \ ")
    print("                                    |  ")
    print("                                    |  ")
