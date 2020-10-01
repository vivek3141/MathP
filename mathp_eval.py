def mathpevalplus(s):
	a = ""
	sum = 0
	z = ""
	c = 0
	op = ""
	for i in s:
		if(i == "+"):
			sum += int(a)
			a = ""
			op = "+"
		if(i == "-"):
			sum += int(a)
			a = ""
			op = "-"
		else:
			a += i
		try:
			z = s[c+1]
		except IndexError:
			if(op == "+"):
				sum = sum + int(a)
			elif(op == "-"):
				sum = sum - int(a)
			else:
				sum = sum + int(a)
		c = c + 1				
	return sum
def mathpeval(s):
	if(s.find('*') == -1 and s.find('/') == -1 and s.find('+') == -1 and s.find('-') == -1) and ("(" in s or ")" in s):
		raise SyntaxError
		return False
	return mathpevalbrac(s)
def mathpevalbrac(s):
	st = s
	z = ""
	add = False
	co = 0
	for i in s:
		if(i == "("):
			z = z + i
			co = co + 1
			add = True
		elif(i == ")" and co == 1):
			add = False
			break
		elif(i == ")"):
			z = z + i
			co = co - 1
		elif(add):
			z = z + i
	exe = z
	exe = exe.replace("(","",1)
	z =  z + ")"
	x = exe
	if(exe == "" and "(" in s):
		raise SyntaxError
		return False
	while(str(exe).find("(") != -1):
		exe = mathpeval(exe)		
	res = mathpevalmul(exe)
	st = st.replace(z,str(res),1)
	if "(" in exe:
		st = st.replace(z,str(res),1)
		st = mathpeval(st)
	else:
		st = mathpevalmul(st)
		return str(st)
	
def mathpevalmul(s):
	st = s
	div = []
	mul = []
	c = 0
	for i in st:
		if(i == "*"):
			mul.append(c)
		c = c + 1
	for i in mul:
		k = ""
		indexm = i-1
		while(indexm >= 0 and indexm < len(s)):
			if not (s[indexm].isdigit()):
				break
			k = k + s[indexm]
			indexm = indexm - 1
		k = "".join(reversed(k))
		indexf = i+1
		v = ""
		while(indexf < len(s)):
			if not(s[indexf].isdigit()):
				break
			v = v + s[indexf]
			indexf = indexf + 1
		final = k + "*" + v
		res = str(int(k)*int(v))
		st = st.replace(final,str(res),1)
	while(st.find("*") != -1):
		st = str(mathpeval(st))

	c = 0
	for i in st:
		if(i == "/"):
			div.append(c)
		c = c + 1
	stv = st
	for i in div:
		k = ""
		indexm = i-1
		while(indexm >= 0 and indexm < len(stv)):
			if not (stv[indexm].isdigit()):
				break
			k = k + stv[indexm]
			indexm = indexm - 1
		k = "".join(reversed(k))
		indexf = i+1
		v = ""
		while(indexf < len(stv)):
			if not(stv[indexf].isdigit()):
				break
			v = v + stv[indexf]
			indexf = indexf + 1
		final = k + "/" + v
		if(v == "0"):
			raise ZeroDivisionError
		res = int(k)/int(v)
		res = int(res)
		st = st.replace(final,str(res),1)
	while(st.find("/") != -1):
		st = str(mathpeval(st))
	return mathpevalplus(st)
