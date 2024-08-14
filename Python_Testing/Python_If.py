

num1 = 12
key = False

if num1 == 12: #make a comparison with if statement using ==
    if key: #this states if the statement above is true. to say not true you would say "if not key"
        print('Num1 is equal to Twelve and they have the key!') #action to take if the if statement is true
    else: #additional else statement. states if num 1 is not 12 fire off below print command
        print('Num1 is equal to Twelve and they Do Not have the key!') 
elif num1 < 12: #additional clause/condition
    print('Num1 is less than Twelve!')#action to take if num1 is less than 12
else:
    print('Num1 is NOT equal to Twelve!') #action to take if the if or elif statements are false

ber = 55
nu = 40

if ber > nu:
    print("the ber is greater than nu!")

nu = 60

if ber > nu:
    print("the ber is greater than nu!")
elif nu > ber:
    print("the nu is greater than ber!")


nu = 55

if ber > nu:
    print("the ber is greater than nu!")
elif nu > ber:
    print("the nu is greater than ber!")
else:
    print("the nu and the ber are equal!")

ber = 99


if ber > nu:
    print("the ber is greater than nu!")
    if ber < 100:
        print("ber is less than 100")
elif nu > ber:
    print("the nu is greater than ber!")
else:
    print("the nu and the ber are equal!")

john = 30
bill = 30

if john == bill:
    print("john and bill are the same age!")

def aFunction():
    return False
print(aFunction())

print(bool("a"))
print(bool("abc"))
print(bool(False))

me = "dan"

print(isinstance(me, str))
      

          
