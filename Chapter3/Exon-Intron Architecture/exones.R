  table_data=read.table(file = "/home/maria/Documentos/Doctorado/Exones/Exones_unicos/Exones_Todos",header = F, stringsAsFactors = F)
  #/home/maria/Documentos/Doctorado/Exones/Exones_unicos/Exones_Todos
  library(ggplot2)
  
  data <- data.frame(ExonLength = table_data$V1, ExonRepeat = table_data$V2, Encode=table_data$V3)
  
  # change fill and outline color manually 
  p <- ggplot(data, aes(x = ExonLength)) +
    geom_histogram(aes(color = ExonRepeat, fill = ExonRepeat), 
                   position = "identity", bins = 10000, alpha = 0.4) +
    scale_color_manual(values = c("#C77CFF", "#E7B800")) +
    scale_fill_manual(values = c("#C77CFF", "#E7B800"))
  p <- p + theme_classic()  + labs(x = "Exon Length") + labs(y = "Frequency") + scale_x_log10()# + scale_x_continuous(trans='log2')  
  #+  scale_x_continuous(breaks = round(seq(min(ExonLength), max(ExonLength), by = 50),1))  # + xlim(c(1,	300))
  p
  
  p <- ggplot(data, aes(x = ExonLength)) +
    geom_histogram(aes(color = ExonRepeat, fill = ExonRepeat), 
                   position = "identity", bins = 10, alpha = 0.4) +
    scale_x_continuous(breaks = c(100,120,130,140,150,160,170,180,190), limits = c(100,200)) +
    scale_color_manual(values = c("#C77CFF", "#E7B800")) +
    scale_fill_manual(values = c("#C77CFF", "#E7B800"))  #+ xlim(c(89,	108))
  p <- p + theme_classic()  + labs(x = "Exon Length") + labs(y = "Frequency")
  p
  
  
  
  intrones=read.table('/home/maria/Documentos/Doctorado/IntronL',header=F)
  datain <- data.frame(intlen=intrones$V2)
  p <- ggplot(datain, aes(x = intlen)) +
    geom_histogram(bins = 500) 
  p <- p + theme_classic()  + labs(x = "Intron Length") + labs(y = "Frequency")  + scale_x_log10()   # + xlim(c(1,	300))
  p
  
  #/home/maria/Documentos/Doctorado/Phases/IPhases
  
  intrones=read.table('/home/maria/Documentos/Doctorado/Phases/IPhases',header=F)
  datain <- data.frame(intlen=intrones$V1)
  p <- ggplot(datain, aes(x = intlen)) +
    geom_histogram(binwidth = 0.8, col="white",bins = 3) 
  p <- p + theme_classic()  + labs(x = "Intron Phases") + labs(y = "Frequency") # + scale_x_log10()   # + xlim(c(1,	300))
  p