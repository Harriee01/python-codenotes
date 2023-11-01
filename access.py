#getter and setter methods for accessing encapsulated data
class MyClass(object):
    def setAge(self, num):#setter method, which allows controlled modification when accessed
       self.age = num


    def getAge(self):#getter method which is read only
      return self.age
    

Mavis = MyClass()

Mavis.setAge(45)#the number is set

print(Mavis.getAge())#displays the set age

Mavis.setAge("Forty Five")#num receives any value

print(Mavis.getAge())




#more explanation on getter and setter methods
class MClass:
    def __init__(self):
        self._my_data = 0  # Encapsulated data

    def get_data(self):
        return self._my_data  # Getter method
    
    def set_data(self, value):
        if value >= 0:
            self._my_data = value  # Setter method


#implementation or method call

goal = MyClass()
goal.set_data(78)
print(goal.get_data())