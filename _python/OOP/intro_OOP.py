# Python Day 2 – OOP        
#     1.What does OOP stand for? What is it, briefly?
#     Object Oriented Programming, style of programming uses a blueprint for modeling data
#     Blueprint defined by the programmer -- DIY datatypes
#        -- customize it for your situation
#     Modularizing 

#     2.What is a class?
#    User/programmer defined defined data-type 
#    Like a function is like a recipe --- class is a blueprint for the data type

#     3.Classes contain 2 things: attributes and methods. Give a brief explanation for each:
#     Attributes: Characterisitcs -- variables that belong to the class, What a class of objects has --> datatypes
            # ex: car
                # --model -- string(corolla)
                # --make --string (toyota)
#     Methods: functions that often affect the properties of the class
        # functions that belong to the class -- 
        # what a clas of objects can DO --> actions/functions
#     4.The following are lines of code could belong to a Shopping Cart class, but are out of order but . On the right, arrange the code to make a functional class.Once you re-order the code on the right, put a * next to any attributes, and a box around any 
#     methods.

class ShoppingCart:
    def __init__(self, store):
        def add_item(self, item, price):
            self.items = []
            self.items.append(item)
            self.total = 0
            self.total += price
            self.store = store
            return self