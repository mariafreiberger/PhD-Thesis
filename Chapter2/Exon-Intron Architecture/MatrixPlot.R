library(reshape2)
library(ggplot2)
library("argparse")
parser <- ArgumentParser()
parser$add_argument("--mat", help="Is the matrix")
parser$add_argument("--size", help="Is the matrix size")
parser$add_argument("--name", help="name to save the plot")
args <- parser$parse_args()

matVar = read.table(args$mat,header=F)
varieties = 1:args$size
df <- data.frame(id=varieties,matVar)
colnames(df)[2:ncol(df)] <- varieties
gg <- melt(df, id="id")
ggplot(gg, aes(x=id,y=variable,fill=value))+
  geom_tile()+
  scale_fill_gradient(low="#FFFF88",high="#FF0000")+
  coord_fixed()
ggsave(paste("/home/maria/Documentos/Doctorado/Phases/NuevoDatos07-2023/Plots/o ",args$name,".png", sep=""))