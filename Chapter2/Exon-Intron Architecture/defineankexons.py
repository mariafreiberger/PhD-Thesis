import os 
import os.path
import numpy as np

lista=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/TableCompleteVar','r')
#/home/maria/Documentos/Doctorado/SeqExones

for line in lista.readlines():
	line=line[:-1]
	spline=line.split(',')
	path='/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/MatPhase/'+spline[1]+'.mat'
	if os.path.isfile(path):
		spexon=spline[2].split()
		a=len(spexon)+1
		print(spline[1])
		matrix = np.loadtxt(path, usecols=range(0,a))
		os.system('grep '+spline[0]+' /home/maria/Documentos/Doctorado/Exones/ExonesLengthU |awk \'{print $3, $5}\' |sort -u -k2n > Aux')
		aux=open('Aux')
		c=0
		for laux in aux.readlines():
			spaux=laux.split()
			if spaux[0] == 'NoAnkRepeat':
				matrix=np.delete(matrix, c, 0)
				matrix=np.delete(matrix, c, axis=1)
				
			else:
				c+=1
		if len(matrix) > 3:
			out=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/MatAnkPhase/'+spline[1]+'.mat','w')
			for i in range(0,len(matrix)):
				for j in range(0,len(matrix)):
					out.write(str(matrix[i][j])+' ')
				out.write('\n')
			out.close()

lista.close()

#grep A0A178Z7Q7 /home/maria/Documentos/Doctorado/Exones/ExonesLengthU |awk '{print $3, $5}' |sort -u -k2n
