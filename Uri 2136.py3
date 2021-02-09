sim=[]#lista que quer ser amigo do habay
nao=[]#lista que não quer ser amigo do habay
yes="YES"
no="NO"
amigo = ""
j = 0
i = 0
escanear = input().split(" ")
while (escanear[0] != "FIM"):# sentinela para parar o algoritmo quando o scan for FIM
	if yes in escanear[1]:#testa se quer ser o amigo do habay
		if escanear[0] not in (sim): #testa se ele já se candidatou, se sim ignora, se não entra na lista
			sim.append(escanear[0])#insere o nome do candidato
	if no in escanear[1]:#testa se o usuario não quis se candidatar
		#if escanear[0] not in (nao):#testa se o usuario ja esta se cadastrado, se sim ignora, se não entra na lista 
		nao.append(escanear[0])
	escanear = input().split(" ")
for j in range(len(sim)):
	if len(sim[j]) > i:
		amigo = sim[j]
		i = len(amigo) 
sim.sort()#Ordena a lista sim
nao.sort()#Ordena a lista nao
for i in range(len(sim)):#printa a lista sim
    print(sim[i])
for i in range(len(nao)):#printa a lista nao
    print(nao[i])
print("\nAmigo do Habay:")
print(amigo)
