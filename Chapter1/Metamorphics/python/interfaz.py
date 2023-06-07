import os

res=open('/home/maria/Documentos/Gonzalo/Chile/30/Full/IC_Conf_Full','r')
out_c=open('Conservados_Interfaz','w')
out_nc=open('Todos_Interfaz','w')

for line in res.readlines():
	sp=line.split()
	if sp[0] != 'Res':
		if int(sp[0]) >= 111 and int(sp[1]) < 111:
			out_nc.write(sp[0]+' '+sp[1]+' '+sp[3]+' '+sp[14]+' '+sp[15]+'\n')
			if float(sp[3])>=0.5:
				out_c.write(sp[0]+' '+sp[1]+' '+sp[3]+' '+sp[14]+' '+sp[15]+'\n')
		if int(sp[0]) < 111 and int(sp[1]) >= 111:
			out_nc.write(sp[0]+' '+sp[1]+' '+sp[3]+' '+sp[14]+' '+sp[15]+'\n')
			if float(sp[3])>=0.5:
				out_c.write(sp[0]+' '+sp[1]+' '+sp[3]+' '+sp[14]+' '+sp[15]+'\n')
		
		
res.close()
out_c.close()
out_nc.close()
