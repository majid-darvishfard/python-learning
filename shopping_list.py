import os
import json

categorys=['cloth','citrus','supermarket','book','food']

def show_help():
    '''print Help Message
    '''
    print('1- Enter "DONE" for stop adding items.')
    print('2- Enter "HELP" for show all instructions in our app.')
    print('3- Enter "SHOW" for show all items in our shopping list.')
    print('4- Enter "UPDATE" for edit items.')
    print('5- Enter "REMOVE" for remove item from list.')
    print()


def clear():
    os.system('cls') if os.name=='nt' else os.system('clear')

def check_item_exist(item_name):
    '''check item exist and return it category
        args:
            item_name
        return:
            if item exist,return item category otherwise None return    
    '''
    for category,value in items_dic.items():
        for name,count in value.items():
            if name == item_name:
                print('item "{}" is in category "{}"'.format(name,category ))
                return category,name,count



def get_category(item_name):
    '''check if item is exist return item category 
      otherwise get item category from user and check that is valid 
        args:
            item_name
        return:
            user input category
    '''
    check_item_category=check_item_exist(item_name)
    if check_item_category != None:
        category,name,count=check_item_category
        return category
    else:    
        print('please input suitable category for item "{}" from the list ({}) '.format(item_name,', '.join(categorys)))
        input_category= input('category>> ')
        while (input_category not in categorys):
            print('please input suitable category for item "{}" from the list ({}) '.format(item_name,', '.join(categorys)))
            input_category= input('category>> ')
        return input_category        


def show_value(show_all=False):
    '''print all categorys items or show specific category
    '''
    if not show_all:
        print('show>> what you want to show .')
        print("enter 'all' or category name({})".format(', '.join(categorys)))
        show_input=input('show>> ').lower()
        if show_input == 'all':
            if items_dic != {} :
                for category,value in items_dic.items():
                    for name,count in value.items():
                        print('category "{}" --> item:"{}" , count:"{}"'.format(category,name,count ))
            else:
                print("It's Empty.No Items Found.")

        elif items_dic.get(show_input) == None:
            show_value()
        elif items_dic.get(show_input) == {}:
            print('Your Category in empty.')
        else:
            value_dic=items_dic[show_input]
            for name,count in value_dic.items():
                    print('category "{}" --> item:"{}" , count:"{}"'.format(show_input,name,count ))   
    else:
        print('your final list is :')
        for category,value in items_dic.items():
            for name,count in value.items():
                print('category "{}" --> item:"{}" , count:"{}"'.format(category,name,count ))

def show_availabe_item(my_dic):
    ''' create list of all items
        return:
            items list
    '''

    item_list=[]
    for category,value in my_dic.items():
        for name,count in value.items():
            item_list.append(name)
    return item_list        


def get_Value():
    '''get user input and run suitable function
        return:
            item_name,item_count,item_category
    '''
    print()
    print('input items and count: ')
    value = input('item>> ')
    if value.isalpha():
        if value=='help':
            clear()
            show_help()
        elif value=='show':
            clear()
            show_value() 
        elif value=='done':
            show_value(show_all=True)
            return False
        elif value=='update':
            clear()
            update()
        elif value=='remove':
            clear()
            remove()    
        else:
            value_count=input('count>> ')
            if value_count.isdecimal():
                value_category=get_category(value)
                return value,value_count,value_category
            else:
                print('please input valid item count.') 
                get_Value()
    else:
        print('please input valid items.')
        get_Value()    


def update():
    '''get item for update and check that 
    '''
    print('input item name for edit: ')
    print('available items is : {}'.format(' ,'.join(show_availabe_item(items_dic))))
    input_update=input('update>>')
    item_found=check_item_exist(input_update)
    if item_found != None:
        category,name,count=item_found
        print ('Item information is:')
        item_info(name,count,category)
        print('Which item property you want to change? (name,count,category)')
        change_input=input('update>>').lower()
        while change_input not in ('name','count','category'):
            print('input Valid item property. (name,count,category)')
            change_input=input('update>>').lower()
        update_item(name,category,change_input)
    else:
        print('input Item not Found!')
        update()

def update_item(item,item_category,item_change):
    ''' update items property in the items_dic
        args:
            item: item name for update
            item_category 
            item_change: item property for update(name-count-category)
    '''
    if item_change == 'name':
        new_item_name=input("update>> input new item name: " ).lower()
        for category,value in items_dic.items():
            for name,count in value.items():
                if name==item:
                    value[new_item_name]=value.pop(item)
                    print('Successfuly Update item name "{}" to "{}."'.format(item,new_item_name))
    elif item_change == 'count':
        new_item_count=input("update>> input new item count: ")
        for category,value in items_dic.items():
            for name,count in value.items():
                if name==item:
                    value[item]=new_item_count
                    print('Successfuly Update item name "{}" to "{}."'.format(count,new_item_count))      
    elif  item_change == 'category':
        new_item_category=input("update>> input new item category: ")
        while (new_item_category not in categorys):
            print('please input valid category from the list ({}) '.format(', '.join(categorys)))
            new_item_category= input('update>> ')

        if (new_item_category not in items_dic.keys()):
            items_dic[new_item_category]=items_dic.pop(item_category)
        else:
            items_dic[new_item_category]={**items_dic.pop(item_category),**items_dic[new_item_category]}
        print('Successfuly item "{}" category changed to "{}"'.format(item,new_item_category))
            
        
def remove():
    '''get item name from user and check item found 
    '''
    print('input item name for remove: ')
    print('available items is : {}'.format(' ,'.join(show_availabe_item(items_dic))))
    input_remove=input('remove>>').lower()
    item_found=check_item_exist(input_remove)
    if item_found != None:
        category,name,count=item_found
        print ('Item information is:')
        item_info(name,count,category)
        user_input=input('Are you Sure Delete item ?  [y/n] ').lower()
        if user_input == 'y':
            remove_item(name)
            print('Item "{}" with Count "{}" Removed in Category "{}." '.format(name,count,category))      
        elif user_input == 'n':
            print("Nothing Change.")    
        else:
            remove()    
    else:
        print('input Item not Found!')
        remove()

def remove_item(item):
    ''' remove item from item_dic
    '''
    for category,value in items_dic.items():
        value.pop(item)


def item_info(item_name,item_count,item_category):
    '''print item information 
    '''
    print()
    print( 'Item Name: {} '.format(item_name))
    print('Item Count: {}'.format(item_count))
    print('Item Category: {}'.format(item_category))
    print('-'*30)


def want_save(item_name,item_count,item_category):
    '''check uesr for save items
    '''
    user_input=input('Want  Save The Items? [y/n] ').lower()
    if user_input == 'y':
        save(item_name,item_count,item_category)
        print('Item "{}" with Count "{}" saved in Category "{}." '.format(item_name,item_count,item_category))      
    elif user_input == 'n':
        print("Don't Save Items.")    
    else:
        want_save()    


def save(item_name,item_count,item_category):
    '''save user item in items_dic dictionary in format {item_category:{item_name:item_count}}
    '''
    value_count_dic={}
    value_count_dic[item_name]=int(item_count)
    if items_dic.get(item_category) == None:
        value_count_dic[item_name]=int(item_count)
        items_dic[item_category]=value_count_dic
    else :
        for value, count in items_dic[item_category].items():
            if value == item_name:
                value_count_dic[value] += int(count)
        items_dic[item_category].update(value_count_dic)
    write_file(file_path)
    return items_dic

def get_username():
    print('Please input yuor NAME: ')
    username=input('username>> ')
    return username

def write_file(file_path):
    '''write Current state of user items in file
    '''
    json_f = json.dumps(items_dic)
    f=open(file_path,'a')    
    f.write(json_f+ os.linesep)
    f.close()

def get_favorite():
    '''read file and return items 
    '''
    favorite=set()
    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            for line in read_file:
                j_line=json.loads(line.strip())
                favorite_items=show_availabe_item(j_line)
                favorite.update(favorite_items)
    return favorite


#create directory for save  user file 
directory_name='user_shopping'
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
directory_path=os.getcwd()+'/'+directory_name

clear()
print()
username=get_username()
file_path=directory_path+'/'+username
print('                      Welcome {}'.format(username))
print('--'*30)
favorit=get_favorite()
if favorit :
    print('Your Favorit Items is {} '.format(', '.join(favorit)))
    print('--'*30)

print ("What Should We Use at the Store ? ")
print()
show_help()
print('Ready to input? (press any keys)')
input()
clear()

items_dic={}
while True:
    values=get_Value()
    if values == False:
        break
        print('GoodBye')

    if values != None:    
        item_name,item_count,item_category=values
        item_info(item_name,item_count,item_category)
        want_save(item_name,item_count,item_category)
