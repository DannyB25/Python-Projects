try: #lets you test a block of code for errors
    print(bob)
except: #lets you handle the error without crashing 
    print("an exception occurred")
    

message = "Good Job"

try:
    print(message)
except:
    print("an error has occurred")
else: #lets you execute code when there is not error 
    print("No errors!")

try:
    print(w)
except:
    print("something is awry")
finally: #lets you execute code, regardless of the result of the try and except blocks 
    print("the try and except blocks have been completed")
