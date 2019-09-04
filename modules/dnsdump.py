from insides.DNSDumpsterAPI import DNSDumpsterAPI
from insides.functions import removeHTTP
global str
def dnsdump(website):
    website = removeHTTP(website)
    print(website)
    #str w=str(website)
    res = DNSDumpsterAPI(False).search(website)
    if not res:
        print ('\n DNS Records')
        return

    print ('\n DNS Records')

    for entry in res.get('dns_records', {}).get('dns', []):
        print ('{domain} ({ip}) {as} {provider} {country}'.format(**entry))

    for entry in res.get('dns_records', {}).get('mx', []):
        print ('\n MX Records')
        print ('{domain} ({ip}) {as} {provider} {country}'.format(**entry))
    print ('\n\033[1;32m[+]\033[1;m Host Records (A)')

    for entry in res.get('dns_records', {}).get('host', []):
        if entry.get('reverse_dns', None):
            print ('{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}'.format(**entry))
        else:
            print ('{domain} ({ip}) {as} {provider} {country}'.format(**entry))
    print ('\n TXT Records')

    for entry in res.get('dns_records', {}).get('txt', []):
        print (entry)
    print ('\n DNS Map: https://dnsdumpster.com/static/map/'+website+'.png\n')
