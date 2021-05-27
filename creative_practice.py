"""
example of a matrix in one line of code using 
list comprehension to set the parameters
below we have a list comprehension again squaring and
appending all numbers in range if they meet the conditional
"""

matrix = [[i for i in range(11) if i % 2 == 0] for y in range(11) if y % 2 == 1] 
print(matrix)


squares = []
[squares.append(i*i) for i in range(10) if i % 2 == 0]
print(squares)



"""in the first problem: 
Our function calculates the total sum of a given range
for our second problem:
we use try catch to assure we dont receive a TypeError
we incorporate a sum function to add our list
in our third line of code:
we use a lambda function to get a value from  range.
we do so by calling the variable with a an argument 
for lambda a 
"""

def add_up(n):
    return sum(range(n +1))
print(add_up(10))

from functools import reduce
numbers = [11,66,3,7,24,53,20]
print(reduce(lambda a, b: a if a > b else b, numbers))


def add(num):
    try:
        new = sum(num)
    except TypeError:
        new = 0
    return new
print(add([1,2,3,4,5]))


user = lambda a: range(a)[-1]
print(user(11))    


"""
using a try catch in our sum function
and our fractorial function
"""

def user(x):
    try:
        new = sum(range(x))
    except TypeError:
        return None
    return new
print(user(11))


def user(x):
    try:
        if x == 0:
            return 1
        else:
            return x * user(x-1)
    except TypeError:
        return None
print(user(5))


"""
in the example below we grab the square root of each
number in range of 10. we applied list comprehension
as well as an if statement that narrows down the odds
below that is a matrix being practiced
and at the bottom, we are practicing named arguments, kwargs
and unpacking.
"""

def user(x):
    try:
        new =  lambda a: [a * a for a in range(x) if a % 2 == 1]
        return new(0)
    except TypeError:
        return 0
print(user(10))


def user(n):
    numlist = [[None for y in range(n)] for x in range(n)]
    couter = 0 
    for a, b in enumerate(numlist):
        for c, d in enumerate(b):
            numlist[a][c] = couter + c
        couter += 1
    return numlist
print(user(5))


def user(time, *args, **kwargs):
    return f"I do say {kwargs['first']}, your wifes new {kwargs['mid']} really {''.join(args)}.\nId like to rest my bulging member on her face, letting {kwargs['new']} rest on the sockets of her eyes, mmm ahh yes, indubitably.\nPerhaps you and I, {kwargs['last']},could swap our two wives for a {time}. what do you say ol chum?"
print(user('night','tickles ', 'my ' 'fancy', mid = 'front rack', first = 'RowQuan, from house dirty dingle berry', last = 'flaxseedMaxy', new = 'my heavy sack of two'))


"""
here we created a function that passes the alpha
and returns the character after. starting back with 'a'
just below:
we built a function that takes in any string of words
and returns the following letter of each letter
"""

class Invoice:
    def user(self):
        for i in range(ord('a'), ord('z')):
            print(chr(i + 1))
        if ord(chr(i)) == (ord('z') -1):
            print(chr(i).replace(chr(i), chr(ord('a'))))
        else:
            print('no')
name = Invoice()
name.user()


import string

x = string.ascii_lowercase
class Invoice:
    def user(self, x, y):
        for i in x:
            print(chr(ord(i)+ y))    
name = Invoice()
name.user(x, 1)


"""
here is an example of a single line code grabing each letter 
of the alph.
"""

for i in range(ord('a'), ord('z')+1):
    print(chr(i))

"""
here we build a complex filter that returns
every letter thats not a vowel. 
this type of code could possibly be used in
a DIVIDE AND CONQUER algorithm// maybe
"""

name = 'hey do you think well be getting out early today?'
def user(letter):
    var = 'aeiou'
    return letter.isalpha() and letter.lower() not in var
constants = [i for i in name if user(i)]
print(constants)

