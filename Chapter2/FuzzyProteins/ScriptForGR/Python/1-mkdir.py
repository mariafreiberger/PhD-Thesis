import os

lista = open("/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique")
os.system("cd /home/maria/Documentos/InterfaceRes/; mkdir VPs")

linea = lista.readline()
while linea:
    linea = linea.strip()
    splista = linea.split(" ")
    # splista[0] = splista[0].lower()
    os.system("cd /home/maria/Documentos/InterfaceRes/VPs; mkdir " + splista[0])
    linea = lista.readline()

lista.close()
