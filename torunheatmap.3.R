source("heatmap.3.R")


#cazy data
data=read.csv(file=file.choose(),header=TRUE,row.names=1)
data2=data
data2$Treatment=NULL
data2$Horizon=NULL
data2=as.matrix(data2)
column_annotation1=matrix(data$Horizon)
column_annotation2=matrix(data$Treatment)
column_annotation_all=cbind(column_annotation1,column_annotation2)
colnames(column_annotation_all) <- c("Horizon", "Treatment")
rownames(column_annotation_all)<-rownames(data2)

col_annotation=matrix(data=NA,nrow=21,ncol=2)
col_annotation[1:3,1]="grey80" #Mineral data
col_annotation[7:9,1]="grey80" #Mineral data
col_annotation[13:15,1]="grey80" #Mineral data
col_annotation[19:21,1]="grey80" #Mineral data

col_annotation[4:6,1]="grey20" #Mineral data
col_annotation[10:12,1]="grey20" #Mineral data
col_annotation[16:18,1]="grey20" #Mineral data

col_annotation[1:6,2]="yellow2"
col_annotation[7:12,2]="orange"
col_annotation[13:18,2]="Darkorange3"
col_annotation[19:21,2]="Darkred"

colnames(col_annotation) <- c("Horizon", "Treatment")
rownames(col_annotation)<-rownames(data2)





#16  CE  1	16
#103	GH	17	119
#68	GT	120	187
#18	PL	188	205

row_annotation=matrix(data=NA,nrow=1,ncol=205)
#row_annotation[1,1:16]="Navy"
#row_annotation[1,17:119]="Cornflowerblue"
#row_annotation[1,120:187]="Lightblue"
#row_annotation[1,188:205]="Slateblue"

row_annotation[1,1:16]="white"
row_annotation[1,17:119]="grey33"
row_annotation[1,120:187]="grey66"
row_annotation[1,188:205]="black"





rownames(row_annotation)=c("CAZy Class")
colnames(row_annotation)<-colnames(data2)




#Define custom dist and hclust functions for use with heatmaps
mydist=function(c) {vegdist(c,method="bray")}
myclust=function(c) {hclust(c,method="average")}

data2<-t(data2)
data3<-log10(data2+1)

#heatmap.3(data3, distfun=mydist,ColSideColors=column_annotation_all,margins=c(4,10),RowSideColors=row_annotation)
#heatmap.3(data3, col=brewer.pal(8,"Blues"),distfun=mydist,ColSideColors=column_annotation_all,margins=c(4,10),RowSideColors=row_annotation)

#heatmap.3(data3, col=brewer.pal(4,"Blues"),distfun=mydist,ColSideColors=column_annotation_all,margins=c(4,10),RowSideColors=row_annotation,breaks=c(0,1,2,3,4))

heatmap.3(data3, col=brewer.pal(8,"Blues"),distfun=mydist,ColSideColors=column_annotation_all,,RowSideColors=row_annotation,side.height.fraction=0.2,margins=c(8,14),cexRow=0.4
          ,xlab="Samples", ylab="CAZy families",keysize=1,KeyValueName="Hits per million reads",density.info="none",sepcol="black",NumColSideColors=2)





legend("topright",legend=c("Mineral","Organic","","OM0","OM1","OM2","OM3","","CE","GH","GT","PL")
       ,fill=c("grey80","grey20","White","Yellow2","orange","darkorange3","darkred","white","white","grey33","grey66","Black")
       , border="black", bty="o",  cex=0.8
       )

row_annotation[1,1:16]="white"
row_annotation[1,17:119]="grey33"
row_annotation[1,120:187]="grey66"
row_annotation[1,188:205]="black"

