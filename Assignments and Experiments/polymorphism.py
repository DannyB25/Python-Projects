#creating parent class
class car_entry:
    name = "Molly" #naming objects and providing values 
    door = "back"
    passcode = "3456"
    help_num = "4032349856"

    def wayIn(self): #creating a function using the self object
        entry_name = input("What is your name?: ")
        entry_door = input("What door are you using?: ") #creating objects/values
        entry_passcode = input("Enter the passcode: ")
        
        if (entry_door == self.door and entry_passcode == self.passcode): #if loop with set parameters 
            print("Welcome in, {}! Have a great day!".format(entry_name)) #message if the if loop is true 
        else: #else statement 
            print("Please try again...") #what to print if the if loop is false

class car_one(car_entry): #creating child class
    door = "bay" #creating objects and providing values
    lic_plate = "12345678910"
    pin = "5050"
    make = "Dodge"
    model = "Dakota"

    def wayIn(self): #creating a function using the self object
        entry_name = input("What is your name?: ")
        entry_door = input("What door are you using?: ") #creating objects/values
        entry_pin = input("Enter the pin: ")#this is where polymorphism comes in. Using this instead of the passcode
          
        if (entry_door == self.door and entry_pin == self.pin): #if loop with set parameters 
            print("Welcome in, {}! Have a great day!".format(entry_name)) #message if the if loop is true 
        else: #else statement 
            print("Please try again...") #what to print if the if loop is false

class car_two(car_entry): #creating child class
    door = "front" #creating objects and providing values
    lic_plate = "5544332211"
    card = "001100"
    make = "Chevrolet"
    model = "Nova"

    def wayIn(self): #creating a function using the self object
        entry_name = input("What is your name?: ")
        entry_door = input("What door are you using?: ") #creating objects/values
        entry_card = input("Enter the card number: ")#this is where polymorphism comes in. Using this instead of the passcode
          
        if (entry_door == self.door and entry_card == self.card): #if loop with set parameters 
            print("Welcome in, {}! Have a great day!".format(entry_name)) #message if the if loop is true 
        else: #else statement 
            print("Please try again...") #what to print if the if loop is false

ingress = car_entry()
ingress.wayIn()

requester = car_one()
requester.wayIn()

also = car_two()
also.wayIn()

    
    

                  
    
