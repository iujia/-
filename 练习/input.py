prompt = "\nTell me something , and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."


active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
print("---------------------------------------------------")


prompt = "\nTell me something , and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")
