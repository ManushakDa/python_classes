# EX 2 -Write a short program that will covert °C to °F.

print("Please intput the °C you want to convert ")
c = input ()
f = float(c) * 1.8 + 32
print("result in °F = " , f )

# EX 3.a. -Create 3 variable ( a = 5, b = 6, c = 7),and write a program which sums and prints out

a = 5
b = 6
c = 7

print (( a + b + c ) / 3)   # 3.1 the average value of a, b, c


print(a ** c + b ** c)      # 3.2 a^c + b^c (2^4 in python is 2**4)


print ( (a + b) ** c )      # 3.3 (a + b)^c



Str_number = str (a) + str (b) + str (c) #abc + a*b*c  (for our case: 567 + 5*6*7)

print (int(Str_number) + a * b * c)


# EX 3 Python Function to Convert Kilometers to Miles( kilometers should give the user)

kilometer = input ("Please input kilometer\t"  )
one_mile_is_equal = 0.62137119
print ("Result in kilometers" ,  float ( kilometer )  * one_mile_is_equal )

# Ex 4 Write a python app which asks user’s age, and tells in which year he/she will become 100 years old

#print("how old are you")
user_age = int(input ("how old are you\t"))
remineder =  100 - user_age
print("You will became  100 year old after",remineder , "year")



