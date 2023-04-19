users = {
    'iusjd':{
        'first_name':'jiajia',
        'last_name':'chen',
         'age':23,
        'city':'zhangjiang',                
             },
    'wiejsjf':{
        'first_name':'ahjskh',
        'last_name':'sajfk',
         'age':19,
        'city':'shenzheng',    
        },
    'wsadf':{
        'first_name':'sjffsh',
        'last_name':'sfjahk',
         'age':19,
        'city':'guanzhou',    
        },
    
    }
for user_name,user_info in users.items():
    print("\nusername : "+user_name)
    full_name = user_info['first_name']+user_info['last_name']
    location = user_info['city']
    age = user_info['age']

    print("\tfull name: "+full_name.title())
    print("\tage: "+str(age))
    print("\tlocation: "+location.title())
print("--------------------------------------------")
user_1 = {
        'first_name':'jiajia',
        'last_name':'chen',
         'age':23,
        'city':'zhangjiang',                
             }
user_2 = {
        'first_name':'ahjskh',
        'last_name':'sajfk',
         'age':19,
        'city':'shenzheng',    
        }
user_3 = {
 
        'first_name':'sjffsh',
        'last_name':'sfjahk',
         'age':19,
        'city':'guanzhou',    
        }
peoples =[user_1,user_2,user_3]
for people in peoples:
    print(people)
print("------------------------------------------------")


favorite_number = {
    'chenjiajia':[7,34],
    'shfh':[8,89],
    'sjkfhs':[11,12,28,22],
    'sjfkahj':[12],
    'safjshf':[13,78,23],
    }
for name,numbers in  favorite_number.items():
    print("\nname: "+name)
n    for number in numbers:
        print("\tnumbers: "+str(number))
