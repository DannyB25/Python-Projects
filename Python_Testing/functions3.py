fName= "Daniel" #provide value to variables
lName= "Brion"
print(fName + lName) 
print(fName + " " + lName) #adding a space in between two variables
print("Hello {}  {}, welcome to Python!".format(fName, lName)) #using format to add to variables into placeholder values

text = "You can come {insert:} anytime!" # using variable insert as value in sentence
print(text.format(insert= "by")) #using format function to fill in place holder above with "by"

hexa = format(113, 'x')
print(hexa)

def getSum(num1, num2):
    answer= num1 + num2
    print("The answer is {}.".format(answer))

getSum(2,4)

myAdd = getSum

myAdd(2, 5)

