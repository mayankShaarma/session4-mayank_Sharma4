import pytest
import session4
import inspect
import re

from session4 import Qualean
import copy
import random
import os
import math

CHECK_FOR_FUNCTIONS = [
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

#test 1
def test_function_name_had_cap_letter():
	functions = inspect.getmembers(session4, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_indentations():
	''' Returns pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(session4)
	spaces = re.findall('\n +.', lines)
	for space in spaces:
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_and_when_q2_not_defined():
	q1=Qualean(0)
	q2=None
	assert q1 & q2 == False, "__and__ function is not short circuiting"

def test_and_functionality():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()!=0 and q2.get_number()!=0:
		assert q1 & q2==True, "and True case is not working as expected"
	else:
		assert q1 & q2==False, "and False case is not working as expected"

def test_or_when_q2_not_defined():
	q1=Qualean(1)
	q2=None
	assert q1|q2 == True, "__or__ function is not short circuiting"

def test_or_functionality():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()!=0 or q2.get_number()!=0:
		assert q1|q2==True, "or True case is not working as expected"
	else:
		assert q1|q2==False, "or False case is not working as expected"

def test_repr():
	q = Qualean(0)
	assert 'object at' not in q.__repr__()

def test_str():
	q = Qualean(0)
	internal_value = q.get_number()
	assert q.__str__() == f'Qualean: internal number ={internal_value}', 'The print does not meet expectations'

def test_add_mul():
	q = Qualean(-1)
	total = q
	for x in range(99):
		total = q+total
	assert total==q*100, "Precision has been lost"

def test_ge():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()>= q2.get_number():
		# print(q1.get_number())
		# print(q2.get_number())
		# print(True)
		assert (q1>=q2)==True, "__ge__ True case not working"
	else:
		# print(q1.get_number())
		# print(q2.get_number())
		# print(False)
		assert (q1>=q2)==False, "__ge__ False case not working"

def test_gt():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()> q2.get_number():
		assert (q1>q2)==True, "__gt__ True case not working"
	else:
		assert (q1>q2)==False, "__gt__ False case not working"

def test_le():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()<= q2.get_number():
		assert (q1<=q2)==True, "__le__ True case not working"
	else:
		assert (q1<=q2)==False, "__le__ False case not working"

def test_lt():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()< q2.get_number():
		assert (q1<q2)==True, "__lt__ True case not working"
	else:
		assert (q1<q2)==False, "__lt__ False case not working"

def test_all_functions_exist():
	code_lines = inspect.getsource(session4)
	for word in CHECK_FOR_FUNCTIONS:
		assert word in code_lines, 'Have you heard of Pinocchio?'

def test_readme_exists():
	assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
	readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
	assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	assert content.count("#") >= 10

def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	for c in CHECK_FOR_FUNCTIONS:
		if c not in content:
			READMELOOKSGOOD = False
			pass
	assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_invalid_input_valueerror():
	with pytest.raises(ValueError):
		Qualean(9)

def test_float():
	assert isinstance(float(Qualean(random.choice([-1,0,1]))), float), "float function not working"

def test_bool():
	assert isinstance(bool(Qualean(random.choice([-1,0,1]))), bool), "bool function not working"

def test_invertsign():
	q1 = Qualean(random.choice([-1,0,1]))
	if q1.get_number()<0:
		assert (q1.__invertsign__()>0)==True, "invertsign not working"
	elif q1.get_number()>0:
		assert (q1.__invertsign__()<0)==True, "invertsign not working"
	else:
		assert (q1.__invertsign__()==0)==True, "invertsign not working"

def test_one_million_sum():
	q = Qualean(random.choice([-1,0,1]))
	total = q
	for x in range(1000000 - 1):
		total = q+total
	assert math.isclose(total,0), "Something is wrong"

def test_eq():
	q1 = Qualean(random.choice([-1,0,1]))
	q2 = q1
	assert(q2==q1), "qual to function not working properly.!"