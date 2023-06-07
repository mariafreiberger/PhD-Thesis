import numpy as np

vect=np.zeros(163)
vect_all=np.zeros(163)
vect_nom=np.zeros(163)

IC=open('IC_Conf_Full','r')
all_cont=np.zeros(163)

for lines in IC.readlines():
	lines=lines[:-1]
	sp=lines.split()
	if sp[0]!='Res':
		if float(sp[3]) >= 0.5 and float(sp[14]) >= 0.5:
			all_cont[int(sp[0])] +=1
			all_cont[int(sp[1])] +=1
			if sp[15] == 'MIN':
				vect_all[int(sp[0])] +=1
				vect_all[int(sp[1])] +=1
				if int(sp[0]) >=114 or int(sp[1]) >=114:
					vect[int(sp[0])] +=1
					vect[int(sp[1])] +=1
					#print(sp[0]+' '+sp[1])
				else:
					vect_nom[int(sp[0])] +=1
					vect_nom[int(sp[1])] +=1
print('Res Metam NoMetam AllContacts')
for i in range(1,len(vect)):
	if all_cont[i] != 0:
		suma=float(vect_all[i])/float(all_cont[i])
		if vect[i]>=3 and suma >0.5:
			print(str(i)+'	'+str(vect[i])+'	'+str(vect_nom[i])+'	'+str(all_cont[i]))
#print(vect)
IC.close()
