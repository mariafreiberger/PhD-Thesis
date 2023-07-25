with open("/home/maria/Documentos/InterfaceRes/CDRList_F") as DIRE:
    with open("/home/maria/Documentos/InterfaceRes/NeuConf.txt", "w") as CNM:
        with open("/home/maria/Documentos/InterfaceRes/MinConf.txt", "w") as MinTM:
            with open("/home/maria/Documentos/InterfaceRes/MaxConf.txt", "w") as MaxTM:
                with open("/home/maria/Documentos/InterfaceRes/Conf.txt", "w") as totalM:
                    d = 0
                    c0 = 0

                    for lista in DIRE:
                        lista = lista.strip()
                        sp = lista.split(" ")
                        DE = open(f"/home/maria/Documentos/InterfaceRes/VPs/{sp[0]}/{sp[0]}.DistEuC")

                        cont = 0
                        for DE_line in DE:
                            DE_line = DE_line.strip()
                            cont += 1
                            splitter = DE_line.split(" ")
                            tam = len(splitter)

                            if tam < 5:
                                continue
                            else:
                                d += 1
                                if float(splitter[4]) > 0.78:
                                    MinTM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")
                                    totalM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")
                                elif float(splitter[4]) > -1:
                                    CNM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")
                                    totalM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")
                                else:
                                    MaxTM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")
                                    totalM.write(f"{splitter[0]} {splitter[1]} {splitter[2]} {splitter[3]} {splitter[4]}\n")

                        DE.close()

