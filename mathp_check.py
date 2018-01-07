import mathp_eval as mp
import random

operators = ['*','/', '-', '+']
def genString():
	string = str(random.randint(1,10))
	size = random.randint(1,10)
	for i in range(size):
		string += random.choice(operators)
		string += str(random.randint(1,1000))
	try:
		value = eval(string)
		if value != mp.mathpeval(string):
			print("ERROR: " + string)
	except ZeroDivisionError:
		pass

for i in range(100):
	genString()
