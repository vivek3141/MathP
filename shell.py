import math
import datetime
import sys
import os
import mathp_eval
run = True
try:
	fil = sys.argv[1]
except IndexError:
	run = False
if(run):
	os.system("python3 /home/vivek/MathP/run.py "+fil)
	exit()
d = str(datetime.datetime.today())
print("MathP v1.0.0 Beta 1 [" + d + "]")
print("viveklabs inc. Written in Python")
print("Type ex() to exit")
print("")
while(True):
	try:
		x = input(".>>")
	except EOFError:
		print("")
		exit()
	except KeyboardInterrupt:
		print("")
		print("MathP Error")
		print("KeyboardInterruptError: Keyboard Interrupt")
		continue
	except TypeError:
		print("")
		print("MathP Error")
		print("SpecialError: No Special characters\n")
	if(x == "ex()"):
		exit()
	try:
		print(mathp_eval.mathpeval(x))
	except SyntaxError:
		print("MathP Error")
		print("SyntaxError: Invalid Syntax\n")
	except ValueError:
		print("MathP Error")
		print("StringErrorValue: Use numbers only\n")
	except NameError:
		print("MathP Error")
		print("StringErrorName: Use numbers only\n")
	except EOFError:
		exit()
	except KeyboardInterrupt:
		print("KeyboardInterruptError: Keyboard Interrupt")
	except TypeError:
		print("")
		print("MathP Error")
		print("StringErrorType: Use numbers only\n")
	except ZeroDivisionError:
		print("")
		print("MathP Error")
		print("DivisionByZeroError: Don't divide by zero!")

