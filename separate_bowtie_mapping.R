#R --no-save -f separate.bowtie1.mapping.R file.to.split #usage
#1    2       3 4          		   5

args<-commandArgs()
#print(args)
data<-read.table(file=args[5],header=FALSE,sep = "\t")
fac<-levels(data$V3)
TA<-table(factor(data$V3))

#####1.separate files as tab###########
c=1
while (c<=nrow(as.data.frame(fac))){
subselection<-subset(data,data$V3==fac[c])
file_name<-gsub("( )", "", paste(args[5],"_",fac[c],".txt"))
write.table(subselection,file_name,sep="\t",quote=FALSE,col.names=FALSE,row.names=FALSE)
print(c)
c=c+1
}
##############
