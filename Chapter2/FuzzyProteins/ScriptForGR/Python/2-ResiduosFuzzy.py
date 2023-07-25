with open("/home/maria/Documentos/InterfaceRes/Fuzzy_NR") as lista:
    for linea in lista:
        linea = linea.strip()
        sp = linea.split(" ")
        spchain = sp[0].split("_")
        spres = sp[1].split(";")
        # spb[0] = spb[0].lower()
        with open(f"/home/maria/Documentos/InterfaceRes/VPs/{spchain[0]}/{spchain[0]}.ResPos", "a") as res:
            d = len(spres)
            c = 0
            while c < d:
                res.write(f"{spres[c]} {spchain[1]}\n")
                c += 1
