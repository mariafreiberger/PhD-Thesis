with open("/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique") as DIRE:
    lista = DIRE.readline()

    while lista:
        lista = lista.strip()
        sp = lista.split(" ")
        pdb_path = f"/home/maria/Documentos/InterfaceRes/{sp[0]}.pdb.done/{sp[0]}.pdb"

        with open(pdb_path) as pdb, open(f"/home/maria/Documentos/InterfaceRes/VPs/{sp[0]}/{sp[0]}.coord", "w") as guarda:
            for pdb_line in pdb:
                pdb_line = pdb_line.strip()
                splitter2 = list(pdb_line)
                atom = "".join(splitter2[0:4])
                ca = "".join(splitter2[13:15])

                if atom == "ATOM" and ca == "CA":
                    res = "".join(splitter2[22:26])
                    x = "".join(splitter2[26:38])
                    y = "".join(splitter2[38:46])
                    z = "".join(splitter2[46:54])
                    res = res.strip()
                    x = x.strip()
                    y = y.strip()
                    z = z.strip()
                    guarda.write(f"{res} {splitter2[21]} {splitter2[17:20]} {x} {y} {z}\n")

        lista = DIRE.readline()
