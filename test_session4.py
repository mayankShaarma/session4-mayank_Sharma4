import pytest
import random
import os
import inspect
import re
import decimal
import session4
import math
from decimal import Decimal
from session4 import Qualean

README_CONTENT_CHECK_FOR = [
	'__and__',
	'__or__',
	'__repr__',
	'__str__',
	'__add__',
	'__eq__',
	'__float__',
	'__ge__',
	'__gt__',
	'__invertsign__',
	'__le__',
	'__lt__',
	'__mul__',
	'__sqrt__',
	'__bool__'
]


# test 1
def test_readme_exists():
	assert os.path.isfile("README.md"), "README.md file missing!"

#test 2
def test_readme_contents():
	readme = open("README.md", "r")
	readme_words = readme.read().split()
	readme.close()
	assert len(readme_words) >=500, "Make your README.md file interesting! Add atleast 500 words"

#test 3
def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r")
	content = f.read()
	f.close()
	for c in README_CONTENT_CHECK_FOR:
		if c not in content:
			READMELOOKSGOOD = False
			pass
	assert READMELOOKSGOOD ==True, "You have not described all the function/class wel in your README file"

#test 4
def test_readme_file_formatting():
	f = open("README.md", "r")
	content = f.read()
	f.close()
	assert content.count("#") >= 10

#test 5
def test_indentation():
	''' Return pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(session4)
	spaces = re.findall('\n +.',lines)
	for space in spaces:
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentations does not follow PEP8 guidelines"

#test 6
def test_function_name_had_cap_letter():
	functions = inspect.getmembers(session4, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#test 7
# def test_things_not_allowed():
# 	code_lines = inspect.getsource(session4)
# 	for word in CHECK_FOR_THINGS_NOT_ALLOWED:
# 		assert word not in code_lines, 'Have you heard of Pinocchio?'

#test 8
def test_mul():
	q = Qualean(random.choice([-1,0,1]))
	sum = q
	for i in range(99):
		sum = q.__add__(sum)
	assert sum==q.__mul__(100), 'Precision has been lost'

#test 9
# def test_sqrt():
# 	myinput = [-1,0,1]
# 	q = Qualean(random.choice(myinput))
# 	assert q.__sqrt__() == Decimal(str(q.number)).sqrt(), 'square root and Decimal of q sqrt not equal!.'
def test_sqrt():
	myinput = [-1,0,1]
	q1 = Qualean(random.choice(myinput))
	if(q1<0):
		assert isinstance(q1.__sqrt__(),complex), 'Sqrt should return complext value!!'
	else:
		assert q1.__sqrt__() == Decimal(q1.number).sqrt(), "Squre root deoesnt matches with Decimial.sqrt"

# def test_check_sqrt():
# 	choice = random.choice([1,0,-1])
# 	q = Qualean(choice)
# 	value = q.get_number()
# 	if value>=0:
# 		assert q.__sqrt__() == Decimal.sqrt(value), 'Squareroot [x]'
# 	else:
# 		assert q.__sqrt__() == 'i'+str(Decimal.sqrt(-value)), 'Squareroot [x]'


#test 10
def test_million_qsum():
	mylist = [-1, 0, 1]
	q = 1
	myinput = random.choice(mylist)
	for i in range(1000000):
		q = Qualean(myinput) * q
	assert math.isclose(i, 0, rel_tol=300), 'q is not appraching to 0'

#test 11
def test_bankers_rounding():
	q1 = Qualean(random.choice([-1,0,1]))
	assert len(str(q1).split(".")[-1]) == 10, 'your calculation will go wrong and run into losses.!'

#test 12
def test_or_notDefine_variable():
	mylist = [-1,0,1]
	myinput = random.choice(mylist)
	q1 = Qualean(myinput)
	q2 = None
	assert q1.__or__(q2) == True, '__or__ function is not short circuiting.!'

#test 13
def test_and_notDefine_variable():
	mylist = [-1,0,1]
	myinput = random.choice(mylist)
	q1 = Qualean(myinput)
	q2 = None
	assert q1.__and__(q2) == False, '__and__ function is not short circuiting.!'

#test 14
def test_and():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.number!=0 and q2.number!=0:
		assert q1.__and__(q2)==True, 'And True case is not working properly.!'
	else:
		assert q1.__and__(q2)==False, 'And False case is not working properly.!'

#test 15
def test_or():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.number!=0 or q2.number!=0:
		assert q1.__or__(q2)==True, 'Or True case is not working properly.!'
	else:
		assert q1.__or__(q2)==True, 'Or False case is not working properly.!'

#test 16
def test_repr():
	q = Qualean(random.choice([-1,0,1]))
	assert 'object at' not in q.__repr__()

#test 17
def test_str():
	q = Qualean(random.choice([-1,0,1]))
	assert(str(q)), 'String function is not working'

#test 18
def test_add():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	assert(math.isclose(q1+q2, q1.number+q2.number)), 'Your add function is not working properly.!'

#test 19
def test_eq():
	q1 = Qualean(random.choice([-1,0,1]))
	q2=q1
	assert(q2==q1), 'Equal to function not working properly.!'

#test 20
def test_float():
	q1 = Qualean(random.choice([-1,0,1]))
	assert isinstance(float(q1), float), ' Float conversion not working properly  '

#test 21
def test_ge():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.number>= q2.number:
		assert q1.__ge__(q2)==True, "__ge__ True case not working"
	else:
		assert q1.__ge__(q2)==False, "__ge__ False case not working"

#test 22
def test_gt():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	assert(q2.number > abs(q1.number)), ' Greater than function not working properly.!'

#test 23
def test_le():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.number <= q2.number:
		assert q1.__le__(q2)==True, '__le__ True case not working'
	else:
		assert q1.__le__(q2)==False, '__le__ False case not working'

#test 24
def test_lt():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	assert(q2 < abs(q1.number)), 'Less than  function  not working properly '

#test 25
def test_invertSign():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = q1.__invertsign__()
	assert(q2 == -(q1.number)), ' Invertion function  not working properly'

#test 26
def test_bool():
	q = Qualean(random.choice([-1,0,1]))
	assert(bool(q)), 'Bool function not working properly'