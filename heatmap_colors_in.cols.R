library(pheatmap)

data=read.csv(file=file.choose(),header=TRUE,row.names=1)

dim(data)
mycolors=as.character(data$col.leaf)

data$col.leaf=NULL #delete color leaf from original data
data2<-data
data2$col.leaf=NULL
data2=as.matrix(data2)

heatmap.2(data2,RowSideColor=mycolors)

mycolors2<-data.frame(data$col.leaf)
class(mycolors2)
pheatmap(data2,annotation=mycolors2)

dim(data2)
annotation=data.frame(Var1 = factor(1:10 \%\% 2== 0, labels = c("Class1", "Class2")), Var2 = 1:10) annotation$Var1 = factor(annotation$Var1, levels = c("Class1", "Class2", "Class3"))
rownames(annotation) = paste("Test", 1:10, sep = "")

pheatmap(test, annotation = annotation)

Var1=factor(1:10 \%\% 2== 0)



