import string
import random

a_list=['a','b','c','d','e','f','g','h','i','k','l','o','q','s','t','v','x','y']
b_list=[['@','^','A','a'],['b','8','B'],['c','(','30','C'],['6','D','d'],['3','E','e'],
		['#','F','f'],['9','G','g'],['#','H','h'],['i','!','1','I'],['i<','K','k'],['L','l'],['0','*','O','o'],['9','Q','q'],['5','$','z','S','s'],['t','+','T'],['<','v','>','V'],['x','%','X'],['y','?','Y']]

def check_username(uname):
	if not 8<= len(uname) <=20 :
		return False
	else:
		return True	

def replace_char(username):
	chars = string.ascii_letters
	digit=string.digits
	password=[]
	for item in username:
		if item in a_list :
			item_index=a_list.index(item)
			if type(b_list[item_index]) is list:
				replace_item=str(random.choice(b_list[item_index]))
			else:
				replace_item=str(b_list[item_index])
			password.append(replace_item)	
		elif item.isalpha():
			replace_item=item.upper()
			password.append(replace_item)
		else:
			password.append(item)	
	#	item_index_username=username.index(item)
	return password		

while True:
	print('Please input your Username: (8-20 character)')
	username=input('> ')
	if check_username(username):
		for i in range(8):
			passwd=replace_char(username)
			print(''.join(passwd))
		break;
	else:
		print('please input valid username!!')
		check_username(username)	