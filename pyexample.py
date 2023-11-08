students = ['Ato','Baffuoh','Vince']
for i in range(len(students)) :#the len returns the number of characters in the list and range can then be used since the range takes only numbers 
    print(i+1, students[i])#the i+1 gives the rank 1 to the first student with index 0 since len returns 0,1,2. student[i] allows the for loop iterate over the students because i was used




# dictionaries,ie,dict
pupils = {
    'Sandra':'Maria', 
    'Nessa':'Conti',
    'Agnes' : 'Amissah'
    }    
for pupil in pupils :
    print(pupil, pupils[pupil],sep= ': ')# prints the name of pupil, accesses the house relating to it in the dictionary, separates with a colon



# list of dictionaries
names = [
{'Name':'Sarah', 'House':'Red', "Food":'Bread'},
{'Name':'Bob', 'House': 'Blue', 'Food':'Yam'},
{'Name':"Hellen",'House':'Yellow', 'Food':'Pie'},
{'Name':'Max','House':'Orange','Food':None}#introducing a keyword called none
]
for name in names:
    print(name["Name"], name['House'], name['Food'], sep=': ')

customer = {
     'name':'Harry',
     'age' : '18',
     'is_verified':True

}
for details in customer :
    print(details, customer[details], sep = ' : ')


#ask for phone number in digits and translate to words
try :# for exceptions in my code
    phone =input('Phone number: ')
    translation = {
      '1' : 'One',
      '2' : 'Two',
      '3' : 'Three',
      '4' : 'Four',
      '5' : 'Five',
      '6' : 'Six',
      '7' : 'Seven',
      '8' : 'Eight',
     '9'  : 'Nine',
      '0' : 'Zero'
     }

    for digit in phone :
        print(translation[digit], end= ' ')#the input digit will print out its pair in the transaltion dict,end='' to ensure they're on the same line
except KeyError:#in case a user input something wrong
    print('!')







#trying the def function which helps me to create my own functions 
def hello(to) :
    print('Hello,',to)
name =input ('What is your name? ')
hello(name)







#trying the def main function
def main () :#this would be my main function to be run
   name = input("What's your name? ")
   hello(name)

def hello(to) :
   print('Hello,',to)

main()



#trying a pythonic expression
def main() :
    number = int(input("What's your number? "))
    if is_even(number) :
        print('Even')
    else :
        print('Odd')

def is_even(n) :
   # return True if n % 2 == 0 else False
   return n % 2 == 0 #more pyhtonic, this is a boolean expression which will give a yes or no answer

main()


#nested loops, printing a block of square
def main():
    print_square(3)

def print_square(size) :#to print the square
    for i in range(size): # to print a row in the square, i reps each of the rows
       # for j in range(size):#to print a block in the row,inside i, j prints the brick
        #    print('#', end=' ')#print the block or brick
        print( )#an automatic line ending like \n
        print('#'* size)#an alternative to creating the brick


main()


#nested loops, creating an f shape
numbers = [8,3,8,3,3]
for i in numbers :
    for j in range(i) :#this takes the number of the first item in numbers
        print ('x', end = '')# all will be on the same line
    print( )#new line

#creating sets
topics = {"Mathematics","Science","Sports","Louis","Social Studies"}
school ={"Holy child","Presec","Wesley Girls","Prempeh","Louis"}
group = topics.union(school)
print(group)
safe = topics.intersection(school)
print(safe)
guess = topics.difference(school)
trial = topics.difference(group)
print(guess,trial, sep = " : ")