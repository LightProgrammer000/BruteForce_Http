from requests import post
from colorama import Fore
from threading import Thread


url = "http://testphp.vulnweb.com/userinfo.php"

data = {"uname": "test", "pass": "test"}

resp = post(url, data)
html = resp.text

if "logout" in html:
    print("ok")

else:
    print("nao")