from pwn import *
 #34.87.30.195 7331
r = remote('34.87.30.195', 7331)
#blockngag
r.send("1 1 1 3")
r.send("\n")
print (r.recv())
r.send("2 1 2 3")
r.send("\n")
print (r.recv())
r.send("3 1 3 3")
r.send("\n")
print  (r.recv())
#block doc

r.send("1 1 3 1")
r.send("\n")
print (r.recv())
r.send("1 2 3 2")
r.send("\n")
print (r.recv())
r.send("1 3 3 3")
r.send("\n")
print (r.recv())
#send..
r.send("1 1 3 1")
r.send("\n")
print (r.recv())

r.send("1 2 3 2")
r.send("\n")
print (r.recv())
r.send("1 3 3 3")
r.send("\n")
print (r.recv())

