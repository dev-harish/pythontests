
class Parent:        # define parent class
   parentAttr = 0
   def __init__(self,val):
      print(super())
      print(self)
      print ("Calling parent constructor")
      Parent.parentAttr =val

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print(super)
      #Parent.__init__(self,10)
      super().__init__(10)
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')


c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method