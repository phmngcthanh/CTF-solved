import time
a=time.time()  
import itertools
old_sigma = "0123456789abcdef"
new_sigma = list(old_sigma)

list(itertools.permutations(new_sigma))

print("it takes",time.time()-a)