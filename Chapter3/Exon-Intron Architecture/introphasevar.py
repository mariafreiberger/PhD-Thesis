import os
lista=open('/home/maria/Documentos/Doctorado/Phases/TableCompleteVar','r')
out=open('/home/maria/Documentos/Doctorado/Phases/TableVarPhaseAll','w')
out.write('Uniprot,EMBL,Phase,VarIntron\n')
lines=lista.readlines()[1:]
lista.close()

for line in lines:
	lines=line.rstrip('\n')
	sp=line.split(',')
	length=sp[2].split()
	print(sp[2])
	if len(length) >= 1:
		mf=max(set(length), key = length.count)
		num=length.count(mf)
		var=1-(num/len(length))
		out.write(sp[0]+','+sp[1]+','+str(mf)+','+str(var)+'\n')

out.close()
