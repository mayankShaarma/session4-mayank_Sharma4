import math
import decimal
from decimal import Decimal
import random

class Qualean(object):
	def __init__(self, value):
		if(value in [1,0,-1]):
			self.num = value
			rand = random.uniform(-1, 1)
			self.number = round((rand * self.num), 10)
		else:
			raise AttributeError('Invalid input')

	def get_number(self):
		return self.number

	def __and__(self,other_object):
		if not bool(self.number):
			return False
		else:
			if isinstance(other_object,Qualean) and other_object.number:
				return bool(self.number and other_object.number)
			else:
				return False

	def __or__(self,other_object):
		if self.number:
			return True
		else:
			if isinstance(other_object,Qualean) and other_object.number:
				return bool(self.number or other_object.number)
			else:
				return False

	def __repr__(self):
		return 'Qualean {0}'.format(self.number)

	def __str__(self):
		return 'Qualean: internal number ={0}'.format(self.number)

	def __add__(self, num):
		if(isinstance(num, Qualean)):
			return self.number+num.number
		return self.number+Decimal(str(num))

	def __mul__(self, num):
		if isinstance(num, Qualean):
			return self.number * num.num
		return self.number * Decimal(num)

	def __eq__(self, num):
		if isinstance(num, Qualean):
			return self.number == num.number
		return False

	def __float__(self):
		return float(self.number)

	def __ge__(self, num):
		if(isinstance(num, Qualean)):
			return self.number >= num.number
		return self.number >= Decimal(str(num))

	def __gt__(self, num):
		if(isinstance(num, Qualean)):
			return self.number > num.number
		return self.number>Decimal(str(num))

	def __le__(self, num):
		if(isinstance(num, Qualean)):
			return self.number <= num.number
		return self.number<=Decimal(str(num))

	def __lt__(self, num):
		if(isinstance(num, Qualean)):
			return self.number < num.number
		return self.number<Decimal(str(num))

	def __invertsign__(self):
		return self.number*Decimal('-1')

	def __bool__(self):
		return bool(self.number)

	def __sqrt__(self):
		if self.number < 0:
			x = self.number * -1
			return 1j * float(x.sqrt())
		else:
			return self.number.sqrt()

	# def differentQs(q):
	# 	return

	# def return_function1(q1, q2):
	# 	return

	# def return_function2(q1, q2):
	# 	return

	# def random_number(q1, q2):
	# 	return

	# def multiple_timesQ_equality(q):
	# 	return