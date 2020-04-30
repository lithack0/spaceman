from pprint import pprint
from termcolor import cprint
from pyfiglet import figlet_format
import requests
cprint(figlet_format("\t    SPACEMAN"),"yellow",attrs=["bold"])
print()
print("\033[33;1m [1].Numbers of People in space right now !!")
print()
print("\033[33;1m [2].Names of People in space right now !!")
print()
a=input(" ")
if a=="1":
	print()
	r=requests.get("http://api.open-notify.org/astros.json")
	j=r.json()
	a=j["number"]
	print(a,"People in space right now")
if a=="2":
	print()
	r=requests.get("http://api.open-notify.org/astros.json")
	j=r.json()
	a=j["people"][0]["name"]
	print(a)
	a=j["people"][1]["name"]
	print(a)
	a=j["people"][2]["name"]
	print(a)
