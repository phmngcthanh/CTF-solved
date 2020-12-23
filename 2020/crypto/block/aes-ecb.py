import json
import requests 
import time

flag=''
padding='1'
def req(par):
    PARAMS=par
    HOST = 'http://aes.cryptohack.org/ecb_oracle/encrypt/'
    R=HOST+PARAMS+'/'
    r = requests.get(url = R) 
    data=r.json()
    return data['ciphertext']


def Get_len_flag():
    PARAMS='a'*(2)
    data = req(PARAMS) 
    len_flag=len(data)//2
    for i in range(2,17):
        PARAMS='a'*(i*2)
        data = req(PARAMS)
        if (len(data)//2) > len_flag:
            #print(len_flag)
            #print(len(data)//2)
            #nghia la len_flag ton (i-1) cho padding
            len_flag=len_flag-(i)
            print('len_flag:',len_flag)
            break
    return len_flag

def BLOCK_PADDING(len_flag):
    i=(len_flag//16)+2
    return i


len_flag=Get_len_flag()
num_pad=BLOCK_PADDING(len_flag)
printable_mod='{_etaoinshrdlcumwfgypbvkjxqzETAOINSHRDLCUMWFGYPBVKJXQZ0123456789!#$%&()*+-?@}~'
a=time.time()
for i in range(len(flag),len_flag+1):
    for j in printable_mod:
        #j='c'
        payload=flag[-15:]+j
        payload=(payload.encode('ansi')).hex()
        while (len(payload)<32):
            payload=padding+payload
        payload=payload+padding*((num_pad*32)-(i*2)-2)
        print(payload)
        data = req(payload)
        print(data)
        if (data[0:32]==data[num_pad*32:(num_pad+1)*32]):
            flag+=j
            print('-----------------------------------------------------------')
            print(flag)

print('took',time.time()-a)
print(flag)