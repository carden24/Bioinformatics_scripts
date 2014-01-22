
data=read.csv(file=file.choose(),header=TRUE,row.names=1)
data2=data
data2$col.leaf=NULL
data2$col.tree=NULL
data2$Tree=NULL
data2$Leaf=NULL

data2=as.matrix(data2)

column_annotation1=matrix(data$Tree)
column_annotation2=matrix(data$Leaf)
column_annotation_all=cbind(column_annotation1,column_annotation2)
colnames(column_annotation_all)=c("Tree","Leaf")
rownames(column_annotation_all)=rownames(data2)
data2=t(data2)

pheatmap(data2, annotation=column_annotation_all,cex=0.8)


column_color_annotation1=matrix(data$col.leaf)
column_color_annotation2=matrix(data$col.tree)
column_color_annotation_all=cbind(column_color_annotation1,column_color_annotation2)




# Generate some data
test = matrix(rnorm(200), 20, 10)
colnames(test) = paste("Test", 1:10, sep = "")
rownames(test) = paste("Gene", 1:20, sep = "")


# Generate column annotations
annotation = data.frame(Var1 = factor(1:10 %% 2 == 0, labels = c("Class1", "Class2")), Var2 = 1:10)
annotation$Var1 = factor(annotation$Var1, levels = c("Class1", "Class2", "Class3"))
rownames(annotation) = paste("Test", 1:10, sep = "")

pheatmap(test, annotation = annotation)


# Specify colors
Var1 = c("navy", "darkgreen")
names(Var1) = c("Class1", "Class2")
Var2 = c("lightgreen", "navy")

ann_colors = list(Var1 = Var1, Var2 = Var2)

pheatmap(test, annotation = annotation, annotation_colors = ann_colors, main = "Example with all the features")

# Specifying clustering from distance matrix
drows = dist(test, method = "minkowski")
dcols = dist(t(test), method = "minkowski")
pheatmap(test, clustering_distance_rows = drows, clustering_distance_cols = dcols)