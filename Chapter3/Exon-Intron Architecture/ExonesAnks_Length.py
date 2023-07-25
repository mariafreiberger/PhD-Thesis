
def max_lar(List):
	return max(set(List), key = List.count)
	
import os

lista=open('/home/maria/Documentos/Doctorado/Exones/ExonesLengthU','r')
out=open('Exones-Ank-Fase','w')

unip=''
for line in lista.readlines():
	line=line.rstrip('\n')
	sp=line.split()
	if sp[0] !=unip:
		if unip!='':
			aux.close()
			os.system('sort -u Aux > Aux2')
			exones=open('Aux2')
			fase=0
			out.write(sp[0])
			exon=exones.readlines()
			exones.close()
			for i in range(0,len(exon)-1):
				spexon=exon[i].split()
				fase=(int(sp[1])+fase)%3
				out.write(' '+str(fase))
			
			out.write('\n')
			#largos=[]
			#for lex in exones.readlines():
			#	spex=lex.split()
			#	largos.append(int(spex[1]))
			#varb=max_lar(largos)
			#var_por=largos.count(varb)/float(len(largos))
			#out.write(unip+' '+str(var_por)+'\n')
			
			
		unip=sp[0]
		aux=open('Aux','w')
	#if sp[2] == 'PartialAnkRepeat' or sp[2] == 'CompleteAnkRepeat':	
	aux.write(sp[0]+' '+sp[1]+' '+sp[4]+' '+sp[5]+'\n')
	#aux.write(sp[0]+' '+sp[1]+'\n')
lista.close()
out.close()
