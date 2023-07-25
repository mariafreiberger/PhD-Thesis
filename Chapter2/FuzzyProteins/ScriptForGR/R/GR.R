    bin=0.5
  
    #All
    tabla_all=read.table("/home/maria/Documentos/CDRFR/ConfNR.txt", header=F, stringsAsFactors=F)
  
    FrstAll=tabla_all[,5]
    histFrstALL=hist(FrstAll)
  
   # virtuals_all=read.table("home/maria/Desktop/NewFuzzy/All/home/maria/Documentos/CDRFR/ConfNRNRNRNF0NFNFNNR.txt", stringsAsFactors=F)
    # virtuals_all=virtuals_all[,5]
    NVp=length(tabla_all)
  
    Distances_all=tabla_all[,4]
    values_all=hist(Distances_all, freq=F, breaks=seq(0, ceiling(max(Distances_all)), by=bin))
    dr_all=values_all$mids-bin/2
  
    gr_all=(values_all$density/(4*pi*(values_all$mids-bin/2)^2*bin)/(NVp^2))/10
    plot(gr_all, type="l", xlim=c(0,200))
  
  
    #Neutros
    tabla_neu=read.table("/home/maria/Documentos/CDRFR/NeuConfNR.txt", header=F, stringsAsFactors=F)
    NVPsNeu=length(tabla_neu[,1])
  
    FrstNeu=tabla_neu[,5]
    histFrstNEU=hist(FrstNeu)
    range(FrstNeu)
  
    Distances_neu=tabla_neu[,4]
    values_neu=hist(Distances_neu, freq=F, breaks=seq(0, ceiling(max(Distances_neu)), by=bin))
  
    # if(values_neu$mids[1]>1){
    #   values_neu$mids=values_all$mids
    #   for(j in 1:length(values_neu$density)){
    #     values_aux[j+1]=values_neu$density[j]
    #   }
    #   values_neu$density=values_aux
    # }
    dr_neu=values_neu$mids-bin/2
    gr_neu=(values_neu$density/(4*pi*(values_neu$mids-bin/2)^2*bin)/(NVPsNeu^2))/10
    plot(gr_neu, type="l", xlim=c(0,200), bg="white")
  
    #Maximos
    tabla_max=read.table("/home/maria/Documentos/CDRFR/MaxConfNR.txt", header=F, stringsAsFactors=F)
    NVPsMax=length(tabla_max[,1])
  
    FrstMax=tabla_max[,5]
    histFrstMax=hist(FrstMax)
    range(FrstMax)
  
    Distances_max=tabla_max[,4]
    values_max=hist(Distances_max, freq=F, breaks=seq(0, ceiling(max(Distances_max)), by=bin))
    dr_max=values_max$mids-bin/2
  
    # if(values_max$mids[1]>1){
    #   values_max$mids=values_all$mids
    #     for(j in 1:length(values_max$density)){
    #       values_aux[j+1]=values_max$density[j]
    #     }
    #     values_max$density=values_aux
    # }
  
    gr_max=(values_max$density/(4*pi*(values_max$mids-bin/2)^2*bin)/(NVPsMax^2))/10
    plot(gr_max, type="l", xlim=c(0,200), bg="white")
  
  
    #Minimos
    tabla_min=read.table("/home/maria/Documentos/CDRFR/MinConfNR.txt", stringsAsFactors=F)
  
    NVPsMin=length(tabla_min[,1])
  
    FrstMin=tabla_min[,5]
    histFrstMin=hist(FrstMin)
    range(FrstMin)
  
    Distances_min=tabla_min[,4]
    values_min=hist(Distances_min, freq=F, breaks=seq(0, ceiling(max(Distances_min)), by=bin))
  
    # if(values_min$mids[1]>1){
    #   values_min$mids=values_all$mids
    #   for(j in 1:length(values_min$density)){
    #     values_aux[j+1]=values_min$density[j]
    #   }
    #   values_min$density=values_aux
    # }
  
    dr_min=values_min$mids-bin/2
  
    gr_min=(values_min$density/(4*pi*(values_min$mids-bin/2)^2*bin)/(NVPsMin^2))/10
    plot(gr_min, type="l", xlim=c(0,200))
    range(gr_min)
  
  
    #Normalizacion a 1 en valor en la posicion tonorm del vector de gr
  
    tonorm=40
    gr_min50=gr_min[1:tonorm]/gr_min[tonorm]
    gr_neu50=gr_neu[1:tonorm]/gr_neu[tonorm]
    gr_max50=gr_max[1:tonorm]/gr_max[tonorm]
    gr_all50=gr_all[1:tonorm]/gr_all[tonorm]
  
  
    dr_min=dr_min[1:tonorm]
    dr_neu=dr_neu[1:tonorm]
    dr_max=dr_max[1:tonorm]
    dr_all=dr_all[1:tonorm]
  
    gr_min50[1]=0
    gr_neu50[1]=0
    gr_max50[1]=0
    gr_all50[1]=0
  
    range(gr_max50)
  
    plot(gr_min50, type="l", main="grmin")
    plot(gr_neu50, type="l", main="grneu")
    plot(gr_max50, type="l", main="grmax")
    plot(gr_all50, type='l', main="grall")
  
    ymax=max(c(max(gr_max50), max(gr_min50), max(gr_neu50), max(gr_all50)))
  
      svg('/home/maria/Documentos/CDRFR/GR_ConfNA.svg', width=6, height= 6)
      plot(dr_all, gr_max50, type="l", col="red", main="", xlab="Distance Angstroms", ylab="g(r)", xlim=c(0,10), ylim=c(0,25), cex.axis=1.5, cex.lab=1.5, lwd=3)
      lines (dr_min, gr_min50, type="l", col="green", lwd=3)
      lines(dr_neu, gr_neu50, type="l", col="grey", lwd=3)
      lines(dr_all, gr_all50, type="l", col="black", lwd=3)
      #legend(y="topright", x="topright", legend=c("min","neu","max","all"), col=c("green", "gray", "red","black"), lty=c(1,1,1), cex=1.5)
      box(lwd=2)
      dev.off()
