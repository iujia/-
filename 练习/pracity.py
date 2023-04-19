
def make_album(name,album):
    sing = {'name':name,'album':album,}     
    return sing


while True:
    print("\nPlease tell me your love sings and album:")
    print("(enter 'q' at any time to quit)")
    l_names=input("sing name: ")
    if l_names == 'q':
        break

    
    l_alibums=input("alibum:")
    if l_alibums == 'q':
        break


    message = make_album(l_names,l_alibums)
    print(message)

    
    







