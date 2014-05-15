data<-read.csv(file=file.choose(),header=TRUE,row.names=1)
for (evalue in names(data)){
  xx=data$expected
  yy=data[,evalue]
  zz=xx+yy
  data2<-data.frame(cbind(xx,yy,zz))
  data3<-subset(data2,data2$zz>0)
  cor<-cor(data3$xx,data3$yy)
  message<-paste(evalue,",",cor[1])
  print(message)
}
