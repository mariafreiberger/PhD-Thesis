#!/usr/bin/env Rscript

# Grafico Contact Map gral

datos<-read.table(file="/home/maria/Documentos/InterfaceRes/3V6R.pdb.done/FrustrationData/3V6R.pdb_configurational_FuzzyRegion",stringsAsFactors = F)

chains<-sort(unique(c(datos$V3,datos$V4)))
positions<-matrix(ncol=3,nrow=length(chains))
auxPosVec<-c()
for(i in seq_along(chains)){
  positions[i,1:2]<-range(c(datos$V1[which(datos$V3==chains[i])],datos$V2[which(datos$V4==chains[i])]))
  positions[i,3]<-positions[i,2]-positions[i,1]+1
  auxPosVec<-c(auxPosVec,positions[i,1]:positions[i,2])
}

#Renumero posiciones
datos$pos1 <- NA
datos$pos2 <- NA
for(i in seq_along(chains)){
  if(i==1){bias <- 0}else{bias <- sum(positions[1:(i-1),3])}
  idx <- which(datos$V3==chains[i] )
  datos$pos1[idx] <- datos$V1[idx]-positions[i,1]+bias+1
  idx <- which(datos$V4==chains[i])
  datos$pos2[idx] <- datos$V2[idx]-positions[i,1]+bias+1
}

posNEW<-matrix(ncol=3,nrow=length(chains))
for(i in seq_along(chains)){
  posNEW[i,1:2]<-range(c(datos$pos1[which(datos$V3==chains[i])],datos$pos2[which(datos$V4==chains[i])]))
  posNEW[i,3]<-posNEW[i,2]-posNEW[i,1]+1
}

total.positions<-sum(apply(positions,1,function(x){x[2]-x[1]+1}))
matrz <- matrix(NA,ncol=total.positions,nrow=total.positions)
for(i in 1:nrow(datos)){
  matrz[datos$pos1[i],datos$pos2[i]]<-datos$V12[i]
  matrz[datos$pos2[i],datos$pos1[i]]<-datos$V12[i]
  
}

png(filename = paste("/home/maria/Documentos/InterfaceRes/3V6R.pdb.done/FrustrationData/3V6R_map.png", sep=""),width = 600,height = 540)
cotaM <- 4
n.breaks=50
vecvalores <- seq(-cotaM,cotaM,length.out = 2*n.breaks)
# vecvalores <- c(vecvalores[1:n.breaks],0,vecvalores[(n.breaks+1):(2*n.breaks)])
colores.paleta<-colorRampPalette(c("red","grey","green"))
colores<-colores.paleta(length(vecvalores)-1)
par(mar=c(5,5,5,5),cex.lab=1.5,cex.axis=1.5)
layout(mat = matrix(1:2,ncol=2),widths = c(5,1))
image(x=1:total.positions,y=1:total.positions,matrz,axes=F,xlab="Residue i",ylab="Residue j",col=colores,asp=1,breaks = vecvalores)

if(length(chains)>1){
  abline(v=cumsum(posNEW[,3])+.5,lty=3,col="darkgrey",lwd=1.5)
  abline(h=cumsum(posNEW[,3])+.5,lty=3,col="darkgrey",lwd=1.5)
  axis(side=3,at=apply(posNEW[,1:2],1,mean),tck=0,las=1,lwd=2,labels = chains,tick = 0)
  axis(side=4,at=apply(posNEW[,1:2],1,mean),tck=0,las=1,lwd=2,labels = chains,tick = 0)
  mtext(text = "Chain",line=3,side=3,cex=1.5)
  mtext(text = "Chain",line=3,side=4,cex=1.5)
}
box(lwd=2)

ticksPos <- axTicks(1)[which(axTicks(1)!=0)]
axis(side=1,at=ticksPos,labels = auxPosVec[ticksPos],tcl=.5,lwd=2)
axis(side=2,at=ticksPos,labels = auxPosVec[ticksPos],tcl=.5,lwd=2)
axis(side=3,at=ticksPos,labels = NA,tcl=.5,lwd=2)
axis(side=4,at=ticksPos,labels = NA,tcl=.5,lwd=2)

par(mar=c(5,1,5,5))
image(y=vecvalores,z=matrix(vecvalores,nrow=1),col=colores,axes=F,ylab="")
axis(side=4,at=seq(-3,3,by=1),tcl=0.3,las=1,lwd=2)
axis(side=4,at=c(-4,4),tcl=0,las=1,lwd=2)
mtext(text = "Local Configurational Frustration Index",line=3,side=4,cex=1.5)
axis(side=2,at=seq(-3,3,by=1),tcl=0.3,labels = NA,lwd=2)

box(lwd=2)

dev.off()

