sandwich_orders = ['pastrami','apple','pastrami','blan','sjfh','pastrami']
finished_sandwiches = []


while sandwich_orders:
    current = sandwich_orders.pop()
    finished_sandwiches.append(current)
    

print("I made your tuna sanfdwich")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
print(finished_sandwiches)
print("-------------------------------------------------------------")

dreams = {}

polling_active = True

while polling_active:
    name = input("\nwhat is you name? ")
    places = input("\nwhere is your love places?")
    
    #将信息存储在字典
    dreams[name] = places

    repeat = input("would you like to let another person places ?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---poll result---")
for name, places in dreams.items():
    print(name+" would go to "+places+".")
    
