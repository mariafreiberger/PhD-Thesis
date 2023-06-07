import os 

lista=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Var0.5','r')
#/home/maria/Documentos/Doctorado/SeqExones

for line in lista.readlines():
	line=line[:-1]
	mat=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Alignment_Var_0.5/'+line+'.mat')
	out=open('/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/MatVar/'+line+'.mat','w')
	for lmat in mat.readlines():
		lmat=lmat.rstrip('\n')
		sp=lmat.split()
		if len(sp) > 1:
			for i in range(1,len(sp)):
				if i == len(sp) -1:
			 		out.write(sp[i])
				else:
			 		out.write(sp[i]+' ')
			out.write('\n')
	mat.close()
	out.close()

lista.close()
