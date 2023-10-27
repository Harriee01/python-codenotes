 #empty objects
class EmpObject :
   pass
obj = EmpObject()
obj.x = 'Hello'
print(obj.x)

#references to the object that do not directly contain the object's data
class Myclass(object) :
    pass
this_obj = Myclass()
print(this_obj)
that_obj = Myclass()
print(that_obj)