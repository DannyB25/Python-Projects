
#parent class
class Organism: #creating class organism 
    name = "Unknown" #providing value to variables from here down 
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self): #creating function with self object 
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based) #Creates a message using format method and variables introduced 
        return msg #produce the message created from the format/value insert above 

#child class instance
class Human(Organism): #creating child class human. Parent class is organism
    name = "MacGuyver"  #providing value to variable (this variable did not have a value in the parent class) 
    species = "Homosapien" #providing value to variable (this variable did not have a value in the parent class) 
    legs = 2 #providing value to variable (this variable did not have a value in the parent class) 
    arms = 2 #providing value to variable (this variable did not have a value in the parent class) 
    origin = "Earth" #providing value to variable (this variable did not have a value in the parent class) 

    def ingenuity(self): #creating a function w/ self object
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

#another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

#another child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg 



if __name__ == "__main__":
    human = Human() #creating instance of Human class through variable human
    print(human.information()) #calling the inherited information method from the parent class 
    print(human.ingenuity()) #printing the ingenuity method for human class 

    dog = Dog() #creating instance of dog class called variable dog 
    print(dog.information()) #calling the inherited information method from the parent class 
    print(dog.bite()) #calling the bite method from class dog 

    bacteria = Bacterium()
    print(bacteria.information())#calling the inherited information method from the parent class
    print(bacteria.replication())#calling the replication method from class bacteria 
