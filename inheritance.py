#the purpose of this code is to demonstrate inheritance, as well as, to display
#how to add additional attributes to a child class 

class passenger: #creating class 'passenger' which is the parent class
    name = " " #variable w/ empty value to be filled later 
    airline = "Delta" #variable w/ empty value to be filled later
    destination = "Bermuda" #variable w/ empty value to be filled later
    eta = 1:00  #variable with value for time of arrival  

class customer(passenger): #creating class 'customer', which is a child of the parent class 'passenger'
    seat_num = " " #variable with empty value 
    ticket_price = 200.00 #variable with default value for ticket price 

class attendant(passenger): #creating class 'attendant' which is a child of the parent class 'passenger'
    hourly_wage = 45.00 #variable with provided value 
    tenure = " " #tenure variable without value provided 
    
    
    
