#define parent class
class primate: #creating class primate 
    c_lass = "mammal" #giving the objects values 
    subspecies = " "
    arms = 2
    legs = 2
    habitat = " "
    diet = " "

    def details(self): #creating a function
        msg = "\nclass: {}\nsubspecies: {}\narms: {}\nlegs: {}\nhabitat: {}\ndiet: {}".format(self.c_lass,self.subspecies,self.arms,self.legs,self.habitat,self.diet)
        return msg
        #return value for msg when called 

class gorilla(primate): #creating a child class w/ primate as parent
    subspecies = "Gorilla" #adding values to objects
    habitat = "Africa"
    diet = "foliage"

    def about(self): #creating function w/ self object
        msg = "\nGorillas are herbivorous, predominantly ground-dwelling great \
apes that inhabit the tropical forests of equatorial Africa. The genus Gorilla \
is divided into two species: the eastern gorilla and the western gorilla, and \
either four or five subspecies."
        return msg
        
    
if __name__ == "__main__": #if module is running, perform commands below
    gorillas = gorilla()
    print(gorillas.details())
    print(gorillas.about())
    
    
    
    
