import os

out=open('/home/maria/Documentos/Doctorado/Phases/Var+phase0.5','w')

var=open('/home/maria/Documentos/Doctorado/Phases/Var_0.5')
linevar=var.readlines()
var.close()

pl=open('/home/maria/Documentos/Doctorado/Phases/PhaseyLargo')
line=pl.readlines()
pl.close()

for i in range(0,len(linevar)):
	spvar=linevar[i].split(' ')
	for j in range(0,len(line)):
		sp=line[j].split(' ')
		if spvar[0] == sp[0]:
			line[j]=line[j].rstrip('\n')
			r=(len(sp)/2)
			print(sp[0]+' '+str(len(sp)))
			out.write(line[j]+' '+str(int(r))+'\n')

out.close()

