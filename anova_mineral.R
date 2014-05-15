#R --no-save -f anova.mineral.R <file> #usage
#1    2       3 4                 5    

args<-commandArgs()
data<-read.csv(file=args[5],header=FALSE)

output<-gsub("( )", "", paste(args[5],".mineral.out"))
sink(output, append=FALSE,split=FALSE)

y1=data[1,1:3]
y2=data[1,7:9]
y3=data[1,13:15]
y4=data[1,19:21]
yy=cbind(y1,y2,y3,y4)
yy=t(yy)
yy2=(yy)


replicates=c(1,2,3,1,2,3,1,2,3,1,2,3)
treatments=c(0,0,0,1,1,1,2,2,2,3,3,3)

mineral.horizon.data<-data.frame(cbind(yy2,replicates,treatments))
names(mineral.horizon.data)=c("Response","Replicate","OC.removal")

attach(mineral.horizon.data)
OC.removal=factor(OC.removal)

result<-summary(fm1 <- aov(Response ~ OC.removal))

print(args)
print(result)
sink()


