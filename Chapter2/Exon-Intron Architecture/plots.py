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
		score=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Score/'+lgrp)
		out.write('\n')	
	group.close()
	
lista.close()
