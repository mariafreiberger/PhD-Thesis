import os

lista=open('/home/maria/Documentos/Doctorado/RepeatsSplice/Lista_Violet','r')
out=open('Posiciones_splice','w')

for line in lista.readlines():
	line=line[:-1]
	splice=open(line,'r')
	vector=[]
	for lsplice in splice.readlines():
		lsplice=lsplice[:-1]
		sp=lsplice.split()
		if sp[len(sp)-1] == '\"orange\"' or sp[len(sp)-1] == '\"violet\"':
			vector.append(sp[len(sp)-1])
	splice.close()
	violet=[]
	for i in range(0,len(vector)):
		if vector[i]=='\"violet\"':
			violet.append(i+1)
	consec=0
	noconse=0
	print(line)
	for j in range(0,len(violet)-1):
		a=int(violet[j+1]) - int(violet[j])
		print(violet[j])
		if a == 1:
			consec+=1
		else:
			noconse+=1
	#print(line+' '+str(consec)+' '+str(noconse))
	if consec > 0:
		if len(sp) != len(violet):
			#if violet[len(violet)-1] == sp[len(sp) -1]:
			distmenor=int(violet[0])-1
			distmayor=int(violet[len(violet)-1]) - len(vector)
			#print(line+' '+str(distmenor)+' '+str(distmayor))
			if distmenor == 0:
				out.write(line+' '+str(0)+'\n')
			elif distmayor == 0:
				out.write(line+' '+str(2)+'\n')
			else:
				out.write(line+' '+str(1)+'\n')
				print(distmayor)
	
lista.close()
out.close()
