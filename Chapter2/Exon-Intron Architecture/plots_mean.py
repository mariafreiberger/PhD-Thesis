import pandas as pd
import numpy as np
import os

lista=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Aux_Phase/grupos')

for line in lista.readlines():
	line=line.rstrip('\n')
	os.system('Rscript generaplots.R --mat /home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/ScorePhase/'+line+'.median --size '+line+' --name '+line)
			
lista.close()
