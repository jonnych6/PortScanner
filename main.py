from socket import *

# Take host and port and scan
def conScan(tgtHost, tgtPort):
    try: 
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print(f'[+]{tgtPort}/tcp open')
        connskt.close()
    except:
        print(f'[-]{tgtPort}/tcp closed')

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f'[-]Cannot resolve {tgtHost}')
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'\n[+] Scan result of: {tgtName[0]}')
    except:
        print(f'\n[+] Scan result of: {tgtIP}')
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: ' + str(tgtPort))
        conScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    portScan('google.com', [80, 22])