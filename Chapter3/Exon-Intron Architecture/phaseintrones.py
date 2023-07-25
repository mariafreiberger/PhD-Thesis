import os
lista=open('/home/maria/Documentos/Doctorado/ExonStartEnd/Lista','r')
out=open('/home/maria/Documentos/Doctorado/PhaseIntrones','w')

for line in lista.readlines():
	line=line[:-1]
	c=0
	intron=open('/home/maria/Documentos/Doctorado/ExonStartEnd/'+line,'r')
	ini=0
	print(line)
	vect=[]
	for lint in intron.readlines():
		lint = lint[:-1]
		sp=lint.split()
		lon=int(sp[2])-int(sp[0]) + 1 - ini
		if lon%3==0:
			vect.append(0)
			ini=0
		elif lon%3==1:
			vect.append(1)
			ini=2
		else:
			vect.append(2)
			ini=1
			
	vect=vect[:-1]
	if len(vect)>3:
		out.write(line+' '+str(vect)+'\n')	
	intron.close()


lista.close()
out.close()

