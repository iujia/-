
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
    }
print("You ordered a"+pizza['crust']+
      "-crust pizza"+"with the fllowing toppings")

for topping in pizza['toppings']:
    print("\t"+topping)




favorite_languages = {
    'jen':['python','ruby'],
    'sarach':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']}

for name , languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
print("-----------------------------------------------------")

users = {
    'aeinsteib':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username, user_info in users.items():
    print("\nusername :"+username)
    full_name = user_info['first']+user_info['last']
    location = user_info['location']

    print("\tfull name :"+full_name.title())
    print("\tlocation: "+location.title())

