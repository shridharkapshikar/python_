"""
Experimenting with arithmetics

"""

number_one = 9
number_two = 3

#addition
result = number_one + number_two
print("The sum of both numers is %d" %(result))
#subtraction
result = number_one - number_two
print(result)
#multiplication
result = number_one * number_two
print(result)
#division
result = number_one / number_two
print(result)
#modules
result = number_one % number_two
print(result)
#floor division
result = number_one // number_two
print(result)
#exponents
result = number_one ** number_two
print(result)

#built in python function

#abs
negetive_number = 13
print("The positive value is %d"%(-1*negetive_number))
print("The positive value is %d"%(abs(negetive_number)))

#divmod
quotient_remainder_combined = divmod(number_two, number_two)
print(quotient_remainder_combined)

#power function
exponent_number = pow(9,3)
print(exponent_number)

#int and float

random_number =  20.3
print(int(random_number))

random_number_two = 20
print(float(random_number_two))

#booleans

boolen_true = True
boolen_false = False
print(boolen_false, boolen_true)

