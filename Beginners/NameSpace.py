#name space

name = "Shridhar Kapshikar"

def home():
    name = "Jordan"

    def sister():
        nonlocal name
        name = "Dude"

    print("the value of name currently is %s" % name)
    sister()
    print("the name now is %s" % name)


home()
#2 built in functions.
print(globals())
print(locals())

