import os
lista=open('/home/maria/Documentos/Doctorado/Phases/TableComplete')
out=open('/home/maria/Documentos/Doctorado/Phases/TableCompleteVar','w')
outa=open('/home/maria/Documentos/Doctorado/Phases/IDsAlign','w')
out.write('UniprotID,EMBLID,IntronPhase,ExonLength,NRepeat,ExonVar\n')

for line in lista.readlines():
	line=line.rstrip('\n')
	sp=line.split(',')
	length=sp[3].split()
	if len(length) >= 3:
		out.write(line+',')
		mf=max(set(length), key = length.count)
		num=length.count(mf)
		var=1-(num/len(length))
		out.write(str(var)+'\n')
		outa.write(sp[1]+'\n')
		if var <= 0.5:
			print(sp[1])
	
lista.close()
out.close()
outa.close()
