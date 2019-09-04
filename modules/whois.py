"""
"""

from insides.colors 	import *
from bs4 				import BeautifulSoup
from insides.functions 	import _headers, write, Request, removeHTTP, addHTTP
import re, 		 os
import requests, json

def whoIS(website):
	website 	= removeHTTP(website)
	url 		= "https://www.whois.com/whois/{site}".format(site=website)
	try:
		request 	= Request(url, _timeout=5, _encode=None)
		bs 		= BeautifulSoup(request, 'html.parser')
		result 		= bs.find_all('pre', {'class': 'df-raw'})[0].text.encode('UTF-8')
		print("\r{output}".format(output=c + result))
	except:
		write(var="!", color=r, data="Sorry, whois cannot be performed right now...!!! :[")


