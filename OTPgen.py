import random
import keyboard

while True:
    length = input('How long would you like your password to be? ')
    if length.isdigit():
        length = int(length)
    else:
        print('Please enter a number.')
        continue
    y = []
    while length > 0:
        x = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"','<','>',',','.','/','?','~'])
        y.append(x)
        length -= 1
        if length == 0:
            print(*y, sep = '')
            keyboard.wait('`')