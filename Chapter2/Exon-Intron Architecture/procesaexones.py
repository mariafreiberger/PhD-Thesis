import os

lista=open('ANK_EMBL.txt','r')

for line in lista.readlines():
	line=line[:-1]
	sp=line.split('|')
	seq=sp[2]
	if sp[3] != ' ':
		exones=sp[3]
		infin=exones.split(';')
		out=open('Seq'+sp[1],'a')
		for i in range(0, len(infin)-1):
			splong=infin[i].split()
			ini=int(splong[0])-1
			fin=int(splong[2])-1
			out.write('>Exon_'+str(ini)+'_'+str(fin)+'\n')
			for j in range(ini,fin):
				out.write(seq[j])
			out.write('\n')
		out.close()
lista.close()
