import os 
lista=open('/home/maria/Documentos/Doctorado/Exones/Exones_Divididos/Lista_exones','r')
out=open('Class_All','w')
#out=open('Phases_All','w') 

for line in lista.readlines():
	line=line[:-1]
	#os.system('sort -u -k3n /home/maria/Documentos/Doctorado/Exones/Exones_Divididos/'+line+' > /home/maria/Documentos/Doctorado/Exones/Exones_unicos/'+line)
	#exones=open('/home/maria/Documentos/Doctorado/Exones/Exones_Divididos/'+spline[0]+'.ex','r')
	
	#out.write(spline[1]+' '+spline[3]+' '+spline[4]+' '+spline[5]+'\n')
	#if ind_ant=='':
	#	ind_ant=spline[0]
	#	phase=int(spline[1])%3
	exones=open('/home/maria/Documentos/Doctorado/Exones/Exones_unicos/'+line,'r')
	exon=exones.readlines()
	exones.close()
	phase=0
	ne=1
	for i in range(0,len(exon)):
		l=exon[i]
		l=l[:-1]
		spl=l.split()
		largo=int(spl[0])
		if phase==1:
			largo=largo-2
		elif phase==2:
			largo=largo-1
		r=largo%3
		if int(spl[2]) == 1 or int(spl[2]) == 3:
			clase=''
			if phase == 0 and r == 0:
				clase=0
			elif phase == 0 and r == 1:
				clase=1
			elif phase == 0 and r == 2:
				clase=2
			elif phase == 1 and r == 0:
				clase=3
			elif phase == 1 and r == 1:
				clase=4
			elif phase == 1 and r == 2:
				clase=5
			elif phase == 2 and r == 0:
				clase=6
			elif phase == 2 and r == 1:
				clase=7
			elif phase == 2 and r == 2:
				clase=8
			out.write(str(clase)+' '+str(r)+'\n')
		phase=r
		#out.write(str(clase)+' '+str(r)+'\n')
lista.close()
out.close()
