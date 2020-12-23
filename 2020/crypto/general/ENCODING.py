from socket import *
import base64
import codecs
import random
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes

ENCODINGS = [
	"base64",
	"hex",
	"rot13",
	"bigint",
	"utf-8",
]
HOST = 'socket.cryptohack.org' 
PORT = 13377  

def JsonToStr(a):
	return json.loads(a)

def StrToJson(a):
	return json.dumps(a)

def Decodec(a): #grab a byte object and decode
	js=JsonToStr(a)
	if js['type'] == "base64":
		decoded = codecs.decode(js['encoded'].encode(), 'base64').decode()
	elif js['type'] == "hex":
		decoded = codecs.decode(js['encoded'], 'hex').decode()
	elif js['type'] == "rot13":
		decoded = codecs.decode(js['encoded'], 'rot_13')
	elif js['type'] == "bigint":
		decoded = long_to_bytes(int(js['encoded'],16)).decode()
	elif js['type'] == "utf-8":
		decoded = [chr(b) for b in js['encoded']]
		decoded = ''.join(map(str, decoded)) 
	return {"decoded": decoded}


with socket(AF_INET, SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	for i in range (102):
		data = s.recv(1024)
		print(data)
		print(Decodec(data))
		s.sendall((StrToJson(Decodec(data))).encode())
