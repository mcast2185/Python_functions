# #1
# in these set of examples i aimed to utilize multiple sorts of methods  
# in order to grasp the complexity and power of functions. by doing so it highlights 
# how narrow/ percise i choose my return value to be when creating my matrix.
# (for loops, list comprehension, if statements) 
# 
# the second example is meant to exercise more methods and statements so to
# fill the empty list of squares.


# matrix = [[i for i in range(15) if i % 2 == 0] for x in range(19) if x % 2 == 1]
# print(matrix)

# squares = []
# [squares.append(i*i) for i in range(20) if i % 2 == 0]
# print(squares)



# #2
# here, in our example directly below, i created a form of functionality which
# takes the value/ number and returns the total sum of its range, meaning,
# if the value is 10, then i want my return to be the total of:
# (0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
# 
# in the following block of code, i imported a local library in python to 
# leverage the functionality of reduce, coupled with a lambda function, to exahust the elements inside the list.
# i used the power of reduce with a conditional statement to return a specific value
# which was the greatest number within the list.
# (import, reduce, lambda, if statement)
#
# for the third example, i exercise the functionality of lambda to store the value in
# range of the number passed. i chose to place this particular, and rather small, line of code
# here so to highlight that, although, user is a variable; once called in the print statement,
# user passes an argument as though it was a function. we do this because our lambda function expects
# something to satisfy its argument of a. by using negative index, in this case, we can grab any of
# the values created in range.


# def add(number):
#     return sum(range(number + 1))
# print(add(10))

# from functools import reduce
# num = [23,45,12,43,11,10]
# print(reduce((lambda a, b: a if a > b else b), num))

# user = lambda a: range(a)
# print(user(11)[-1])   



# #3
# below, we are creating a caesar cipher. we leverage many methods in 
# route to forming our algorithm, as well as importing a string value of the alphabet.
# the usecase of the function is to create an encryprtion which takes the value 
# of a letter being passed as an argument and shifts it over by the number of spaces passed 
# as its second argument, meaning, if my first argument is the letter a and my second arument
# is the number 2 then the return value would be the letter c.
# we do this by assigning each letter a numeric value and giving it parameters to stay within,
# as in only stay within the frame of the alphabet, dont reach to numbers higher then the 
# highest value of the alphabet nor lowest.
# so while the first function assigns each letter a numeric value as well as setting the parameters,
# the second function creates an iteration of the imported alphabet so to be passed into our first 
# function, then returning the outcome of the cipher.


# import string
# alpha = string.ascii_lowercase
# def user(x,y):
#     if x not in string.ascii_lowercase:
#         return x
#     new_letter = ord(x) + y
#     while new_letter > ord('z'):
#         new_letter -= 26
#     while new_letter < ord('a'):
#         new_letter += 26
#     return chr(new_letter)
# def caesar(msg, y):
#     func = [user(x,y) for x in msg]
#     return ''.join(func)
# print(caesar(alpha, 1))



# #4
# in this example we leverage a for loop method to return each letter of the alphabet
# by creating a range from the letters, then transformed numerically, a to z.


# def alph():
#     for letter in range(ord('a'), ord('z')+1):
#         print(chr(letter))
# alph()



# #5
# in this block of code we create a filter for what and what not to return
# this is minor example or usecase of the divide and conquer technique.


# from string import ascii_lowercase

# new_var = 'the quick brown fox jumped over the lazy dog'
# def user(letter):
#     var_one = 'aeiou'
#     return letter.isalpha() and letter.lower() not in var_one
# constants = [i for i in new_var if user(i)]
# print(constants)



# #6

# we import a couple libraries here to create a function that iterates through
# our operating systems directory in order to return certain files we are
# searching for. looking in our directory for any file the has '.' which assures
# us that it will look through all files because each file ends with (.js, .py, .css, and so on)
# from there we simply specify that we want all files ending with py.
#
# in the second example we leverage fnmatchcase once more in order
# to find what matches the parameters passed for the arguments.

# import os
# import fnmatch as fn
# from fnmatch import fnmatch
# def get_files():
#     for file in os.listdir('.'):
#         if fn.fnmatch(file, '*.py'):
#             print('we found:', file)
# get_files()

# import fnmatch as fn
# from fnmatch import fnmatch

# astros = [
#   'Gennett 2b',
#   'Bregman 3b',
#   'Altuve 2b',
#   'Correa ss',
# ]
# new_one = [player for player in astros if fn.fnmatchcase(player, '*2b')]
# print(new_one)



# #7
# here we import reduce once again to create a function which returns
# the mean of the array passed.
#
# the second example finds the median

# from functools import reduce
# content = [23,45,57,79,60]
# def user(num):
#     print(float(reduce((lambda x,y: x + y), num)/ len(num)))
# user(content)


# def user(x):
#     print(sorted(x).pop(len(x)//2))
# user([23,45,57,79,60,5])



# #8
# here we attain the api for a website and scrap the data returned,
# narrowing down our search by small increments at a time until we are able to 
# get the result of posts we are searching for. 

# from bs4 import BeautifulSoup
# from inflection import titleize
# import requests as re
# import inflection as fle

# r = re.get('http://www.dailysmarty.com/topics/python')
# soup = BeautifulSoup(r.text, 'html.parser')
# soup_links = soup.find_all('a')

# def soup_title(soup_links):
#     titles = []
#     def soup_posts(post):
#         if 'posts' in post:
#             post = post[7:]
#             post = fle.titleize(post)
#             titles.append(post)
#     for link in soup_links:
#         if link.get('href') == None:
#             continue
#         else:
#             soup_posts(link.get('href'))
#     return titles
# titles = soup_title(soup_links)
# for title in titles:
#     print(title)



# #9
# for our code below we implement the class object as well as property and setter
# decorators

# class ExampleClass:
#     def __init__(self, client, total):
#         self._client = client
#         self._total = total
#     def user(self):
#         return f"{self._client} has paid off their total of {self._total}"
#     @property
#     def client(self):
#         return self._client
#     @property
#     def total(self):
#         return self._total
#     @total.setter
#     def total(self, total):
#         self._total = total
# instant = ExampleClass('Nike', '$5,000')
# nike = instant.user()
# print(nike)



# #10
# for this example, we are implementing class objects once again, however,
# here we take advantage of the iterator protocol, meaning, we loop with 
# the dunder iter and next methods to control the iteration of an iterable. 
# much like a for loop, except, instead of looping through none stop like a loop
# the iterator methods lets us control the pace at which the values are returned.
# in this case im iterating over a list of players in a roster and once our iteration
# reaches the end of the list, it returns back to the 0 index, or the first name.

# class LineUp:
#     def __init__(self, players):
#         self.players = players
#         self.last_idx = (len(self.players) - 1)
#     def __iter__(self):
#         self.n = 0
#         return self
#     def get_player(self, n):
#         return self.players[n]
#     def __next__(self):
#         if self.n < self.last_idx:
#             player = self.get_player(self.n)
#             self.n += 1
#             return player
#         elif self.n == self.last_idx:
#             player = self.get_player(self.n)
#             self.n = 0
#             return player
# astros = [
#   'Springer',
#   'Bregman',
#   'Altuve',
#   'Correa',
#   'Reddick',
#   'Gonzalez',
#   'McCann',
#   'Davis',
#   'Tucker'
# ]
# astro = LineUp(astros)
# process = iter(astro)
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))



