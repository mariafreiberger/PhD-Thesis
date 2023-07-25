import os
lista=open('/home/maria/Documentos/Doctorado/Phases/PhaseyLargo')
out=open('/home/maria/Documentos/Doctorado/Phases/TableComplete','w')
out.write('UniprotID,EMBLID,IntronPhase,ExonLength,NRepeat\n')

for line in lista.readlines():
	line=line.rstrip('\n')
	sp=line.split()
	os.system('grep '+sp[0]+' /home/maria/Documentos/Doctorado/Phases/ANK_Repeats.txt > AUX')
	aux=open('AUX')
	laux=aux.readlines()
	aux.close()
	a=len(laux)
	if a >= 1:
		unip=laux[0].split()
		out.write(unip[0]+','+sp[0]+',')
		f=0
		for i in range(1,len(sp)):
			if int(sp[i]) > 2:
				out.write(',')
				f=i
				break
			else:
				out.write(' '+sp[i])
		for i in range(f,len(sp)):
			out.write(' '+sp[i])
		out.write(','+str(a)+'\n')
	
lista.close()
out.close()
