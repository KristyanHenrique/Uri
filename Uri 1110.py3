import collections 
cartas=[]
removidas=[]
removidas2=[]
stringR=""
scan = int(input())#função int torna scan apto para receber numeros inteiros
aux = 0
aux2=""
scan += 1
while (aux==0):
	for x in range(1,scan):#cria a pilha
		cartas.append(x)
	while (len(cartas)>1):#faz as operações da pilha enquanto nao houver apenas 1 uma carta
		removidas.append(cartas[0])
		del(cartas[0])
		aux = cartas[0]
		cartas.append(aux)
		del(cartas[0])
	for i in range(0,len(removidas)):#Transofrmar a pilha em string
		aux2=str(removidas[i])
		removidas2.append(aux2)
		if i!=0:#teste para que não seja adicionado um espaço em branco antes da reposta
			stringR=stringR+", "+removidas2[i]
		else:
			stringR=removidas2[i]
	print("Discarded cards:",stringR)#Printa as cartas removidas
	print("Remaining card:",cartas[0])
	scan = int(input())
	if scan <= 0:
		break
	aux = 0
	scan += 1
	cartas=[]
	removidas=[]
	removidas2=[]
	stringR=""
	aux2=""
