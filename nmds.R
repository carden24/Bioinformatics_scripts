library(vegan)
library(MASS)

data<-read.csv(file=file.choose(),header=TRUE,row.names=1) #mis muestras estaban ordenadas en columnas
data<-t(data) #asi que hize la transposicion

dist<-vegdist(data,method="bray") # el predeterminado es Bray-Curtis

dist<-vegdist(data,method="jaccard") # el predeterminado es Bray-Curtis

mynmds<-isoMDS(dist) #este es la funcion de NMDS
ordiplot(mynmds,type="text")

mynmds_points<-mynmds$points #extrae las coordindas de los puntos
colnames(mynmds_points)=c("x","y") #cambia el nombre de las columnas a X, Y

#ahora tienes que obtener las las series individualmente y plotear una por una

#primero empiezas con el plot vacio
ordiplot(mynmds,type="none")

#y ahora empiezas con las series
#ejemplo , serie uno primeros tres puntos

#serie      [rango filas, rango columnas]
serie1=data.frame(mynmds_points[1:3,1:2]) #extras dato
points(serie1$x,serie1$y,type="p",col="black",pch=1)  #los pones

serie2=data.frame(mynmds_points[4:6,1:2]) #extras dato
points(serie2$x,serie2$y,type="p",col="black",pch=16)  #los pones

serie3=data.frame(mynmds_points[7:9,1:2]) #extras dato
points(serie3$x,serie3$y,type="p",col="blue",pch=1)  #los pones

serie4=data.frame(mynmds_points[10:12,1:2]) #extras dato
points(serie4$x,serie4$y,type="p",col="blue",pch=16)  #los pones

serie5=data.frame(mynmds_points[13:15,1:2]) #extras dato
points(serie5$x,serie5$y,type="p",col="green",pch=1)  #los pones

serie6=data.frame(mynmds_points[16:18,1:2]) #extras dato
points(serie6$x,serie6$y,type="p",col="green",pch=16)  #los pones


serie7=data.frame(mynmds_points[19:21,1:2]) #extras dato
points(serie7$x,serie7$y,type="p",col="orange",pch=1)  #los pones



#Aca estan los diferentes simbolos de R
#http://voteview.com/symbols_pch.htm

# y aca los diferentes colors
#http://www.stat.columbia.edu/~tzheng/files/Rcolor.pdf


legend("topright", c("OM0C0", "OM1C0", "OM2C0","OM3C0","","Mineral","Organic"), cex=1.5, bty="n",col=c("black","blue","green","orange","white","grey","grey"),pch=c(15,15,15,15,0,16,1))
legend("topright", c("OM0C0", "OM1C0", "OM2C0","OM3C0","","Mineral","Organic"), cex=1.5, col=c("black","blue","green","orange","white","grey","grey"),pch=c(15,15,15,15,0,16,1))

