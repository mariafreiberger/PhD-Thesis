tablagc=read.table(file="/home/maria/Documentos/Doctorado/GC/TablaGCTax", header = F, stringsAsFactors = F)

plot(tablagc$V2,tablagc$V3)
table=read.table(file = "/home/maria/Documentos/Doctorado/Exones/ClassAll",header = F, stringsAsFactors = F)

library(ggplot2)

  df <- data.frame(ExonClass = table$V1, Frequency = table$V2)
  
  # change fill and outline color manually 
  p<-ggplot(df, aes(x=ExonClass, y=Frequency, fill=ExonClass)) +
    geom_bar(stat="identity")+theme_minimal()
  p <- p + theme_classic()  + labs(x = "Exon Class") + labs(y = "Frequency") #+
  # xlim(c(1,300))
  
  p

  table_data=read.table(file = "/home/maria/Documentos/Doctorado/Exones/Class_Repeat",header = F, stringsAsFactors = F)
  data <- data.frame(ExonClass = table_data$V1, IntronPhase = table_data$V2)
  
  # change fill and outline color manually 
  p <- ggplot(data, aes(x = ExonClass)) +
    geom_histogram(aes(color = ExonClass, fill = ExonClass), 
                   position = "identity", bins = 9,col="white") +
    scale_x_continuous(breaks = c(0,1,2,3,4,5,6,7,8))
  p <- p + theme_classic()  + labs(x = "Exon Class") + labs(y = "Frequency")
  p
  
  table_data=read.table(file = "/home/maria/Documentos/Doctorado/Exones/Phases_Repeat",header = F, stringsAsFactors = F)
  data <- data.frame(ExonClass = table_data$V1, IntronPhase = table_data$V2)
  
  p <- ggplot(data, aes(x = IntronPhase)) +
    geom_histogram(aes(color = IntronPhase, fill = IntronPhase), 
                   position = "identity", bins = 3,col="white") +
    scale_x_continuous(breaks = c(0,1,2))
  p <- p + theme_classic()  + labs(x = "Intron Phase") + labs(y = "Frequency")
  p