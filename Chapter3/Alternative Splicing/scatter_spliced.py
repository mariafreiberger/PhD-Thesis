import os
lista=open('Lista')
out=open('Scatter_Splice','w')
out.write('ID TotalR non-spliced spliced Group\n')

for line in lista.readlines():
	line=line.rstrip('\n')
	os.system('grep orange '+line+' > Orange;wc -l Orange > Cant')
	os.system('grep violet '+line+' > Violet;wc -l Violet >> Cant')
	cant=open('Cant')
	lc=cant.readlines()
	lc[0]=lc[0].rstrip('\n')
	lc[1]=lc[1].rstrip('\n')
	ora=lc[0].split()
	vio=lc[1].split()
	total=int(ora[0])+int(vio[0])
	grp=''
	if total == int(ora[0]):
		grp='red'
	elif total == int(vio[0]):
		grp='green'
	else:
		grp='blue'
	out.write(line+' '+str(total)+' '+ora[0]+' '+vio[0]+' '+grp+'\n')
	
lista.close()
out.close()
