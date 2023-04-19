unconfirmed_users = ['chenjiajia','chensiming','shfujkf']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user)
    confirmed_users.append(current_user)

print("\nThe follow users have been confirmed: ")
for  confirmed_user in confirmed_users:
    print(confirmed_user)


print("------------------------------------------------------------------------")
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
print("------------------------------------------------------------------------")


responses = {}

polling_active = True

while polling_active:
    name  =input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input(" Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n---Poll Result---")
for name,reponse in responses.items():
    print(name+"would you like to climb "+response+".")
