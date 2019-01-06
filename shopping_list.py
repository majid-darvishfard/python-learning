## Majid DarvishFard
#For Print LOGO 
print()
print('=' * 38)
print('=='+' '*10+ 'Shopping_List'+" "*10 +' ==')
print('=' * 38)
print()
print ("What Should We Use at the Store ? ")
print()

#Show Help Message
def show_Help():
    print('1- Enter "DONE" to stop adding items.')
    print('2- Enter "HELP" to show all instructions in our app.')
    print('3- Enter "SHOW" to show all items in our shopping list.')
    print()

#Get Value From User
def get_Value():
    value = input('> ')
    if value.isalnum():
        return value


show_Help()
values=[]
while True:
    value = get_Value()
    if value is not None:
        value = value.lower()
        if value=='help':
            show_Help()
        elif value=='show':
            print(values) 
        elif value=='done':
            print("Your List element Is {} .".format(', '.join(values)))
            break   
        else:
            if value not in values:
                values.append(value)
                print('\033[32m'+"Successfully Add to list. Your List Lenght is {}".format(len(values))+'\033[0m')
            else:
                print('\033[31m'+"Your input valuses '{}' is duplicate.".format(value)+'\033[0m')
