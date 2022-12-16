import random

random_number = random.randint(1, 20)

name = 'name' #input('Hello, what is your name? ')
print('Hello ' + name + ', this is a game of guess the number. I will think a number, and you od your best to find it out.')
print(random_number)
print(type(random_number))
for i in range(5,-1,-1):
    
    number = input('Choose a number: ')
    if number.isnumeric() == False:
        print('You must choose a number to play. You have', int(i), 'moves left.')
        print()
        continue

    if int(number) < int(random_number):
        if i == 1:
            print('The number', number, 'is not correct, mine is higher! You have', int(i), 'move left.')
        else:
            print('The number', number, 'is not correct, mine is higher! You have', int(i), 'moves left.')
    elif int(number) > int(random_number):
        if i == 1:
            print('The number', number, 'is not correct, mine is lower! You have', int(i), 'move left.')
        else:
            print('The number', number, 'is not correct, mine is lower! You have', int(i), 'moves left.')
    else:
        print('That is correct!')
        break
    if i == 0:
        print('Sorry looser!')
    print()
    
    
    