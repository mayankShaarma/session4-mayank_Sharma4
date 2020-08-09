import pytest
import random
import session4
import os
import inspect
import re
import decimal
from decimal import Decimal

README_CONTENT_CHECK_FOR = [
	'',
	'',
	'',
	'',
	'',
	''
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
	'',
	'',
	'',
	''
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
def test_things_not_allowed():
	code_lines = inspect.getsource(session4)
	for word in CHECK_FOR_THINGS_NOT_ALLOWED:
		assert word not in code_lines, 'Have you heard of Pinocchio?'

#test 8
def test_addition_equality():
	#q + q + q ... 100 times = 100 * q
	for i in range(100):
		q = +q
		count++
		if count == 100 :
			assert session4.multiple_timesQ_equality(q) == 100*q, 'both same'

#test 9
def test_sqrt_equality():
	#q.__sqrt__() = Decimal(q).sqrt
	assert q.__sqrt__() == Decimal(q).sqrt, 'square root and Decimal of q sqrt not equal!.'

#test 10
def test_million_qs():
	#sum of 1 million different Q's is very close to zero (use isclose)
	q = Qualean()
	mylist = [-1, 0, 1]
	myinput = random.choice(mylist)
	assert q.differentQs(myinput), "sum of 1 million different Q's is not very close"

#test 11
def test_define_variable():
	#q1 and q2 returns False when q2 is not defined as well and q1 is False
	#q1 or q2 returns True when q2 is not defined as well and q1 is not false
	assert session4.return_function1(q1,q2) == False, " q1 and q2 return False, as q2 not defined as well q1 is False"
	assert session4.return_function2(q1,q2) == True, "q1 or q2 returns True when q2 is not defined as well and q1 is not false"

#test 12
def test_qualean_class():
	assert session4.random_number(q1, q2)

#test 13
def 

if __