#R --no-save -f anova.organic.R <file> #usage
#1    2       3 4                 5    

args<-commandArgs()
data<-read.csv(file=args[5],header=FALSE)

output<-gsub("( )", "", paste(args[5],".organic.out"))
sink(output, append=FALSE,split=FALSE)

x1=data[1,4:6]
x2=data[1,10:12]
x3=data[1,16:18]
xx=cbind(x1,x2,x3)
xx=t(xx)
xx2=(xx)
xreplicates=c(1,2,3,1,2,3,1,2,3)
xtreatments=c(0,0,0,1,1,1,2,2,2)

organic.horizon.data<-data.frame(cbind(xx2,xreplicates,xtreatments))
names(organic.horizon.data)=c("Response","Replicate","OC.removal")

attach(organic.horizon.data)
OC.removal=factor(OC.removal)
result<-summary(fm2 <- aov(Response ~ OC.removal))

print(args)
print(result)
sink()


