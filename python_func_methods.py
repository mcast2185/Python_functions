# """
# every day we do these over. every day add to the notes. 
# how is it applicable? what is the function thats occuring? 
# what kind of real time situation needs this?
# start learning an algorithm a week.
# """


# """
# #1 
# scrapping a website without access to its api. 
# creating variables that each narrow the code down to links. then using functions
# """
# import requests as re
# import inflection as fle
# from bs4 import BeautifulSoup
# from inflection import titleize

# r = re.get('http://www.dailysmarty.com/topics/python')
# soup = BeautifulSoup(r.text, 'html.parser')
# soup_links = soup.find_all('a')

# def soup_title(soup_links):
#     titles = []
#     def soup_posts(posts):
#         if 'posts' in posts:
#             posts = posts[7:]
#             posts = fle.titleize(posts)
#             titles.append(posts)
#     for link in soup_links:
#         if link.get('href') == None:
#             continue
#         else:
#             soup_posts(link.get('href'))
#     return titles
# titles = soup_title(soup_links)
# for title in titles:
#     print(title)


# """
# #2 
# Here the @setter value simply implies that the value 
# can be changed, @property allows only get not set.
# be sure to understand that self is essentially each independent 
# argument. with self being able to apply any methods within the 
# class to the argument being attached. so imagine whatever you set 
# an argument to plus whatever you defined it
# as. with self the below arguments get called 
# during the instantiation with (name = Invoice('hey', 'you'))-
# self represents both, if called the arguments passed 
# will be initialized by init()
# """

# class Payment:
#     def __init__(self, client, total):
#         self._client = client
#         self._total = total
#     def user(self):
#         return f"For the month of May, {self._client} will be billed {self._total}, through the dates 04/01/21 - 05/30/21."
#     @property
#     def client(self):
#         return self._client
#     @client.setter
#     def client(self, client):
#         self._client = client
#     @property
#     def total(self):
#         return self._total
# company_bill = Payment('Company.inc', '$19,000')
# statement = company_bill.user()
# print(statement)


# """
# #3 
# here we practice the init function. it allows us 
# to add values during instantiation. using self as the 
# instance to any method or atribute within the class
# """

# class Invoice:
#     def __init__(self, email, first_last):
#         self.email = email
#         self.first_last = first_last
#     def user(self):
#         return f"For quality assurance, is '{self.first_last}' your name? and is {self.email} the correct email address?"

# name = Invoice('python@gmail.com', 'Frank Grayson')
# print(name.user())


# """
# #4 
# __str__() method returns string from our object, so 
# to be used and accessed as a string and not as data
# from a class object.
# we do not need to call user.__str__() like other methods
# as it is value is used and called on by 'self', permitting
# us its return value. however if we want to use it to 
# return a string, str(user) will allow us to do so. 
# """

# class String:
#     def __init__(self, client):
#         self.client = client
#     def __str__(self):
#         return f"Hello {self.client}, here is your Invoice for the month of May."
# user = String('Charles Ragnow')
# print(str(user))
        


# """ 
# #5 
# example of a factorial function. it multiplies down 
# its decending order. (4*3*2*1)
# the return at the bottom has to include the function
# as its multipying the numbers in the process of the 
# function not just the number. for else it would read
# 4 * (4 - 1) which would equal 12 and thats it.
# we also use an example of a (try) catch a bug catcher.

# """

# def user(n):
#     try:
#         if n == 0:
#             return 1
#         else:
#             return n * user(n-1)
#     except TypeError:
#         return None
# print(user(4))


# """
# #6 
# here we are creating a matrix. here you have 
# to visualize the form its taking. 
# the idx represents the index number of lists 
# nested in the matrix. the nested idx represents 
# the indexes of the elements nested inside. if 
# the range is five, the nested indexes go 0 - 4, 
# since 0 is counted as an index 
# the el represents the elements inside those lists.
# next we take the matrix and grab its index,
# then the nested index of that: list, item in list.
# and we make each of them equal to the counter, 
# which is 0, and add to it its index number
# and for each time it creates a new list, which it does
# in the first loop, we add a counter incremented by one
# and finally, we return the value of the matrix.

# """

# from typing import Counter

# def matrix_func(n):
#     matrix = [[None for x in range(n)]for y in range(n)]
#     Counter = 0
#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix[idx][nested_idx] = Counter + nested_idx
#         Counter += 1
#     return matrix
# print(matrix_func(5))


# """
# #7 
# we created a histogram here. grabbing each key and 
# value by using the function call of .items(), 
# re-assigning the output value to be a string symbol thats
# being concatenated with another string value and the key value
# """

# sales = {
#     'Google': 24,
#     'Facebook': 22,
#     'Twitter': 16,
#     'Offline': 10
# }
# for key, value in sales.items():
#     print(key + ': ' + value * '$')


# """
# #8 
# two different examples of an iteration that applies a
# string value for every condition applied, one with range 
# the other with enumerate. remember that if our conditions 
# value crosses over with an other, we wont get the results
# we intend unless we place the overlapping condition at
# the top.
# when using the enumerate(), two variables must be applied,
# enumerate always counts with an index
# """

# def fizzbuzz(num):
#     for y, x in enumerate(num):
#         if y % 5 == 0 and y % 3 == 0:
#             print('FizzBuzz')
#         elif y % 3 == 0:
#             print('Fizz')
#         elif y % 5 == 0:
#             print('Buzz')
#         else:
#             print(x)
# fizzbuzz(range(101))

# def fizzbuzz(num):
#     for x in range(num):
#         if x % 5 == 0 and x % 3 == 0:
#             print('FizzBuzz')
#         elif x % 3 == 0:
#             print('Fizz')
#         elif x % 5 == 0:
#             print('Buzz')
#         else:
#             print(x)
# fizzbuzz(101)


# """
# #9 
# here we are creating a dynamic function using reduce to iterate.
# the reduce function takes its first function argument and applies
# to the iterable that follows, until its reduced to a single value 
# The nested operator gets sent between x and y in our list
# """


# from functools import reduce
# import operator

# def dynamic_reducer(list, op):
#     operators = {
#         '+': operator.add,
#         '*': operator.mul
#     }
#     return reduce((lambda a, b: operators[op](a,b)), list)
# print(dynamic_reducer([1,2,3,4,5,6,7,8], '+'))
# print(dynamic_reducer([1,2,3,4,5,6,7,8], '*'))


# """
# #10 
# still have to practice this code, and understand.
# """

# import numpy as np

# def lottery(weights):
#     name = []
#     for key, weight in weights.items():
#         for _ in range(weight):
#             name.append(key)
#     return np.random.choice(name) 
# weights = {
#     'win': 1,
#     'lose': 8,
#     'even': 2
# }
# print(lottery(weights))


# """ 
# #11
# 1: wants a module that iterates through a list
# 2: wants a function that gets to the end and starts over
# 3: wants ability to control the iteration, not looping automatically
# 4: what we know-
# we know that the iter() function iterates through a given iterable/ our list
# we know that the next() function works alongside the iter() returning the following
# we know we'll have to set our variables: length of list, players in list
# we know we'll have to have a function that returns players by their index
# 5: break that down-
# -if we break down each task into functions, and detail their tasks
# the process of next() should be the only set of conditionals.
# -when we iterate we are concerned with the index not the name set the idx at 0
# -grabbing players should be their index
# -we have to return the player processed with the index raised, thats 
# what hands us the next name
# """

# class Lineup:
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
# astros_lineup = Lineup(astros)
# process = iter(astros_lineup)
# print(next(process))


# """
# #12
# this our python generator of our lineup. yield prevents 
# the loop from iterating over automatically unless
# called again, giving us the ability to use the next() 
# without having defined the method of when, and how to proceed
# """

# class InfiniteLineup:
#     def __init__(self, players):
#         self.players = players
#     def lineup(self):
#         max_lineup = len(self.players)
#         idx = 0
#         while True:
#             if idx < max_lineup:
#                 yield self.players[idx]
#             else:
#                 idx = 0
#                 yield self.players[idx]
#             idx += 1
#     def __str__(self):
#         return f"For todays game we have the Astros lineup of {self.players}"
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
# astros_ = InfiniteLineup(astros)
# astro_intro = str(astros_)
# astros_lineup = astros_.lineup()
# print(astro_intro)
# print(next(astros_lineup))


# """
# #13
# -we create the caesar() function thats going to give us
# the return we want. setting variable equal to a compound 
# conditional that takes us to the user() function.
# -here we set x = the ord() of a/ 97 + 1, which is b/98
# -98 is not > than ord() of z/122 
# -98 is greater than ord() a/97, so we dont add either, so
# we continue through the alpha
# - when we get to ord() z/122 + 1, the first while loop
# finally takes place
# -since 123 is higher than ord() z, we subtract 26 which gives us 97/a
# -this creates the loop of always resetting after it iterates over
# """

# import string

# x = string.ascii_lowercase
# def user(x, y):
#     if x not in string.ascii_lowercase:
#         return x
#     new_letter = ord(x) + y
#     while new_letter > ord("z"):
#         new_letter -= 26
#     while new_letter < ord("a"):
#         new_letter += 26
#     return chr(new_letter)
# def caesar(message, y):
#     enc_list = [user(x, y) for x in message]
#     return "".join(enc_list) 
# print(caesar(x, 1))


# """
# #14
# Here we are workinig with abstract classes. Their purpose:
# hold/ store shared behavior, only inherited classes/child classes call this class.
# the 'raise' value in parent class error warning if used directly 
# (Polymorphism): when a child class inherits methods from parent classes, 
# then overrides the behavior.
# while communicating with API (app, programming, interface) whether one line   
# or one item, were making polymorphic changes. Altering the inherit code,
# self.content is the inherit code manipulated to our use.
# """

# class Html:
#     page_title = f"The Restive"
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         raise NotImplementedError('Must use Sub-class with render method')
# class Div(Html):
#     def render(self):
#         return f"<div>{self.content}</div>"
# class Heading(Html):
#     def render(self):
#         return f"<h1>{self.content}</h1>"
# tags = [
#     Div(" Python: Intro to Polymorphism "),
#     Heading(" Today's topics: "),
#     Div(" JavaScript: Intro to Media Queries ")
# ]
# for tag in tags:
#     print(tag.render())
# Admin = Html('Permit if inherited.')
# print(Admin.__dict__)
# print(Admin.page_title)


# """
# #15
# rules:
# -build a function that takes in two numbers as arguments
# -the second argument replaces the decimal numbers.(3.20, 99) > 3.99
# -but also capable of (3.20, 0.99) > 3.99
# what we know:
# - we know a slice method/range method could work
# - we know we could use formatting here
# - we know '.' indicates when to stop. possiblly partition()/ split()?.
# - we know that we are not using operators or traditional math
# - we know format(#, '.2f') limits decimal point to 2
# *(1st solution mine, 2nd solution his.)* 
# my solution takes up one more line of code, however it does 
# not return more than two decimal points, as his.
# """
# import math as m

# def gross_value(net, tax):
#     if tax > 1 and '.' not in str(tax):
#         return int(net) + float('.' + str(tax))
#     else:
#          return int(net) + tax
# print(gross_value(3.50, 57))

# def gross_value(net, tax):
#     if isinstance(tax, int):
#         tax = tax * 0.01
#     return int(net) + tax
# print(gross_value(3.50, 57))


# """
# In binary search we take a sorted list of elements and start looking for an element at the middle of the list. 
# If the search value matches with the middle value in the list we complete the search. Otherwise we eleminate half 
# of the list of elements by choosing whether to procees with the right or left half of the list depending on the 
# value of the item searched. This is possible as the list is sorted and it is much quicker than linear search. 
# Here we divide the given list and conquer by choosing the proper half of the list. We repeat this approcah till we 
# find the element or conclude about it's absence in the list.
# """

# def bsearch(list, val):

#     list_size = len(list) - 1

#     idx0 = 0
#     idxn = list_size
# """Find the middle most value"""

#     while idx0 <= idxn:
#         midval = (idx0 + idxn)// 2

#         if list[midval] == val:
#             return midval
# """Compare the value the middle most value"""
#         if val > list[midval]:
#             idx0 = midval + 1
#         else:
#             idxn = midval - 1

#     if idx0 > idxn:
#         return None
# """Initialize the sorted list"""
# list = [2,7,19,34,53,72]

# """Print the search result"""
# print(bsearch(list,72))
# print(bsearch(list,11))


