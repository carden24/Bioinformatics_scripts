# create copy number data for 4 samples for 3 genes 
data<-data.frame(
  gene=sample(c("geneA","geneB","geneC"),10000,replace=TRUE),
  sampleName=sample(c("sample1","sample2","sample3","sample4"),10000,replace=TRUE),
  position=round(runif(n=10000,min=0,max=5000),digits=0),
  copy_number=rnorm(n=10000,mean=2,sd=0.1)
)

# create copy number gain in sample 4 gene A
data[data$gene=="geneA" & data$sampleName=="sample1",4]<-rnorm(
  mean=3,
  sd=0.1,
  n=length(
    data[data$gene=="geneA" & data$sampleName=="sample1",4]
  )
)

# and a focal lost at sample 3, gene B
data[data$gene=="geneB" & data$sampleName=="sample3" & data$position > 2000 & data$position < 4000,4]<-rnorm(
  mean=1,
  sd=0.1,
  n=length(
    data[data$gene=="geneB" & data$sampleName=="sample3" & data$position > 2000 & data$position < 4000,4]
  )
)

# plot copy numbers for all genes for all samples
library(ggplot2)
plot<-ggplot(data) + #add basic layer
  geom_point(aes(x=position,y=copy_number)) + #add copy number points to plot
  facet_wrap(gene ~ sampleName) + # seperate the CN numbers for each gene and for each sample
  scale_y_continuous(limits=c(0,4)) # set y-limits

# and save plot to file
png("copy_numbers.png",1000,1000)
print(plot)
dev.off()