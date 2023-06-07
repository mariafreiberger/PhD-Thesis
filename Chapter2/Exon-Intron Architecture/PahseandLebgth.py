import os
lista=open('/home/maria/Documentos/Doctorado/Phases/Var_0.5','r')
out=open('/home/maria/Documentos/Doctorado/Phases/Var+phase0.5','w')

for line in lista.readlines():
	line=line.rstrip('\n')
	sp=line.split()
	out.write(line)
	intron=open('/home/maria/Documentos/Doctorado/ExonStartEnd/'+sp[0],'r')
	for lint in intron.readlines():
		lint=lint.rstrip('\n')
		splint=lint.split()
		rest=int(splint[2]) - int(splint[0]) + 1 
		out.write(' '+str(rest))
	out.write('\n')
	intron.close()

lista.close()
out.close()

