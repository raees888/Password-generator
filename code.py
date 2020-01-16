import random
import time
list1=[chr(i) for i in range(48,91)]
list1.extend([chr(i) for i in range(97,123)])
uppercasealphabets=[chr(i) for i in range(65,91)]
print('Hello and welcome to this code where I generate a safe and secure password for you and that to for free')
name=input('Please tell us your name:\n')
if name is int:
    print("hmmm... that's a pretty strange name ;);)")
else:
    print(f'Okay so {name} please tell us the length of the password that you want\n')
while True:
    try:
        length=int(input())
        if length<6:
            raise ValueError
    except:
        print('The minimum allowable lenght is 6')
    else:
        break
string=random.sample(list1,length-1)
startingvalue=random.sample(uppercasealphabets,1)
string.extend(startingvalue)
count=random.randint(1,3)
while count!=0:
    print('preparing your password...')
    count-=1
    time.sleep(0.8)
print(''.join(string[::-1]))
#i am doing this for the first time.
