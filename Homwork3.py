
from Rate1 import *

# # EX_1 create an app which will exchange the given amount of money to dollar, dollar rate should be taken from another file
# from Rate1 import *
# currency_name = input("input currnecy name \t")
# amount = float(input("input amount you need to convert\t") )
# print(amount,currency_name ,"  will be ", amount * usd_rate, "USD")

# EX_2 Ask user his height and tell him the optimal weight depending of his height. Google will help you to calculate this.


# ideal_weight = height - 100
# print( "your optimal weight will be \t" ,ideal_weight)

# Ex_3 Write python program for food court. There should be a menu with two dishes, pizza and kebab, and two additions ketchup, “Mayonez” all should have their prices. Depending on the answers of the user the value of the price row should be True .
# pizza = 1000 , kebab=800, ketchup = 100, Mayonez = 500
# EX. User ordered pizza with ketchup then in terminal should be seen
# 	You have ordered pizza with Mayonez and your price is 1500 => False
#         You have …
#         You have …
# 	You have ordered pizza with Ketchup and your price is 1100 => True
# You should NOT use if/elif/else statement

pizza_price = 1000 
kebab_price = 800
ketchup_price = 100
mayonez_price = 500

order_1 = pizza_price + ketchup_price
order_2 = pizza_price + mayonez_price
order_3 = kebab_price + ketchup_price
order_4 = kebab_price + mayonez_price
order_5 = kebab_price
order_6 = pizza_price




print(( order_amount == order_1 ) *  " ordered pizza with ketchup and your price is 1100", end = "")
print(( order_amount == order_2 ) *  " ordered pizza with mayonez and your price is 1500", end = "")
print(( order_amount == order_3 ) *  " ordered kebab with ketchup and your price is 900", end = "")
print(( order_amount == order_4 ) *  " ordered kebab with mayonez and your price is 1300", end = "")
print(( order_amount == order_5 ) *  " ordered kebab and your price is 800", end = "")
print(( order_amount == order_6 ) *  " ordered pizza and your price is 1000", end = "")
print(((( order_amount != order_1) or ( ordeder_amount != order_2 ) or ( ordeder_amount != order_3 ) or ( ordeder_amount != order_4 ) or
	( ordeder_amount != order_5 ) or ( ordeder_amount != order_6 ))   * "You didnt enter right order price "))
