
lista=open('/home/maria/Documentos/Doctorado/Phases/TableComplete')
out=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/VarPhase100','w')

line = lista.readlines()
lista.close()
 
for i in range(1, len(line)):
	line[i]=line[i].rstrip('\n')
	sp=line[i].split(',')
	ssp=sp[2].split()
	#if len(ssp) > 4:
	cero=sp[2].count('0')
	uno=sp[2].count('1')
	dos=sp[2].count('2')
	pcero=cero/(cero+uno+dos)
	puno=uno/(cero+uno+dos)
	pdos=dos/(cero+uno+dos)
	if pcero == 1:
		out.write(sp[1]+' 0\n')
	elif puno == 1:
		out.write(sp[1]+' 1\n')
	elif pdos == 1:
		out.write(sp[1]+' 2\n')

out.close()
