import sys
import os
import mathp_eval

fil = str(sys.argv[1])
if(os.path.isfile(fil) == False):
	print("MathP Error")
	print("FileError: No such file")
	exit()
str = ""
line = open(fil,"r")
for i in line:
	str = str + i
if(str.find("ex()") != -1):
	exit()
try:
	print(mathp_eval.mathpeval(str))
except SyntaxError:
	print("MathP Error")
	print("SyntaxError: Invalid Syntax\n")
except ValueError:
	print("MathP Error")
	print("StringError: Use numbers only\n")
except NameError:
	print("MathP Error")
	print("StringError: Use numbers only\n")
except EOFError:
	exit()
except KeyboardInterrupt:
	print("KeyboardInterruptError: Keyboard Interrupt")
except TypeError:
	print("MathP Error")
	print("StringError: Use numbers only\n")
