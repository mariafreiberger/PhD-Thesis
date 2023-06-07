with open("/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique") as DIRE:
    lista = DIRE.readline()

    while lista:
        lista = lista.strip()
        sp = lista.split(" ")
        guarda = open(f"/home/maria/Documentos/InterfaceRes/VPs/{sp[0]}/{sp[0]}.vpC", "w")
        frst = open(f"/home/maria/Documentos/InterfaceRes/{sp[0]}.pdb.done/FrustrationData/{sp[0]}.pdb_configurational")

        for frst_line in frst:
            frst_line = frst_line.strip()
            splitfrst = frst_line.split(" ")
            coord = open(f"/home/maria/Documentos/InterfaceRes/VPs/{sp[0]}/{sp[0]}.coord")

            for coord_line in coord:
                coord_line = coord_line.strip()
                splitcoord = coord_line.split(" ")

                if int(splitfrst[0]) == int(splitcoord[0]):
                    R1X = float(splitcoord[3])
                    R1Y = float(splitcoord[4])
                    R1Z = float(splitcoord[5])

                if int(splitfrst[1]) == int(splitcoord[0]):
                    R2X = float(splitcoord[3])
                    R2Y = float(splitcoord[4])
                    R2Z = float(splitcoord[5])
                    X = (R1X + R2X) / 2
                    Y = (R1Y + R2Y) / 2
                    Z = (R1Z + R2Z) / 2
                    guarda.write(f"{splitfrst[0]} {splitfrst[1]} {splitfrst[2]} {splitfrst[3]} ")
                    guarda.write(f"{X:.3f} {Y:.3f} {Z:.3f} {splitfrst[11]}\n")
                    break

            coord.close()

        guarda.close()
        frst.close()

        lista = DIRE.readline()

