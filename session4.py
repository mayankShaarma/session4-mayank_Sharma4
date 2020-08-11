import math
import decimal
from decimal import Decimal
import random

import random
import decimal
from decimal import Decimal

with decimal.localcontext() as ctx:
	ctx.prec = 10
	class Qualean:
		def __init__(self, real):
			if(not(real==0 or real==1 or real==-1)):
				raise ValueError("Number can only be 0 or 1 or -1")
			rand = random.uniform(-1, 1)
			decimal_number = Decimal(str(real))
			self.number = Decimal(str(round((rand * real), 10)))

		def __and__(self, other):
			if(not bool(self.number)):
				return False
			if(isinstance(other, Qualean)):
				return bool(self.number*other.number)
			return False

		def __or__(self, other):
			if(bool(self.number)):
				return True
			if(isinstance(other, Qualean)):
				return bool(self.number+other.number)
			return False

		def __repr__(self):
			return 'Qualean({0})'.format(self.number)

		def __str__(self):
			return 'Qualean: internal number ={0}'.format(self.number)

		def __add__(self, other):
			if(isinstance(other, Qualean)):
				return self.number+other.number
			else:
				return self.number+Decimal(str(other))

		def __mul__(self, other):
			if(isinstance(other, Qualean)):
				return self.number*other.number
			else:
				return self.number*Decimal(str(other))

		def __eq__(self, other):
			if isinstance(other, Qualean):
				return self.number == other.number
			else:
				return False

		def get_number(self):
			return self.number

		def __float__(self):
			return float(self.number)

		def __ge__(self, other):
			if(isinstance(other, Qualean)):
				return self.number>=other.number
			else:
				return self.number>=Decimal(str(other))

		def __gt__(self, other):
			if(isinstance(other, Qualean)):
				return self.number>other.number
			else:
				return self.number>Decimal(str(other))

		def __le__(self, other):
			if(isinstance(other, Qualean)):
				return self.number<=other.number
			else:
				return self.number<=Decimal(str(other))

		def __lt__(self, other):
			if(isinstance(other, Qualean)):
				return self.number<other.number
			else:
				return self.number<Decimal(str(other))

		def __invertsign__(self):
			return self.number*Decimal('-1')

		def __bool__(self):
			return bool(self.number)

		def __sqrt__(self):
			return self.number.sqrt()