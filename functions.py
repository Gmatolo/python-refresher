def func():
    print("Allows us to put code with a single purpose into a single location that \n that can be called in other locations within the codebase")

#calling function
func()
func()
func()
func()


def func():
    return 'Hello function'

print(func().upper())

func()

print("Working with default arguments")

def func_hello(greeting):
    return '{} Function'.format(greeting)


print(func_hello("greetings"))

def func_hello(greeting, name= "Gerald"):
    return '{}, {} Welcome' .format(greeting, name)

print(func_hello("Hello",))
print(func_hello("Hello", name = 'muli'))
