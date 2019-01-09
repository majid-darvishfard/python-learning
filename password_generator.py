import string
import random

def check_password_input(password):
	'''check input password lenght is valid(numeric and at least 8)
		args:
			password: user input
		return:
			password lenght	
	'''
	while not password.isnumeric():
		password = input('please input integer: ')
	
	if int(password) < 8:
		password = 8
	return int(password)

def random_password(pass_lenght):
	'''generate random string with dynamic lenght
		args:
			pass_lenght: password lenght
		return:
			generated password with pass_lenght size 
	'''
	chars = string.ascii_letters+string.digits+'!@#$%^&*_+'
	return ''.join(random.choice(chars) for char in range(pass_lenght))


pass_lenght_input=input('please enter password lenght. (lenght > 8): ')
password_lenght = check_password_input(pass_lenght_input)
print()	

# generate 10 password and print 
for i in range(10):
	print('pass {}: '.format(i+1)+random_password(password_lenght))