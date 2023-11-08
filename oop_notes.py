
class myclass(object):#explaining the __init__ constructor
  def __init__(self,aaa, bbb):#aaa and bbb are the arguments and the object has been initialized
      self.a = aaa
      self.b = bbb
x = myclass(4.5, 3)
print(x.a, x.b, sep= "\n")#accessing the method in the class with the '.'



#explaining how class attributes and instance attributes work
class InstanceCounter(object):
  count = 0 # class attribute, will be accessible to all 
               #instances
  def __init__(self, val):#val is the instance attribute
     self.val = val
     InstanceCounter.count +=1 # Increment the value of class attribute, 
                               #accessible through class name.Each time a new object of the class is created, 1 is added to the value
# In above line, class ('InstanceCounter') act as an object
  def set_val(self, newval):#allows one change the value of val in the previous instance(object)
      self.val = newval

  def get_val(self):#returns the value of the 'newval' or val in the previous instance
     return self.val
  
  def get_count(self):#returns the value of the class attribute 'count' per the number of instances created
    return InstanceCounter.count
  
# the lines below are the instances of the class created
a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)
d = InstanceCounter(576)
for obj in (a, b, c):#iterates through each instance
 print ('val of obj: %s' %(obj.get_val())) # Initialized value ( 9, 18, 27 )# just added the 4th instance
                                                         #%(obj.get_val()) is the value that will replace the string placeholder,%s
 print ('count: %s' %(obj.get_count())) # always 3; it'll now be 4 because there are 4 instances or objects of the class created



#File I/O
#using open and write
name = input("What's your name?\n: ")
file = open("name.txt", "w") #write creates a new file always whenever the code is executed
file.write(name)
file.close()

#using open with append
name = input("What's your name?\n: ")
file = open("name.txt", "a") # adds information to the file
file.write(f"{name}\n") 
file.close()

#using with function
name = input("What's your name?\n: ")
with open('names.txt', "a") as file :# the with function automatically opens and closes a file
    file.write(f"{name}\n")



#to read a file
with open("names.txt","r") as file :
    lines = file.readlines()#reads the lines the the file
for line in lines :
    print("Hello,",line.rstrip())
# more pythonic
with open("names.txt","r") as file :#iterates over each line in the file
    for line in file :
      print("Hello,",line.rstrip())



#to sort
names = []
with open("names.txt") as file :#default read
    for line in file :
        names.append(line.rstrip())#fills the empty list with the names in the file line by line
for name in sorted(names) :
    print(f"Hello, {name}")



#csv(comma separated values)
with open("name.csv") as file :
    for line in file :
        row = line.rstrip().split(",")
        print(f"{row[0]} in{row[1]}")



#unpacking 
with open("name.csv") as file :
   for line in file :
      name,house = line.rstrip().split(",")
      print(f"{name} in{house}")


#to sort items in a csv
students = []
with open("name.csv") as file :
    for line in file :
        name,house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
  print(student)   