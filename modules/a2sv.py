#/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
import argparse
import socket
import datetime
from urlparse import urlparse
sys.path.append(os.path.dirname( os.path.abspath( __file__ ))+"/module")
from M_ccsinjection import *
from M_heartbleed import *
from M_poodle import *
from M_freak import *
from M_logjam import *
from M_drown import *
from M_crime import *
from M_anonymous import *
from C_display import *
from insides.functions import WWW


#==============================================
displayMode=0
targetMode=0
output_ck=0
output_path="./a2sv_output.txt"

targetfileList = []
# Version 
myPath=os.path.dirname( os.path.abspath( __file__ ))
vfp = open(myPath+"/version","r")  #Version File Pointer
a2sv_version = vfp.read()
a2sv_version = a2sv_version.rstrip()
#==============================================

global targetIP
global port
global ccs_result
global heartbleed_result
global poodle_result
global freak_result
global logjam_result
global drown_result
global crime_result
global anonymous_result

# Set Result Val
# -1: Not Scan
# 0x00: Not Vuln
# 0x01: Vuln
ccs_result = "-1"
heartbleed_result = "-1"
poodle_result = "-1"
freak_result = "-1"
logjam_result = "-1"
drown_result = "-1"
crime_result = "-1"
anonymous_result = "-1"
#===========================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
VIOLET = '\033[0;35m'
END = '\033[0m'

## Report Table
class TablePrinter(object):
    "Print a list of dicts as a table"
    def __init__(self, fmt, sep=' ', ul=None):
        """        
        @param fmt: list of tuple(heading, key, width)
                        heading: str, column label
                        key: dictionary key to value to print
                        width: int, column width in chars
        @param sep: string, separation between columns
        @param ul: string, character to underline column label, or None for no underlining
        """
        super(TablePrinter,self).__init__()
        self.fmt   = str(sep).join('{lb}{0}:{1}{rb}'.format(key, width, lb='{', rb='}') for heading,key,width in fmt)
        self.head  = {key:heading for heading,key,width in fmt}
        self.ul    = {key:str(ul)*width for heading,key,width in fmt} if ul else None
        self.width = {key:width for heading,key,width in fmt}

    def row(self, data):
        return self.fmt.format(**{ k:str(data.get(k,''))[:w] for k,w in self.width.iteritems() })

    def __call__(self, dataList):
        _r = self.row
        res = [_r(data) for data in dataList]
        res.insert(0, _r(self.head))
        if self.ul:
            res.insert(1, _r(self.ul))
        return '\n'.join(res)
########################

def mainScreen():
    os.system('cls' if os.name=='nt' else 'clear')
def runScan(s_type):
    global ccs_result
    global heartbleed_result
    global poodle_result
    global freak_result
    global logjam_result
    global drown_result
    global crime_result
    global anonymous_result

    
    print ""
    # SSL Check Logic --------------------------- 
    print(GREEN+"[INF] Check the SSL.."+END)
    result = subprocess.Popen(['timeout','4','openssl','s_client','-connect',targetIP+":"+str(port)], stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
    if "Connection refused" in result:
        print(RED+"[RES] This target does not support SSL.."+END)
    # ------------------------------------------------------
    else:
        print(GREEN+"[RES] This target supports SSL.."+END)
        if s_type == "anonymous":
            print(GREEN+"[INF] Scan Anonymous Cipher.."+END)
            anonymous_result = m_anonymous_run(targetIP,port)
            print(GREEN+"[RES] Anonymous Cipher :: "+anonymous_result+END)
        elif s_type == "crime":
            print(GREEN+"[INF] Scan CRIME(SPDY).."+END)
            crime_result = m_crime_run(targetIP,port)
            print(GREEN+"[RES] CRIME(SPDY) :: "+crime_result+END)
        elif s_type == "heart":
            print(GREEN+"[INF] Scan HeartBleed.."+END)
            heartbleed_result = m_heartbleed_run(targetIP,port)
            print(GREEN+"[RES] HeartBleed :: "+heartbleed_result+END)
        elif s_type == "ccs":
            print(GREEN+"[INF] Scan CCS Injection.."+END)
            ccs_result = m_ccsinjection_run(targetIP,port)
            print(GREEN+"[RES] CCS Injection :: "+ccs_result+END)
        elif s_type == "poodle":
            print(GREEN+"[INF] Scan SSLv3 POODLE.."+END)
            poodle_result = m_poodle_run(targetIP,port)
            print(GREEN+"[RES] SSLv3 POODLE :: "+poodle_result+END)
        elif s_type == "freak":
            print(GREEN+"[INF] Scan OpenSSL FREAK.."+END)
            freak_result = m_freak_run(targetIP,port)
            print(GREEN+"[RES] OpenSSL FREAK :: "+freak_result+END)
        elif s_type == "logjam":
            print(GREEN+"[INF] Scan OpenSSL LOGJAM.."+END)
            logjam_result = m_logjam_run(targetIP,port)
            print(GREEN+"[RES] OpenSSL LOGJAM :: "+logjam_result+END)
        elif s_type == "drown":
            print(GREEN+"[INF] Scan SSLv2 DROWN.."+END)
            logjam_result = m_drown_run(targetIP,port)
            print(GREEN+"[RES] SSLv2 DROWN :: "+drown_result+END)
        else:
            print(GREEN+"[INF] Scan Anonymous Cipher.."+END)
            anonymous_result = m_anonymous_run(targetIP,port)
            print(GREEN+"[INF] Scan CRIME(SPDY).."+END)
            crime_result = m_crime_run(targetIP,port)
            print(GREEN+"[INF] Scan CCS Injection.."+END)
            ccs_result = m_ccsinjection_run(targetIP,port)
            print(GREEN+"[INF] Scan HeartBleed.."+END)
            heartbleed_result = m_heartbleed_run(targetIP,port)
            print(GREEN+"[INF] Scan SSLv3 POODLE.."+END)
            poodle_result = m_poodle_run(targetIP,port)
            print(GREEN+"[INF] Scan OpenSSL FREAK.."+END)
            freak_result = m_freak_run(targetIP,port)
            print(GREEN+"[INF] Scan OpenSSL LOGJAM.."+END)
            logjam_result = m_logjam_run(targetIP,port)
            print(GREEN+"[INF] Scan SSLv2 DROWN.."+END)
            drown_result = m_drown_run(targetIP,port)
            print(GREEN+"[RES] Finish scan all vulnerability.."+END)

def outVersion():
    print "A2SV v"+a2sv_version

def updateVersion():
    print GREEN+"[INF] Update A2SV"+END
    print GREEN+"[INF] This A2SV version is .. v"+a2sv_version+END
    os.chdir(os.path.dirname( os.path.abspath( __file__ )))
    os.system("git reset --hard HEAD")
    os.system("git pull -v")
    vfp = open(myPath+"/version","r")  #Version File Pointer
    print RED+"[FIN] Updated A2SV"+END

def outReport(o_ck,o_path,tmode):
    global ccs_result
    global heartbleed_result
    global poodle_result
    global freak_result
    global logjam_result
    global drown_result
    global crime_result
    global anonymous_result
    if anonymous_result == "0x01":
        anonymous_result = "Vulnerable!"
    elif anonymous_result == "0x00":
        anonymous_result = "Not Vulnerable."
    elif anonymous_result == "0x02":
        anonymous_result = "Exception."        
    else:
        anonymous_result = "Not Scan."
    if crime_result == "0x01":
        crime_result = "Vulnerable!"
    elif crime_result == "0x00":
        crime_result = "Not Vulnerable."
    elif crime_result == "0x02":
        crime_result = "Exception."        
    else:
        crime_result = "Not Scan."
    if ccs_result == "0x01":
        ccs_result = "Vulnerable!"
    elif ccs_result == "0x00":
        ccs_result = "Not Vulnerable."
    elif ccs_result == "0x02":
        ccs_result = "Exception."        
    else:
        ccs_result = "Not Scan."
    if heartbleed_result == "0x01":
        heartbleed_result = "Vulnerable!"
    elif heartbleed_result == "0x00":
        heartbleed_result = "Not Vulnerable."
    elif heartbleed_result == "0x02":
        heartbleed_result = "Exception"
    else:
        heartbleed_result = "Not Scan."
    if poodle_result == "0x01":
        poodle_result = "Vulnerable!"
    elif poodle_result == "0x00":
        poodle_result = "Not Vulnerable."
    elif poodle_result == "0x02":
        poodle_result = "Exception"
    else:
        poodle_result = "Not Scan."
    if freak_result == "0x01":
        freak_result = "Vulnerable!"
    elif freak_result == "0x00":
        freak_result = "Not Vulnerable."
    elif freak_result == "0x02":
        freak_result = "Exception"
    else:
        freak_result = "Not Scan."
    if logjam_result == "0x01":
        logjam_result = "Vulnerable!"
    elif logjam_result == "0x00":
        logjam_result = "Not Vulnerable."
    elif logjam_result == "0x02":
        logjam_result = "Exception"
    else:
        logjam_result = "Not Scan."
    if drown_result == "0x01":
        drown_result = "Vulnerable!"
    elif drown_result == "0x00":
        drown_result = "Not Vulnerable."
    elif drown_result == "0x02":
        drown_result = "Exception"
    else:
        drown_result = "Not Scan."

#----------- Template -----------
#    if logjam_result == "0x01":
#        logjam_result = "Vulnerable!"
#    elif logjam_result == "0x00":
#        logjam_result = "Not Vulnerable."
#    else:
#        logjam_result = "Not Scan."
#----------- -------- -----------

    data = [
    {'v_vuln':'Anonymous Cipher', 'v_cve':'CVE-2007-1858', 'cvss':'AV:N/AC:H/Au:N/C:P/I:N/A:N', 'v_state':anonymous_result},
    {'v_vuln':'CRIME(SPDY)', 'v_cve':'CVE-2012-4929', 'cvss':'AV:N/AC:H/Au:N/C:P/I:N/A:N', 'v_state':crime_result},
    {'v_vuln':'HeartBleed', 'v_cve':'CVE-2014-0160', 'cvss':'AV:N/AC:L/Au:N/C:P/I:N/A:N', 'v_state':heartbleed_result},
    {'v_vuln':'CCS Injection', 'v_cve':'CVE-2014-0224', 'cvss':'AV:N/AC:M/Au:N/C:P/I:P/A:P', 'v_state':ccs_result},
    {'v_vuln':'SSLv3 POODLE', 'v_cve':'CVE-2014-3566', 'cvss':'AV:N/AC:M/Au:N/C:P/I:N/A:N', 'v_state':poodle_result},    
    {'v_vuln':'OpenSSL FREAK', 'v_cve':'CVE-2015-0204', 'cvss':'AV:N/AC:M/Au:N/C:N/I:P/A:N', 'v_state':freak_result},
    {'v_vuln':'OpenSSL LOGJAM', 'v_cve':'CVE-2015-4000', 'cvss':'AV:N/AC:M/Au:N/C:N/I:P/A:N', 'v_state':logjam_result},
    {'v_vuln':'SSLv2 DROWN', 'v_cve':'CVE-2016-0800', 'cvss':'AV:N/AC:M/Au:N/C:P/I:N/A:N', 'v_state':drown_result}
]
    fmt = [
    ('Vulnerability',       'v_vuln',   16),
    ('CVE',          'v_cve',       13),
    ('CVSS v2 Base Score',          'cvss',       26),
    ('State', 'v_state', 15)
]
    if o_ck == 1:
        print "The result is in \""+str(o_path)+"\"."
        if tmode == 1:
            of = open(str(o_path),'a')
            of.write(" [TARGET]: "+targetIP+"\r\n")
            of.write(" [PORT]: "+str(port)+"\r\n")
            of.write(" [SCAN TIME]: "+str(datetime.datetime.now())+"\r\n")
            of.write(" [VULNERABILITY]"+"\r\n")
            of.write(TablePrinter(fmt, ul='=')(data))
            of.write("\r\n")
        else:
            of = open(str(o_path),'w')
            of.write(" [TARGET]: "+targetIP+"\r\n")
            of.write(" [PORT]: "+str(port)+"\r\n")
            of.write(" [SCAN TIME]: "+str(datetime.datetime.now())+"\r\n")
            of.write(" [VULNERABILITY]"+"\r\n")
            of.write(TablePrinter(fmt, ul='=')(data))
            of.write("\r\n")
    else:
        print BLUE+" [TARGET]: "+targetIP+END
        print BLUE+" [PORT]: "+str(port)+END
        print BLUE+" [SCAN TIME]: "+str(datetime.datetime.now())+END
        print RED+" [VULNERABILITY]"+END
        print( TablePrinter(fmt, ul='=')(data) )

###MAIN##
def a2svmain(website):

    parser = argparse.ArgumentParser("a2sv",formatter_class=argparse.RawTextHelpFormatter)
    #parser.add_argument("-t","--target", help="Target URL and IP Address\n > e.g -t 127.0.0.1")
    parser.add_argument("-tf","--targetfile", help="Target file(list) URL and IP Address\n > e.g -tf ./target.list")
    parser.add_argument("-p","--port", help="Custom Port / Default: 443\n > e.g -p 8080")
    parser.add_argument("-m","--module", help="Check SSL Vuln with one module\n[anonymous]: Anonymous Cipher\n[crime]: Crime(SPDY)\n[heart]: HeartBleed\n[ccs]: CCS Injection\n[poodle]: SSLv3 POODLE\n[freak]: OpenSSL FREAK\n[logjam]: OpenSSL LOGJAM\n[drown]: SSLv2 DROWN")
    parser.add_argument("-d","--display", help="Display output\n[Y,y] Show output\n[N,n] Hide output")
    parser.add_argument("-o","--out", help="Result write to file\n > e.g -o /home/yourdir/result.txt")
    parser.add_argument("-u","--update", help="Update A2SV (GIT)",action='store_true')
    parser.add_argument("-v","--version", help="Show Version",action='store_true')
    args = parser.parse_args()

    #target = raw_input("Enter URL \n")
    target=WWW(website)
    port =raw_input("Would you like to enter custom port? Defualt 443")
    #port =int(port)
    # if args.version:
    #     outVersion()
    #     exit()
    # if args.update:
    #     updateVersion()
    #     exit()
    # 

    if target != '':
        #target = args.target
        print (target)
        #print(BLUE+"[SET] target => "+args.target+END)
        print(BLUE+"[SET] target => "+target+END) 
        targetIP = socket.gethostbyname(target)
        #print(BLUE+"[SET] IP Address => "+targetIP+END)
        print(BLUE+"[SET] IP Address => "+targetIP+END)
    elif args.targetfile:
        f = open(args.targetfile,"r")
        print(BLUE+"[SET] target => "+args.targetfile+END)
        print(BLUE+"[SET] IP Address list"+END)
        line = f.readline()
        while line:
            targetfileList.append(socket.gethostbyname(line.rstrip('\n')))
            print(BLUE+"       => "+str(targetfileList[-1:])+END)
            line = f.readline()        
        #global displayMode
        #global targetMode
        targetMode = 1
        displayMode = 1
        print "Running a2sv sillent mode[file list default]"
        f.close()
    else:
        mainScreen()
        print("Please Input Target Argument / -h --help")
        exit()
    if port:
        port = int(port)
        print(BLUE+"[SET] target port => "+port+END)
    else:
        port = 443
        print(BLUE+"[SET] target port => 443"+END)
    if args.module:
        checkVun = args.module
        ModuleName = args.module
        if ModuleName == "ccs":
            ModuleName = "CCS Injection"
        elif ModuleName == "heart":
            ModuleName = "HeartBleed"
        elif ModuleName == "poodle":
            ModuleName = "SSLv3 POODLE Attack"
        elif ModuleName == "freak":
            ModuleName = "OpenSSL FREAK Attack"
        elif ModuleName == "logjam":
            ModuleName = "OpenSSL LOGJAM Attack"
        elif ModuleName == "drown":
            ModuleName = "SSLv2 DROWN Attack"
        elif ModuleName == "crime":
            ModuleName = "CRIME(SPDY)"
        elif ModuleName == "anonymous":
            ModuleName = "Anonymous Cipher Suite"
        print(BLUE+"[SET] include => "+ModuleName+" Module"+END)
    else:
        checkVun = "all"
        print(BLUE+"[SET] include => All Module"+END)

    if args.out:
        output_path = args.out
        output_ck = 1
    else:
        output_ck = 0
        
    if displayMode == 0:
        mainScreen()
    if targetMode == 1:
        i=0
        imax = len(targetfileList)
        print "_________________________________________________________________________"
        print "                              [REPORT]                                   "
        while(i<imax):
            targetIP = targetfileList.pop()
            runScan(checkVun)
            outReport(output_ck,output_path,targetMode)
            i+=1
        print "_________________________________________________________________________"
    else:
        runScan(checkVun)
        print "_________________________________________________________________________"
        print "                              [REPORT]                                   "
        outReport(output_ck,output_path,targetMode)
        print "_________________________________________________________________________"
    print(RED+"[FIN] Scan Finish!"+END)
