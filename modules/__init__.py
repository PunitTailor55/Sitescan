"""
"""

from insides 		import *
from cloudflare 	import cloudflare 	as Cloudflare
from crawler 		import googleCrawl 	as GoogleCrawl
from crawler 		import bingCrawl 	as BingCrawl
from crawler 		import manualCrawl 	as ManualCrawl
from reverseip 		import reverseViaHT
from reverseip		import reverseViaYGS
from whois 			import whoIS
from browserspy 	import browserspyRep
from nameservers 	import nameServers
from webspeed 		import websiteSpeed
from subdomains 	import findSubdomains
from shells 		import findShells
from adminpanel 	import findAdminPanel
from banner 		import grabBanner
from dnsdump        import dnsdump
#from a2sv           import a2svmain
from xss       import xssscanmain
from lfiscanner     import LFIscanner
#from advancesubdomain import advancesubdomain
def __init__(self, xssscanmain):
     self.xssscanmain = xssscanmain()
