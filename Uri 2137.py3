scanner=1
while scanner != "0":
	try:
		lista=[]
		scanner=int(input())
		for i in range(0,scanner):
			x=input()
			if len(x)==4:
				lista.append(x)
		lista.sort()
		for j in range(0,len(lista)):
			print(lista[j])
	except (EOFError):
    		break
