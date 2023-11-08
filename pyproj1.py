instruct = "" #an empty string
started = False# this variable shows the car has not started, just to show the state of a motionless car
while True:
    instruct  = input ('> ').lower()# to make it case insensitive
    if instruct == "help" :
        print("""
Start - to start car.
Stop - to stop car.
Quit - to exit.    """)
    elif instruct == "start" : 
        if started :#if the start option has already been entered or the car has started
            print('Car has already started')
        else :
            started = True#if the start option is now being entered
            print ('Car started... ready to go')
    elif instruct == "stop" :
        if not started:#this means the car was already not in motion
            print(' Car has already stopped')
        else :
            started = False#the car has now stopped
            print('Car stopped')

    elif instruct == "quit" :
        break
    else :
        print( ' I do not understand')





#for loop
item_prices= [10,20,30,50,900]
total = 0
for price in item_prices :
    total += price
print(f'Total price of items is ${total:,}')
new_total = pow(total, 3)#trying how to square numbers with this function
print(f'The total prices have have tripled and now you owe ${new_total:,}')

#notes and practice for libraries

#import random
#flipping a coin
#coin = random.choice(['heads','tails'])
#print(coin)
#returning a random integer with the two boundaries inclusive
#number = random.randint(1,10)
#print(number)
#shuffling a list of items
#cards = ['Jack','Queen','King','Spade','Hearts','Club']
#random.shuffle(cards)
#for card in cards:
#    print(card)

# Define the classes and methods



    
    
    
   







