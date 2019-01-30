#program
# **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
#
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output :
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
#
# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
#
# If you feel ambitious, explore the Collections module to solve this problem!

# def count(s):
#     if s.isupper():
#         cnt = cnt + len(s.isupper())
#         retunr(cnt)
#
# print (count('Shridhar'))
count1 = 0
count2 = 0
string =  'Hello Mr. Rogers, how are you this fine Tuesday?'
for a in string:
    print(a)
    if (a.islower()):
        count1 = count1 + 1
    elif (a.isupper()) == True:
        count2 = count2 + 1

print("The numer of lowercase is: "+ str(count1))

print("The numer of uppercase is: " + str(count2))


