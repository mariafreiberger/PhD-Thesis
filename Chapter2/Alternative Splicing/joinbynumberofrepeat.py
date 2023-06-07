import os

lista=open('Lista','r')
out=open('Cant_Repeat','w')

for line in lista.readlines():
	line=line[:-1]
	os.system('wc -l '+line+' > wc_l')
	aux=open('wc_l','r')
	for laux in aux.readlines():
		sp=laux.split()
		la=int(sp[0])-1
		out.write(line+' '+str(la)+'\n')
	aux.close()
lista.close()
out.close()

grupos=open('Cant_Repeat','r')

for gline in grupos.readlines():
	spl=gline.split()
	s=spl[0].split('_')
	out=open('Group_'+spl[1],'a')
	out.write(spl[0]+' '+s[0]+' '+spl[1]+'\n')
	out.close()

grupos.close()
