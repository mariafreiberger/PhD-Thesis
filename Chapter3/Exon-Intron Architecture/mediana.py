import pandas as pd
import numpy as np
import os

lista=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Aux_Phase/grupos')

for line in lista.readlines():
	line=line.rstrip('\n')
	group=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Aux_Phase/'+line+'group')
	a=0
	os.system('rm AuxFiles/**')
	for lgrp in group.readlines():
		lgrp=lgrp.rstrip('\n')
		vi=0
		a+=1
		score=open(lgrp)
		for lscore in score.readlines():
			lscore=lscore.rstrip('\n')
			sp=lscore.split()
			for i in range(0,len(sp)):
				out=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/AuxFiles/'+str(vi)+'_'+str(i),'a')
				out.write(' '+sp[i])
				out.close()
			vi+=1
		score.close()
	out=open('ScorePhase/'+line+'.median','w')
	print(line+'group '+str(a))
	for i in range(0,vi):
		for j in range(0,vi):
			matrix=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/AuxFiles/'+str(i)+'_'+str(j))
			linemat=matrix.readline()
			matrix.close()
			sp=linemat.split()
			vect=np.zeros(len(sp))
			for w in range(0,len(sp)):
				vect[w]=sp[w]
			med=np.median(vect)
			out.write(str(med)+' ')
		out.write('\n')
	out.close()
	group.close()
	
lista.close()
