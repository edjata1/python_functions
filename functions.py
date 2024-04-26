print('*********** Functions are reusable blocks of code *************')
print()
print('*********** simple function *************')
def hello_world():
    print("Hello World")

hello_world()

print()
print('*********** naming functions all (lower case and _) *************')

print()
print('*********** function receive data called parameters *************')

# pass in parameters-> Never change
def sum(num1, num2):
    print(num1 + num2)

# pass in arguments-> Change (Data in function)
sum(5, 7)
sum(3, 48)
sum(100, 3)

print()
print('*** reusable function, Return value to function us in program *************')

def mul(num1, num2):
    return num1 * num2

total = mul(2, 3)
print(total)

print(),
print('*********** verify recieving numbers *************')

def subtra(num1, num2):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return
    return num1 - num2

total = subtra("a",3)
print(total) # output: None


print()
print('*********** What happens if nothings passed in *************')

def subtra(num1, num2):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return
    return num1 - num2
# This line causes an error:
# total = subtra()
print(total)

print()
print('*********** Giving Default values *************')

def subtra(num1=0, num2=0):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return
    return num1 - num2

total = subtra()
print(total) # output: None

# default values of 0
def subtra(num1=0, num2=0):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return
    return num1 - num2

total = subtra(1, 2)
print(total) # output: None

print()
print('*********** passing 1 Default value *************')
def subtra(num1, num2=3):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return
    return num1 - num2

total = subtra(1)
print(total) # output: None

print()
print('*********** return default value w/return *************')

# default values of 0
def subtra(num1=0, num2=0):
    # check parameters
    if(type(num1) is not int or type(num2) is not int):
        # early return 
        return 555
    return num1 - num2

total = subtra()
print(total) # output: None

print()
print('*********** unknown # of agruments function type tuple *************')

def multipe_items(*args):
    print(args)
    print(type(args))
    print(len(args))

multipe_items("Mike", 5, 'pete',{"key":"value"}, ["Kiv"])

print()
print('**key word arguments naming unknown arguments type dictionary *************')

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(len(kwargs))

multi_named_items(first = "Mike", last = 'pete')










