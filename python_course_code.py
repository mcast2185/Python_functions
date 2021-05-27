# """
# here we are creating a dict view from our class. since our
# self automatically takes on the value assigned once we 
# instantiated. with the value of its argument set as title
# that takes on the key position and the argument passed takes on
# the value. dict is a function call we can use even if not used
# in class. 
# calling user alone only returns an object mapping path
# """

# class Object_view:
#     def __init__(self, Title):
#         self.Title = Title
# key_value = Object_view('Ruins')
# key_value_obj = Object_view('Do Androids Dream of Electric Sheep')
# print(key_value.__dict__)
# print(key_value_obj.__dict__)


# """
# in this short example, we examine what a class attribute can do
# and what its limitations are. class attribute does not need a
# constructor like __init__ to be called. however, it is limited 
# to its hard coded value. value belongs only to that class, unless
# its parent class is inherited.
# """

# class Attribute:
#     title = f"Where the Red Fern Grows"
# user = Attribute()
# print(user.title)


# """
# here, we explore the concept of inheritance 'AdminUser(User):',
# this allows our separate class to take on the methods and attributes
# nested within the class inherited. It doesnt have access to the instantiated 
# values but can take the place of the init arguments with its own
# the User class is still limited to the values it contains.
# """


# class User:
#     title = f"finance"
#     def __init__(self, name, number):
#         self.num = number
#         self.name = name
        
#     def email_letter(self):
#         return f"{self.name} has ignored their {self.num} invoice, and as of 05/24/21, has two delinquency payment."

# class AdminUser(User):
#     def access(self):
#         return f"Pardon me sir, an email from {self.title} just came in: \n'{self.email_letter()}'\n How should we proceed?"
        
              
# User_access = User('Sebaan', '$22,500')
# Admin_access = AdminUser('Tricel inc', '$22,500')
# print(Admin_access.access())
# print(User_access.email_letter())


# """
# Here we are workinig with abstract classes. the purpose for 
# these classes is to hold and store shared behavior, only the 
# inherited classes/child classes will be the ones to ever call this class.
# initially, this was our print **print(str(tag) + ': ' + tag.render())** 
# using the string and concatenating it as debugging content, returning:
# **<__main__.Div object at 0x104228280>: <div>Python- Intro to Classes</div>**
# we can tell its running correctly as no references to the Html parent class
# show up. the 'raise' value in the parent class lets others know 
# that we never want this class called only used as an inherit class.
# (Polymorphism) when  we have a child class that inherits these methods from 
# parent classes, then overrides the behavior.
# So here communicating with API's(app, programming, interface)
# what were doing is polymorphism. meaning were creating multiple changes with 
# the inherit code, to many or just one item that takes many forms.
# self.content is the inherit code manipulated to our use.
# """


# class Html:
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         raise NotImplementedError('Subclass must implement render method')
# class Heading(Html):
#     def render(self):
#         return f"<h1>{self.content}</h1>"
# class Div(Html):
#     def render(self):
#         return f"<Div>{self.content}</Div>"
# tags = [
#     Div('Python: Intro to Polymorphism'),
#     Heading('Welcome to Advanced Programming'),
#     Div('JavaScript: Queries/ Media Queries')
# ]
# for tag in tags:
#     print(tag.render())


# """
# the first example: 
# below is just to show that the code still works
# without the parent class as an inheritance. the parent class served 
# more as a gatekeeper to the stored behavior.
# the next example:
# it shows us something similar except passed by a function,
# where in the moment of print or return, is when we apply the render()
# method to the variables
# use the function when dealing with a minor bit of code you need to 
# similarily alter, if lots of code, use inherit classes
# """

# class Heading:
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         return f"<h1>{self.content}</h1>"
# class Div:
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         return f"<Div>{self.content}</Div>"
# tags = [
#     Div('Python: Intro to Polymorphism'),
#     Heading('Welcome to Advanced Programming'),
#     Div('JavaScript: Queries/ Media Queries')
# ]
# for tag in tags:
#     print(tag.render())




# class Heading:
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         return f"<h1>{self.content}</h1>"
# class Div:
#     def __init__(self, content):
#         self.content = content
#     def render(self):
#         return f"<Div>{self.content}</Div>"

# head = Heading('Welcome to Advanced Programming')
# div_one = Div('Python: Intro to Polymorphism')
# div_two = Div('JavaScript: Queries/ Media Queries')     
# def html_render(tag_object):
#     print(tag_object.render())
# html_render(div_one)
# html_render(div_two)
# html_render(head)

# """
# here we are creating and writing to a file in python.
# open() is a function in python that allows us to open
# or create files by passing in a file name, if the file is 
# not found then it will create it. arg1 is name and type of 
# file. arg2 is the way we want to open.
# when creating, opening a file, we want to wrap the behavior
# created with a .close() that takes no args.
# if the file had previous txt or data, it overrides it
# """

# file_builder = open("logger.txt", "w+")

# for i in range(100):
#     file_builder.write(f"im on line {i + 1}\n")

# file_builder.close()

# """
# we started by using zsh shell the (touch), and made a few files at once
# imported the libraries below, fnmatch allows us to pass in regular
# expressions, (*,^,$) three for example. (*.txt) means is that if any of the 
# text in the directory we are going through, includes .txt, 'True', show me
# (*) means display for zero or more occurences.
# in the list comprehension, we used (fnmatchcase) for the first time, what it does
# does is catch any pattern, re occurence of the arguments or filenames passed.
# we combined the os(operating system) library and the fnmatch library to filter through
# our list of files
# (this is a common tool we'll be using so implement as much as possible)
# works to filter down a list too.
# """

# import fnmatch as fn
# from fnmatch import fnmatchcase
# import os

# def list_files():
#     for file in os.listdir('.'):
#         if fn.fnmatch(file, "*.txt"):
#             print('Text files: ', file)
#         if fn.fnmatch(file, "*.rb"):
#             print('Ruby files: ', file)
#         if fn.fnmatch(file, "*.yml"):
#             print('Yaml files: ', file)
#         if fn.fnmatch(file, "*.html"):
#             print('Html files: ', file)
# list_files()

# astros = [
#   'Gennett 2b',
#   'Bregman 3b',
#   'Altuve 2b',
#   'Correa ss',
# ]

# second_base = [player for player in astros if fnmatchcase(player, '* 2b')]
# print(second_base)