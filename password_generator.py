import random
import string

seq=string.printable
a=int(input("How long do you want your password to be? "))
passw=''

for i in range(0,a):
    passw=passw+random.choice(seq)
print(passw)    
