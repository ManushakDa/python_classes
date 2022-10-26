
# ex_1 
#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a python app which will ask day number, and return the day name (a string)
print(""" ""EX_1 WELCOME TO WEEK DAYS APP"" """)
sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6


week_dayes = int(input("Enter the day of the week you want to see.select the number from the table\n \
	Sundaye    enter 0\n \
	Monday     enter 1\n \
	Thursdaye  enter 2\n \
	Wednesday  enter 3\n\
	Thursday   enter 4\n\
	Friday     enter 5\n \
	saturday   enter 6 \n "))

if week_dayes == sunday:
    print ("Sunday")
elif week_dayes == monday:
    print("Mondaye")
elif week_dayes == tuesday:
    print("Tuesday")
elif week_dayes == wednesday:
	print("wednesday")
elif week_dayes == thursday:
	print("thusday")
elif week_dayes == friday:
	print("friday")
elif week_dayes == saturday:
	print("saturday")
else:
	print("it is a wrong week day\n")

# ex_2
# Write a python program which takes string as input then checks if there \
# is a space in string ( it means that users inputed the word or the sentence ) then print message for both cases " )

print(""" \t EX_2 "PROGRAM WILL CHEK SPACE IN STRING" """)

text_string = input("Please input word or sentence\n")
if " " in text_string:
    print ("Space exist in this word")
else:
	print("space not exist there \n")



# ex_3 Write a python program to check leap year without using datetime library

print("""\t EX_3 "THE PROGRAM WILL CHEK LEAP YEAR" """)
year = int(input("Please input year\n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print(year, "year is retreat")
else:
	print(year, "year is not retreat\n")




# ex_4 Write rock/paper/scissors game
print(""" \tEX_4""LETS PLAY GAME" """)

player1 = int(input(""" Player1 please enter 1,2,3 for  "stone = 1 " "paper = 2" "scissors = 3 "\t """))
player2 = int(input(""" Player2 please enter 1,2,3 for  "stone = 1 " "paper = 2" "scissors = 3 "\t """))

stone = 1
paper = 2
scissors = 3 

if(player1 == paper and player2 == payper) or (player1 == stone and player2 == stone) or (player1 == scissors and player2 == scissors):
	print ("NO ONE won")
elif (player1 == paper and player2 == stone) or (player1 == stone and player2 == scissors) or (player1 == scissors and player2 == paper):
	print ("player1 is won")
else:
	print("player2 is won")




aa











