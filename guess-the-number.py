import random

random_number = random.randint(1, 20)

name = 'name' #input('Hello, what is your name? ')
print('Hello ' + name + ', this is a game of guess the number. I will think a number, and you od your best to find it out.')
print(random_number)

for i in range(5):
    print('fse')
    number = input('Choose a number: ')
    if int(number) < int(random_number):
        print('The number', number, 'is not correct, mine is higher!')
    elif int(number) > int(random_number):
        print('The number', number, 'is not correct, mine is lower!')
    else:
        print('that is correct!')
        break
    
    i+=1