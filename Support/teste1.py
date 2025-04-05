from requests import post
from colorama import Fore
from threading import Thread


url = "http://advanced.bancocn.com/admin/index.php"

data = {"user": "admin", "password": "senhafoda"}

resp = post(url, data)
html = resp.text

if "Logout" in html:
    print("ok")

else:
    print("nao")