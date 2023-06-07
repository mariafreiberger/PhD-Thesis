lista=open('Tamanio')

for line in lista.readlines():
	line=line.rstrip('\n')
	sp=line.split()
	out=open(sp[0]+'group','a')
	print(sp[0])
	out.write(sp[1]+'\n')
	out.close()

lista.close()
