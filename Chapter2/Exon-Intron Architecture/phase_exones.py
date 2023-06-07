import os 

lista=open('Lista_Fasta','r')
out=open('Clases_exones','w')

for line in lista.readlines():
	line=line[:-1]
	rest=0
	phase=0
	fasta=open('/home/maria/Documentos/Doctorado/SeqExones/Seq'+line,'r')
	for lfasta in fasta.readlines():
		lfasta=lfasta[:-1]
		if lfasta[0] == '>':
			sp=lfasta.split('_')
			rest=int(sp[2])-int(sp[1])+1
			if phase == 1:
				rest=rest-2
			elif phase == 2:
				rest=rest-1
			auxp=rest%3
			out.write(line+' '+lfasta+' '+str(phase)+'-'+str(auxp)+'\n')
			phase=auxp
	fasta.close()
lista.close()
out.close()
