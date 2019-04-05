import random
secret = random.randint(1,10)
temp = input('input = ')
guess = int(temp)
i = 1
while i != 3 and guess != secret:
    i +=1
    if guess>secret:
        print('big')
    elif guess <secret:
        print('small')
    temp = input('input = ')
    guess = int(temp)
if guess == secret:
    print('right')
else:
    print('false')