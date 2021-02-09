scanner=1
a=""
while scanner != "0":
	try:
		scan=int(input())
		for x in range(0,scan):
			x=input().split(" ")
			x.sort(reverse = True, key = len)
			#print(x)
			#del(a[0])
			for j in range(len(x)):
				if j!=0:
					a=a+" "+x[j]
				else:
					a=x[j]
			print(a)
			scanner=1
			a=""
	except (EOFError):
			break
