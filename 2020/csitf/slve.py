import random

key_ = 'insovietrussiapikachucatchesyou'
cipher = '»·­ª»£µ±¬¥¼±ºµ±¿·£¦­´¯ª¨¥«¥¦«´¸¦¡¸¢²§¤¦¦¹¨'

def dec1(text):
    r = random.randint(1,25)
    return bytes.fromhex(''.join([hex(((ord(i) - ord('a') - r) % 26) + ord('a'))[2:] for i in text])).decode('ascii')

def dec3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

def dec2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord('a') + ord(k[i])) for i in range(len(text))])

for i in range(25):
  print(dec1(dec2(dec3(dec3(cipher)), key_)))

csictf{esreverisjustreverseinreverseright}
#ord(text[i]) ^ ord(k[i]) + ord('a') == enc-flag
#enc3(enc3(enc2(enc1(encryptedText), key))) == enc_flag
# enc1(enc2(enc3(enc3(enc_flag)), key)) == flag