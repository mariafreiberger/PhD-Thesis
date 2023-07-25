import math

with open("/home/maria/Documentos/InterfaceRes/Fuzzy_NR") as lista:
    DistEu = 0.0
    l = 0
    line = lista.readline()

    while line:
        line = line.strip()
        sp = line.split(" ")
        spchain = sp[0].split("_")
        guarda = open(f"/home/maria/Documentos/InterfaceRes/VPs/{spchain[0]}/{spchain[0]}.DistEuM", "w")
        CR = open(f"/home/maria/Documentos/InterfaceRes/VPs/{spchain[0]}/{spchain[0]}.ResF")

        for lineaCR in CR:
            lineaCR = lineaCR.strip()
            splitterCR = lineaCR.split(" ")
            coordVP = open(f"/home/maria/Documentos/InterfaceRes/VPs/{spchain[0]}/{spchain[0]}.vpM")

            for lineaVP in coordVP:
                lineaVP = lineaVP.strip()
                spliterVP = lineaVP.split(" ")
                DistEu = math.sqrt(
                    (float(spliterVP[4]) - float(splitterCR[3])) ** 2
                    + (float(spliterVP[5]) - float(splitterCR[4])) ** 2
                    + (float(spliterVP[6]) - float(splitterCR[5])) ** 2
                )
                guarda.write(f"{splitterCR[0]} {spliterVP[0]} {spliterVP[1]} ")
                guarda.write(f"{DistEu:.3f} {spliterVP[7]}\n")

            coordVP.close()

        guarda.close()
        CR.close()
        line = lista.readline()

