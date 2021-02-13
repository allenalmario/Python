class Ninja:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def displayStats(self):
        print("Name:" + self.name)
        print("Health:" + str(self.health))
        return self

    def eatStrawberry(self):
        self.health += 10
        
# Predict the Output (if there are any errors,
# try to predict what it will say, and then fix it.)
hikusake = Ninja("Hikusake", 60) # makes instance
print(hikusake.name) # Output: Hikusake
kikomo = Ninja("Kikomo") # makes instance
kikomo.displayStats()
# Name: Kikomo
# Health: 100
kikomo.eatStrawberry() 
kikomo.displayStats()
# Name: Kikomo
# Health: 110