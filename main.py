
#Initialize
import os
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()

#Start character in Room 1
game = 0
#All floors and tracking user location
land_1 = [[0,2,3],[4,5,0],[0,8,0]]
user_location = land_1[1][1]
Land_2 = [[0,0,0],[0,0,0],[0,0,0]]
Land_3 = [[0,0,0],[0,0,0],[0,0,0]]
user_inv =[]

#All floor maps
def bird_land_1():
  for row in land_1:
      print(row)
def bird_land_2():
  for row in Land_2:
      print(row)
def bird_land_3():
  for row in Land_3:
      print(row)

#Things you can do
def help_():
	print (Fore.YELLOW + 'Help with Objective,Options,Invintory')
	command = input("What do you need help with \n >"  )
	if command.lower().strip() == 'objective':
		print ('The objective of the game is to escape the subway station you may have to find keys or slay monsters to do so')
	if command.lower().strip() == 'options':
		print ('Type move to move from room to room or type the same number room youre in to stay in that room \n Type examine to take a closer at the room youre in \n Type pick up to take items you want\n Type inventory to view all items in your inventory ')
	if command.lower().strip() == 'inventory':
		print ('This is where all the items youve collected are type open inventory to see the list of items you cureently have you may use items by typing use (chosen item)')
def examine():
		if user_location == 2:
			print (Fore.LIGHTMAGENTA_EX +'While taking in the room you notice that you can see your reflection in anything,there appears to be a foul smell coming from the west staircase'+ Fore.RESET + Fore.YELLOW)
		elif user_location == 3:
			print(Fore.LIGHTMAGENTA_EX +'The rat appears to have a limp leg if you attack quick enough you might kill it'+ Fore.RESET + Fore.YELLOW)
		elif user_location == 4:
			print (Fore.LIGHTMAGENTA_EX +'While taking in the subway cart you notice that you cant see your reflection in anything,there appears to be an umbrella and a bag on the floor'+ Fore.RESET + Fore.YELLOW)
		elif user_location == 5:
			print (Fore.LIGHTMAGENTA_EX +'you stand on the train platform and notice its seem as though its been abandon quite a while you wonder if the rats took over?'+ Fore.RESET + Fore.YELLOW) 
def pick_up():
	command = input("What do you wish to pick up \n >"  )
	if user_location == 4 and command == 'umbrella':
		user_inv.append('umbrella')
		print ('You have picked up the umbrella it is now in your inventory')
	if user_location == 3 and command == 'key':
		user_inv.append('key')
		print ('You have picked up the key it is now in your inventory')
def inventory():
	print (user_inv)

def fight_scene_1():
	global user_location
	global game
	H = 10
	print (Fore.LIGHTMAGENTA_EX + 'A rat appears on the staircase' + Fore.RESET + Fore.YELLOW)
	print(Fore.LIGHTMAGENTA_EX +'The rat lunges at you but misses, what do you do'+ Fore.RESET + Fore.YELLOW)
	command = input("\n >"  )
	if command == 'attack':
		rat = random.randint(1,10)
		print (rat)
		H - (rat)
		if H <= 10:
			command = input("\n >"  )
			if command == 'attack':
				rat = random.randint(1,10)
				print (rat)
				H - (rat)
			elif command == 'befriend':
				print ('you die')
				game + 1
	if command == 'befriend':
		print ('you die')
		game + 1


	


#Give the option of things you can do
def action():
	command = input("What do you wish to do \n >"  )
	if command == 'examine':
		examine()
	if command == 'help':
		help_()
	if command == 'pick up':
		pick_up()
	if command == 'inventory':
		inventory()
	if command == 'move':
		user_moving_1()

#All floor rooms
def bird_land_1_rooms():
	global user_location
	if user_location == 0:
		print(Fore.YELLOW+'NOT A ROOM TRY AGAIN')

	if user_location == 2:
		print (Fore.LIGHTMAGENTA_EX + 'up the stairs,theres an exit to the west leading up to the street' + Fore.RESET + Fore.YELLOW)
		action()

	if user_location == 3:
		print('Options attack the enemy,move back to the previous room,befriend the rat? ')
		action()
		fight_scene_1()

	if user_location == 4:
		print (Fore.LIGHTMAGENTA_EX + 'open subway cart ' + Fore.RESET + Fore.YELLOW)
		action()


	if user_location == 5:
		print (Fore.LIGHTMAGENTA_EX + 'You awaken in what looks like an empty subway station there appears to be an EXIT sign to the north up the stairs an open Subway cart to your west and a locked bathroom to the south ' + Fore.RESET + Fore.YELLOW )
		action()
				
	if user_location == 8:
		command = input("What do you wish to do \n >"  )
		if command == 'use key' or 'key' and 'key1' in user_inv:
			print (Fore.LIGHTMAGENTA_EX + 'The bathroom apears to have bare white walls with five stalls and five sink the mirrors seem to have been taken of the wall and only a black outline of what was once there ' + Fore.RESET + Fore.YELLOW)
		else:
			print (Fore.LIGHTMAGENTA_EX + 'This room is locked' + Fore.RESET + Fore.YELLOW)	
#not done floor 2 make floor list first
def bird_land_2_rooms():
	global user_location
	if user_location == 0:
		print('NOT A ROOM TRY AGAIN')
	if user_location == 2:
		print (Fore.LIGHTMAGENTA_EX + ' ' + Fore.RESET + Fore.YELLOW)
	if user_location == 3:
		print (Fore.LIGHTMAGENTA_EX + '' + Fore.RESET + Fore.YELLOW)
	if user_location == 4:
		print (Fore.LIGHTMAGENTA_EX + 'open subway cart ' + Fore.RESET + Fore.YELLOW)
	if user_location == 5:
		print (Fore.LIGHTMAGENTA_EX + 'You awaken in what looks like an empty subway station there appears to be an EXIT sign to the north up the stairs an open Subway cart to your west and a locked bathroom to the south ' + Fore.RESET + Fore.YELLOW )	
	if user_location == 6:
		print('NOT A ROOM TRY AGAIN')
	if user_location == 7:
		print('NOT A ROOM TRY AGAIN')
	if user_location == 8:
		print (Fore.LIGHTMAGENTA_EX + ' locked bathroom' + Fore.RESET + Fore.YELLOW)	
	if user_location == 9:
		print('NOT A ROOM TRY AGAIN')

#All user movings
def user_moving_1():
	global user_location
	command = int(input("Which room do wish to go to \n >"  ))

	if command == 4 and user_location == 5 or user_location == 4:
		user_location = land_1[1][0]
		print (user_location)
	elif command == 4 and user_location != 5:
			print('you cant walk through walls')

	elif command == 8 and user_location == 5 or user_location == 8:
		user_location = land_1[2][1]
		print (user_location)
	elif command == 8 and user_location != 5:
			print('you cant walk through walls')

	elif command == 2 and user_location == 5 or user_location == 3 or user_location == 2:
		user_location = land_1[0][1]
		print (user_location)
	elif command == 2 and user_location != 5 or user_location != 3:
			print('you cant walk through walls')

	elif command == 3 and user_location == 2 or user_location == 3:
		user_location = land_1[0][2]
		print (user_location)
	elif command == 3 and user_location != 2:
			print('you cant walk through walls')

	elif command == 5 and user_location == 4 or user_location == 2 or user_location == 8 or user_location == 5:
		user_location = land_1[1][1]
		print (user_location)
	elif command == 5 and user_location != 2 or user_location != 4 or user_location != 8:
			print('you cant walk through walls')

	else :
		print ('that room isnt real here')


def print_header():
	os.system("clear")
	print (Fore.CYAN +''' 
  ________           
 /_  __/ /  ___      
  / / / _ \/ -_)     
 /_/ /_//_/\__/      
    __  ____________ 
   /  |/  /_  __/ _ |
  / /|_/ / / / / __ |
 /_/  /_/ /_/ /_/ |_|                 
'''+ Fore.RESET)
#Show start screen
print_header()
print (Fore.CYAN+"""
Welcome To Escape From The MTA
""" + Fore.RESET )
delay = input(Fore.YELLOW + "Press ENTER to continue." + Fore.RESET)


#Main Loop
while game <= 1:

	#Print the header
	print_header()
	#Describe location
	print ( Fore.YELLOW + "You are in room " + str(user_location) + Fore.YELLOW )
	bird_land_1() 
	bird_land_1_rooms()


	#After all is said and done and before loop repeats, pause
	delay = input("\nPress ENTER to continue.")