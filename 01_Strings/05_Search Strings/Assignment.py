text = input("Enter some text:") #use input to actually store into text. remove ""

result = text.find("the")

if result == -1:
    print("The word the is not in the string")
else:
    print("The word the is in the string")
    print ("It is located at", result)
    
