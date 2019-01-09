from random import randint
import os


def boxprint(box_row, box_column, x, y, role):
	''' this func used For print map
		args:	
				box_row ,box_column --> count map row and column
				x,y --> for "role" variable index in map 
				role --> Character for print in map for example 'X'
		output:				
				print string for show current index of character 'X'.'''
	for i in range(box_row+1):
		for j in range((box_column*4)+1):
			if i==0:
				if j%4==0:
					print(' ',end='')
				else:
					print('_',end='')
			else:
				if j%4==0:
					print("|",end="")
				else:
					if i==((x-1)+1) and j==(((y-1)*4)+2):
						print(role,end='')
					else:
						print("_",end="")
		print('')
	print()
	print("you're currently in room ({},{})".format(x, y))
                

def check_inputvalue(value):
	''' check user input is numberic and bigger than 0 for row and column count.
		args:
			value: user input 
		return:
			-value with int type if user input is numberic
			- 0 if user input non numberic
	'''
	if value.isnumeric():
		return int(value)
	else:
		return 0


def check_count(input_count,input_type):
	'''check user input for row and column count.
	'''
	counts = check_inputvalue(input_count)
	while counts == 0:
		print("---> Pleae input a Valid input number (input>0)")
		again_counts_input = input("input count of {}s: ".format(input_type))
		counts = check_inputvalue(again_counts_input)
	return counts


# get row count and check is valid
row_input = input("input count of rows: ")
row_count = check_count(row_input,'row')

# get column count and check is valid
column_input = input("input count of column: ")
column_count = check_count(column_input,'column')

def check_value(x, y):
	''' generate  D(Door) and Z(Dragon) index and check Not Duplicate with X. 
		args:
			x,y= index of 'X' in map
		return:
			row_id,col_id = index of 'D' or 'Z' on map	
	'''
	row_id=randint(1,row_count)
	col_id=randint(1,column_count)
	#print('CHECK ',end=' ')
	#print(str(row_id)+','+str(col_id))
	if x==row_id and y==col_id:
		row_id=randint(1,row_count)
		col_id=randint(1,column_count)
	return row_id, col_id


def check_move(x, y):
	'''check availabel movement in index (x.y)
		args:
			x,y: current 'X' index on the map
		return:
			move_list: list af available movement include UP,DOWN,LEFT,RIGHT 	
	'''
	move_list = []
	if x-1 > 0:
		move_list.append('UP')
	if x+1<=row_count:
		move_list.append('DOWN')
	if y-1 > 0 :
		move_list.append('LEFT')
	if y+1 <= column_count:
		move_list.append('RIGHT')
	
	return move_list

# Genarate index of 'X'
x_i = randint(1, row_count)
x_j = randint(1, column_count)

# Generate index of 'D'(Door)
d_i, d_j = check_value(x_i, x_j)

# Generate index of 'Z' (Dragon)
z_i, z_j = check_value(x_i, x_j)


def check_status(x_location, y_location):
	'''check curent location of 'X' is same with 'D' or 'Z'
		args:
			x_location,y_location : current index of 'X' in map
		return:
			if find 'D' or 'Z' return True and print output for win or lose
		    if don't find 'D' or 'Z' return False	
	'''
	if x_location == d_i and y_location == d_j:
		print('----------------')
		print("    You Win")
		print('----------------')
		return True
	if x_location == z_i and y_location == z_j:
		print('----------------')
		print("    You Lose")
		print('----------------')
		return True
	return False	


def move(direction, now_x_i, now_x_j):
	''' get direction from user and change 'X' indexs
		args:
			direction: get value from user include UP,DOWN,LEFT,RIGHT
			now_x_i,now_x_j: current index of 'X' in map
		return:
			x,y : index of 'X' after direction	
	'''
	x=now_x_i
	y=now_x_j
	if direction == 'up':
		if now_x_i != 1:
			x = now_x_i-1
	if direction == 'down':
		if now_x_i != row_count:
			x=now_x_i+1
	if direction == 'left':
		if now_x_j != 1:
			y=now_x_j-1
	if direction == 'right':
		if now_x_j != column_count:
			y=now_x_j+1
	return x, y


def show(x,y):
	'''clear screan and print map and 'X'
		args:
			x,y: index of 'X' in map
		return:
			show map and information of 'X' current index
			return list of all Available movement of 'X' in current location
	'''
	os.system('clear') 
	boxprint(row_count, column_count, x, y, 'X')
	print()
	allow_movement = check_move(x, y)
	print('You can move :{}'.format(', '.join(allow_movement)))
	print('enter QUIT to quit Game.')
	return allow_movement


def check_user_input(user_input):
	'''check user input for move direction.
		args:
			user_input: user input
		return:
			True : if user input is in valid_word list otherwise return False
	'''
	valid_word=['up','down','left','right']
	if not user_input.lower() in valid_word:
		return False
	else:
		return True	

now_allow_movement=show(x_i, x_j)
now_x_i = x_i
now_x_j = x_j

while True:
	user_movment = input('> ')
	if user_movment.lower() == 'quit':
		print('GoodBy')
		break 
	if check_user_input(user_movment):
		current_x_i, current_x_j = move(user_movment,now_x_i,now_x_j)
		now_x_i=current_x_i
		now_x_j=current_x_j
		now_allow_movement=show(current_x_i,current_x_j)

		if check_status(current_x_i,current_x_j):
			break
	else:
		print('Plese input Valid input from {}, quit'.format(", ".join(now_allow_movement)))
		continue
