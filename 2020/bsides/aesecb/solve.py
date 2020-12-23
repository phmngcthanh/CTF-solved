import socket 
from string import *
import base64
host='chall.bsidesalgiers.com'
port= 5002
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.recv(4096)

#sometime it will fail at some stage, just type the known flag and it will get the rest of it
flag=''
padding='0'
payload_padding='0'
BLCK_SZ=16
sent=''

len_flag=67
#adjusted from string.printable , for quicker
printable_mod='{_etaoinshrdlcumwfgypbvkjxqzETAOINSHRDLCUMWFGYPBVKJXQZ0123456789!#$%&()*+-?@}~'
for j in range(len(flag),len_flag):
    for i in printable_mod:
        print("----++++-----")
        sent=flag[-15:]+i
        while (len(sent)<16):
            sent=payload_padding+sent
        sent+=(padding*((16*6)-j-1))
        sent=sent+'\n'
        print('a-')
        print(sent)
        s.sendall(sent.encode())
        a=s.recv(2048)
        print('b-')
        print(a)
        if(len(a) <20):
            print('c-')
            a=s.recv(1024)
            print(a)
        if (a[0:3]==b'The'):
            a=a[13:]
        if (a.decode().find('=>')):
            a=a[:-4]
        print('d-')    
        print(a)
        a=base64.b64decode(a).hex()
        print('e-')
        print(a)        
        if (a[0:32]==a[192:224]):
            print("-------------------------FLAG-------------------------------------")
            print('FLAG:',end="")
            flag+=i
            print(flag)
            break 



  
print(flag)                     