print()
print ("What Should We Use at the Store ? ")
print()

#Show Help Message
def show_Help():
    print('1- Enter "DONE" for stop adding items.')
    print('2- Enter "HELP" for show all instructions in our app.')
    print('3- Enter "SHOW" for show all items in our shopping list.')
    print('4- Enter "UPDATE" for edit items.')
    print('5- Enter "REMOVE" for remove item from list.')
    print()

#Get Value From User
def get_Value():
    value = input('> ')
    if value.isalnum():
        return value

##for edit item in lists
def edit_Item(item):
    if item in values:
        new_item=input('--update>> please input new item : ')
        values[values.index(item)]=new_item
        print('Successfully update "{}" to "{}".'.format(item,new_item))
    else:
        print('item "{}" not found in list !!'.format(item))    

#for remove item from list
def remove_Item(item):
    if item in values:
        print('are you sure to removing item "{}" from the list?(yes or no)'.format(item)) 
        while True:
            a=input('--remove>> ')
            if a =='yes':
                values.remove(item)
                print("--remove>> item {} removed.".format(item))
                break
            elif a=='no':
                print()
                break
            else:
                print('please input yes or no.')          
    else:
        print('item "{}" not found in list !!'.format(item))

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
        elif value=='update':
            if len(values)!=0:
                print('Which item do you want to change?  ' + ', '.join(values))
                item=input('--update>> ')
                edit_Item(item)
            else:
                print('Your List is empty.')
        elif value=='remove':
            if len(values)!=0:
                print('Which item do you want to remove?  ' + ', '.join(values))
                item=input('--remove>> ')
                remove_Item(item)

            else:
                print('Your List is empty.')
                
        else:
            if value not in values:
                values.append(value)
                print("Successfully Add '{}' to list. Your List Lenght is {}".format(value,len(values)))
            else:
                print("Your input valuses '{}' is duplicate.".format(value))