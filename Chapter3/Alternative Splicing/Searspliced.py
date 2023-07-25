import os

lista=open('/home/maria/Documentos/Doctorado/RepeatsSplice/Lista','r')
out=open('Posiciones_splice_All','w')

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
	for j in range(0,len(violet)-1):
		a=int(violet[j+1]) - int(violet[j])
		if a == 1:
			consec+=1
		else:
			noconse+=1
	#print(line+' '+str(consec)+' '+str(noconse))
	if len(violet) == 0:
		out.write(line+' '+str(0)+'\n')
	if consec > 0:
		if len(sp) != len(violet):
			#if violet[len(violet)-1] == sp[len(sp) -1]:
			distmenor=int(violet[0])-1
			distmayor=int(violet[len(violet)-1]) - len(sp)
			#print(line+' '+str(distmenor)+' '+str(distmayor))
			if len(vector)==len(violet):
				out.write(line+' '+str(1)+'\n')
			elif distmenor == 0:
				out.write(line+' '+str(2)+'\n')
			elif distmayor == 0:
				out.write(line+' '+str(3)+'\n')
			elif len(violet) == 0: 
				out.write(line+' '+str(0)+'\n')
			else:
				out.write(line+' '+str(4)+'\n')
			
		#else:
		#	out.write(line+' '+str(4)+'\n')
		#	print(line+' '+str(distmenor))
lista.close()
out.close()
