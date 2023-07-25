import pandas as pd
import numpy as np
import os

lista=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/grupos')

for line in lista.readlines():
	line=line.rstrip('\n')
	group=open(line+'group')
	mat=np.zeros((int(line),int(line)))
	a=0
	for lgrp in group.readlines():
		lgrp=lgrp.rstrip('\n')
		vi=0
		a+=1
		score=open(lgrp)
		for lscore in score.readlines():
			lscore=lscore.rstrip('\n')
			sp=lscore.split()
			for i in range(0,len(sp)):
				mat[vi][i]=float(sp[i])
			vi+=1
		score.close()
	mat2=mat/a
	out=open('ScoreVar/'+line+'.mean','w')
	print(line+'group '+str(a))
	for i in range(0,len(mat2)):
		for j in range(0,len(mat2)):
			out.write(str(mat[i][j])+' ')
		out.write('\n')	
	group.close()
	
lista.close()
