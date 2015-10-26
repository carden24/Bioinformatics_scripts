#R --no-save -f splitter.R file.to.split pieces #usage
#1    2       3 4          5             6   

args<-commandArgs() #read from arguments
data<-read.table(file=args[5],header=FALSE,sep = "\t") #open file to split

size=nrow(data)
pieces=as.integer(args[6]) #this was the problem as the argument is passed in " ". so need to make it integer
interval<-as.integer(trunc(size/pieces)) #rounding up divisor

c=1
d=c+interval-1
while (c+interval-1<=size){
d=c+interval-1
d1<-data[c:d,]
file_name<-gsub("( )", "", paste(args[5],"_cols_",c,"_to_",d))
write.table(d1,file_name,sep="\t",quote=FALSE,col.names=FALSE,row.names=FALSE)
c=d+1
}

if (d==size) {
print("exact")
} else {
d1<-data[c:size,]
file_name<-gsub("( )", "", paste(args[5],"_cols_",c,"_to_",size))
write.table(d1,file_name,sep="\t",quote=FALSE,col.names=FALSE,row.names=FALSE)
print("nice")
}
