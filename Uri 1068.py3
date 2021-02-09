scan = "a"
while scan != 0:
	try:
		scan=input()
		a=[]
		b=0
		for i in range(len(scan)):
			if scan[i] == "(":
				a.append(i)
			if scan[i] == ")":
				if len(a)>0:
					del(a[0])
				else:
					b=1
					break
		if len(a)>0  or b==1:
			print("incorrect")
		else:
			print("correct")
	except (EOFError):
    		break
