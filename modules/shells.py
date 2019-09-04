"""
"""

from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def findShells(website):
	website = addHTTP(website)
	shells = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/shells", _timeout=6, _encode=True).split("\n")
	print("{}{:<92}| {:<50}".format(c, "URL", "STATUS"))
	for _shells in shells:
		if len(_shells) != 0:
			combo = website + "/" + _shells
			try:
				resp = requests.get(combo, timeout=5, headers=_headers, allow_redirects=False).status_code
				if resp == 200:
					print("{}{:<92}| {:<50}".format(g, combo, resp))
				elif resp == 301:
					print("{}{:<92}| {:<50}".format(r, combo, "404"))
				elif resp == 500 or resp == 502:
					print("{}{:<92}| {:<50}".format(c, combo, "404"))
				else:
					print("{}{:<92}| {:<50}".format(r, combo, "404"))
			except Exception:
				print("{}{:<92}| {:<50}".format(r, combo, "404"))