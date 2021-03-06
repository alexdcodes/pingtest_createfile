x, y, z = 1, 2, 3

print x, y, z

name = raw_input("What is your name? ")
if name.endswith('Alex'):
    if name.startswith('Mr.'):
        print 'Hello Mr. Alex'
    elif name.startswith('Mrs.'):
        print 'Hello Mrs. Alex'
    else:
        print 'Hello, Alex'
else:
    print 'Hello, Stranger'


def enter_number():

    num = input("Enter a number: ")
    if num > 0:
        print 'The number is positive'
    elif num < 0:
        print 'The number is negative'
    else:
        print 'The number is zero'


enter_number()


def boolean_operators():

    number = input("Enter a number from 1 to 10: ")
    if number <= 10:
        if number >= 1:
            print 'Great!'
        else:
            print 'Wrong!'
    else:
        print 'Wrong!'


boolean_operators()


# Loop 1 - 100
def while_loop():

    x = 1
    while x <= 100:
        print x
        x += 1


while_loop()


# Keyword Parameters and Defaults

def hello_1(greeting, name):
    print '%s, %s!' % (greeting,name)


def hello_2(name, greeting):
    print '%s, %s!' % (name,greeting)


def hello_3(greeting='Hello', name='world'):
    print '%s, %s!' % (greeting,name)


hello_1('Hello', 'World')
hello_2('Hello', 'world')
hello_3(name='Alex')


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.ammend(full_name)
            else:
                data[label][name] = [full_name]


d = {}
init(d)
store(d, 'Han SwiftDeveloper')
lookup(d, 'last', 'Skywalker')
print lookup(d, 'last', 'SwiftDeveloper')

