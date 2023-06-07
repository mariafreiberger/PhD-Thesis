import os
lista = open('Exon_Repeats.txt','r')
out = open('Exones','w')

for line in lista.readlines():
	line=line[:-1]
	splilne=line.split()
	l=len(splilne) - 2
	c=2
	if l > 1:
		out.write(splilne[0])
		while c < l:
			out.write('_'+splilne[c]+'-'+splilne[c+2])
			c=c+3
		out.write('\n')


out.close()
lista.close()
