import os

lista=open('Lista2','r')
out=open('Grupos_Especies','w')

for line in lista.readlines():
	line=line[:-1]
	wget='wget https://www.uniprot.org/uniprot/'+line+'.txt -O aux'
	os.system(wget)
	uniprot=open('aux','r')
	for unip in uniprot.readlines():
		spunip=unip.split()
		if spunip[0] == 'OS':
			print (unip)
			out.write(line+' '+' '+unip)
			break
		
lista.close()
out.close()
