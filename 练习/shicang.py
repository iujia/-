def describe_pet(pet_name,animal_type = 'dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")



describe_pet(pet_name = 'momo')
describe_pet('nono')
describe_pet('wou','cat')
describe_pet(animal_type = 'hamster', pet_name = 'bobo')
print("-----------------------------------------------------------")


def get_formatted_name(first_name,last_name,middle_name = ''):
    """返回整洁的名字"""
    if middle_name:
        full_name = first_name + " "+middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name    
    return full_name.title()

message = get_formatted_name('jiajia','chen')
print(message)

message = get_formatted_name('wu','hua','sff')
print(message)

print("-----------------------------------------------------------")

def build_person(first_name,last_name,age = ''):
    person = {'first':first_name,'last':last_name,}
    if age:
        person['age'] = age
    return person

musician = build_person('jiajia','chen',age=27)
print(musician)



def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name,}
    if age:
        person['age'] =age
    return person
message =  build_person('hjsf','sfhsja',age = 28)
print(message)
        





















