"""
Experimenting with variables & string formatting

"""

my_name = "Shridhar Kapshikar"
first_number = 20
second_number = 10

#print(my_name, first_number, second_number)

#print("Hi ! My name is", my_name, "I am from Amsterdam")

## String formatting

print("My name is %s. I am from Amsterdam"%(my_name))

print("Hi ! The two numbers I have are %d and %d"%(first_number, second_number))

print("Hi ! The two numbers I have are %0.2f and %0.2f"%(first_number, second_number))


# python built in function .format
print("----- built in function")
print("My name is {}. I have {} and {} numbers".format(my_name, first_number, second_number))