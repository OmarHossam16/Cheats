##################### PAGES ######################

CONCEPTS
SETS
FILES
FUNCTIONS
LISTS
STRINGS
NUMBERS
DICTS
OS
REGEX
RANDOM
DATE
MODULE
ITERTOOLS
CSV
DECORATORS
NAMETUPLES
JSON
Flask
##################### CONCEPTS ######################

CLOSURES : Remembering a Function

DRY : Not To Repeate Yourself
MEMOIZATION : cashing to save computing time
COMPINATIONS : Order does not Matter 
PERMUTATIONS : Order Matter
IDEMPOTENCE : When f(x) = f(f(x)) example: GET, PUT, DELETE
STRING CONCATENATION : 'Name is ' + name
STRING INTERPOLATION : f'Name is {name}'
MUTABLE : lists
IMMUTABLE : strings
1st ClASS FUNCTION
##################### CLASSES ######################

def __repr__(self,str1): # __add__ , __len__	,__str__
	return f'Arg : {self.arg}{str1}'
# repr --> unambigous | str --> readable
__repr__ = function

@property
def fullname(self):
	return f'{self.first} {self.last}'

@fullname.setter
def fullname(self,name):
	first,last = name.split(' ')	
	self.first = first
	self.last = last

@fullname.deleter # del emp1.fullname 
	def fullname(self,name):
	self.first , self.last = None , None
	print('Name Deleted')

	
##################### SETS ######################

set1 = {1,2}
set2 = {1,2,3}

set1.intersection(set2) # >> 1,2
set1.difference(set2) # >> 3
set1.union(set2) # >> 1,2,3

nums = [1,1,2]
set3 = {i for i in nums} # {1, 2}
##################### FILES ######################

file = open("file.txt","r") 
# r:read , w:write , a:append , r+ :r,w | (images) : rb , wb 	 
file.mode # >> r 	
file.readable() #>> True or False
file.read() #.read(100)
file.readline() 
file.seek(2) # begin with 3rd char
list = file.readlines()
file.write("append") # \n
file.close()

with open('file.txt','r') as r:
	with open('txt.txt','w') as w: #new_file
		read = r.read(4)
		while len(read):
			w.write(read)
			read = r.read(4)
##################### FUNCTIONS ######################

def student_info(*args,**kwargs):
	print(args) # returns tuple : >> ('Programming','DataStructures')
	print(kwargs) # returns dict : >> {'name':'Omar','age':19}

student1 = student_info('Programming','DataStructures',name='Omar',age=19)	
classes = ['Programming','DataStructures']
info = {'name':'Omar','age':19}
student 2 =student_info(*classes,**info)
# student1 == student 2

import random
random.choice(list1)
import math
rad = math.radians(90) # >>1.57
math.sin(rad) # >> 1.0
import calendar
calendar.isleap(year)
import secrets
secrets.token_hex(16)
import webbrowser

dir(var) # >> all methods and functions
help(var) # dir() but more discripted
type(var) # >> int , str , float ...

def html_tag(tag):
	def wrapper(text):
		print(f'<{tag}>{text}</{tag}>')
	return wrapper
h1 = html_tag('h1')
h1('Text')
##################### LISTS ######################

empty_list = []
empty_tuple = ()
empty_dict = {}
empty_set = set()

list1 = [1,2,3]
list2 = [4,5,6]

list3 = [list1,list2] # [[1,2,3],[4,5,6]]
list4 = zip(list1,list2) # [(1,4),(2,5),(3,6)]

list1 = [i for i in range(1,11)] # = [0,1,2,...9]
list1 = [i for i in range(1,11) if i%2==0]: # [2,4,6,8,10]
list1 = [(i,y) for i in list2 for y in range(1,11)] # [(i,y),...]

generator1 = (i**2 for i in range(1,11)) #(1,4,9,16,25,36,49,64,81,100)
list1 = list(generator1)

def sqr_generator(nums):
	for i in nums:
		yield i*i

nums = sqr_generator([1,2,3])
for i in nums:
	print(i)

item = list[row][item]
tuple1 = (items) #a list that can't be changed
item = list.pop() # popped = last item 
list1 = sorted(list) 	
list2 = list.copy()
str_list = ' '.join(list) # a b c d
list1 = str_list.split(' ') #returns list

len(list1)
list1.extend(list2)
list1.append(item)
list1.insert(index,item)
list1.remove(item)
list1.clear()
list1.pop() #removes last item from list
list1.pop(index)
list1.index(item)
list1.sort()
list1.sort(reverse=True)
list1.reverse()

nums = [-2,0,1]
list1 = sorted(nums,key=abs) # [0,1,-2]

def custom_sort(arg):
	return arg

list1 = sorted(nums,key=custom_sort)


print(list1)
for index,item in enumerate(list): 
# enumerate(list,start=1)
	print(index,item)
##################### STRINGS ######################

str1.count('word') # counts times word occures
str1.find('word') # >> -1 if not found
formated = f'{str1} word {str2}'
str1.replace(old,new)
replace(old_str,new_str)
input("str")
str1.strip() # removes last & first spaces
str1.zfill(2) # 1,10 -> 01,10
'-'.join('abc') # >> 'a-b-c'
##################### NUMBERS ######################

abs(num)
pow(num,3) #num^3
max,min(num1,num2)
round(num) # '~='
floor(num) # min num
sqrt(num)
range(num)
range(num1,num2)
round(9,2) # 9.00
2**3 # 2^3  
3 // 2 # >> 1
##################### DICTS ######################

dict1 = {'name':'Omar','age':19}
list1 = [1,2]
list2 = ['omar','hossam']

dict1.get('name') # >> Omar
dict1.get('address') # >> None
dict1.get('address','Not Found') # >> Not Found
dictionary['age']
dict1['address'] = 'Alexandria' # adds Address to dict1
dict1.update({'address':'Hossam'})
del dict1['name']
name = dict1.pop('name')# >> Omar , delets name form dict1

dict1.keys()
dict1.values()
dict1.items() # >> dict_items([('name', 'Omar'), ('Age', 19)])

for key,value in dict1.items():
	print(key,value)

dict1 = {key:value for key,value in zip(list1,list2)} # {1:'omar',2:'hossam'}
dict1 = {key:value for key,value in zip(list1,list2) if key <2} # {1: 'omar'}
##################### OS ######################

import os
os.getcwd()
os.chdir('/path')
os.rename('old.txt','new.txt')
os.mkdir('/path')
os.makeedirs('/path/folder')
os.rmdir('/path')
os.removedirs('/path/folder')
os.stat('file.anything')#os.stat().st_size

os.path.join(os.environ.get('path/'),'file.txt')
os.path.basename('/path/file.txt') # >> file.txt
os.path.dirname('/path/file.txt') # >> /path
os.path.split('/path/file.txt') # >> ('/path','file.txt') # >> ('file','.txt')

os.path.exists('/path/file.txt') # >> True , False
os.path.isdir('/path/file.txt') # >> True , False
os.path.isfile('/path/file.txt') # >> True , False
os.path.splitext('/path/file.txt') # >> ('/path/file','.txt')

walk = os.walk(os.getcwd())
for dirpath,dirname,filename in walk:
	print("DIRPATH : ",dirpath)
	print("DIRNAME : ",dirname)
	print("FILENAME : ",filename)
	print()
##################### REGEX ######################

import re
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [1-10]  - Matches nums in range(1,11)
# [a-z]   - Matches Characters from 'a' to 'z'
# [a-zA-Z]- Matches Characters from 'a' to 'z' (lower or upper)
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {2}     - Exact Number example: \d{2} = \d\d
# {3,4}   - Range of Numbers (Minimum, Maximum)
	
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+ --> email	
# https?://(www\.)?(\w+)(\.\w+) --> URL

pattern = re.compile(r'.') # (r'.',re.I) I = IGNORECASE 

first_word_match = pattern.match('word') # ONLY 1st word of a sentence
word_match = pattern.search('word')

url_match = pattern.sub(r'\2\3',urls) # \2\3 = group 1,2

matches = pattern.finditer(search_text)
matches = pattern.findall(search_text)

for match in matches:
	match.group(1) 
##################### RANDOM ######################

import random

random.random() #float
random.uniform(1,10) #float
random.randint(1,10)

list1 = ['black','white','blue']
random.choice(list1)
random.choices(list1,weights=[18,18,2],k=10)
# 10 random items from list1 chance:(black=18/38, white=18/38, blue=2/38)

random.shuffle(list1)
random.sample(list1,k=5) # >> list of 5 random items of list1

##################### DATE ######################

import datetime

date1 = datetime.date(1999,4,15)
date2 = datetime.time(9,30,45,10000)
date3 = datetime.datetime(1999,4,15,9,30,45,10000)

today1 = datetime.date.today() #.year |.month |.day
today2 = datetime.time.today() #.hour
today3 = datetime.datetime.today()

now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()


today.weekday() # Sun:6,Mon=0,Tue=1
today.isoweekday() # Sun:7,Mon=1,Tue=2

timedelta = datetime.timedelta(days=1) #.total_seconds() |.month |.days

date2 = date + timedelta #>> 1999-04-16
timedelta1 = date1 - date # date1 > date

import pytz # terminal/~ pip install pytz
##################### MODULE ######################

import module
import module as m
from module import function as f,var
from module import * # Not Good Practice

# adding module path if not in the same dir#
import sys
sys.path.append('/path/ModuleFoulder')
# OR 
terminal ~$ nano ~/.bash_profile
	# add this to the end of the file
	export PYTHONPATH="/path/ModuleFoulder"
##################### ITERTOOLS ######################

import itertools
list1 = [1,2,3]

combins = itertools.combinations(list1,3)
	# (1, 2, 3)
combins = itertools.combinations(list1,2)
	# (1, 2)
	# (1, 3)
	# (2, 3)

permuts = itertools.permutations(list1,3)
	# (1, 2, 3)
	# (1, 3, 2)
	# (2, 1, 3)
	# (2, 3, 1)
	# (3, 1, 2)
	# (3, 2, 1)
permuts = itertools.permutations(list1,2)
	# (1, 2)
	# (1, 3)
	# (2, 1)
	# (2, 3)
	# (3, 1)
	# (3, 2)

##################### CSV ######################

word = 'sample'
match = 'masple'
match = itertools.permutations(word,6)
for i in m:
	if ''.join(i) == match:
		print('MATCH')
import csv

with open('file.csv','r') as file:
	reader = csv.reader(file)

	for line in reader:
		print(line)
##################### DECORATORS ######################

def decorator_function(original):
	def wrapper(*args,**kwargs):
		print(original.__name__)
		return original(*args,**kwargs)
	return wrapper

# OR 

class class_decorator(object):
	def __init__(self, original):
		self.original = original

	def __call__(self,*args,**kwargs):
		print(f'call method executed before {self.original.__name__}()')
		return self.original(*args,**kwargs)


@decorator_function # OR @class_decorator
def display():
	print('Done')	
display()	
# >>display /n Done

@decorator_function # OR @class_decorator
def info(name,age):
	print(f'{name} {age} info()')
info('Omar',19)
# >> info /n Omar 19 info()
##################### NAMETUPLES ######################

from collections import namedtuple

Employee = namedtuple("Employee", ["id", "title", "salary"])
emp1 = Employee('12345', 'Engineer', 100000)
emp2 = Employee('54321', 'Manager', 120000)

emp1.id # >> A12345
emp2.title # >> Manager
##################### JSON  ######################

import json
from urllib.request import urlopen

with urlopen('url') as response:
    source = response.read()

data = json.loads(source)

json.dumps(data, indent=2)
##################### Flask ######################

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
hashed = bcrypt.generate_password_hash('str').decode('utf-8')
bcrypt.check_password_hash(hashed,'str') # >> True
