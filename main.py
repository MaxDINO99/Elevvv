'''name = ("Maxim")
id = 'MD93049'
balance1 = 250
balance2 = 34.7
boolean = False #True
print(bool(0))
#variable
print("Ur id is " + id)


score = int(input('Enter ur score'))
if score == 100:
    print('U win')
else:
    print('U need more points')
'''
import random

lives = 3
win_var = random.randint(0 , 25)

while lives != 0:
    check = int(input('Enter ur number '))
    if check == win_var:
        print("U win")
        break
    elif check > win_var:
        print("Ur number is more than need")
    elif check < win_var:
        print("Ur number is less than need")

    lives = lives - 1
else:
    print("You louse")
