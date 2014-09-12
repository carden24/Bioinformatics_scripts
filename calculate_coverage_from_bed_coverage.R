#R --no-save -f <calculate.coverage.from.bed.coverage.R> <file.to.score.txt>#usage
#1    2       3 4          					5

args<-commandArgs()
data<-read.table(file = args[5],header = FALSE, sep = "\t")
fac<-levels(data$V1)

print(args[5])

#####1.separate contigs and print###########
c = 1
while (c <= nrow(as.data.frame(fac))){
subselection <- subset(data,data$V1 == fac[c])
contig = subselection[1, 1]
contig_length = subselection[1, 4]
weighted_coverage = (subselection$V2) * (subselection$V3)
weighted_coverage2 = (colSums(as.matrix(weighted_coverage))) / contig_length
result <- gsub("( )", "", paste(fac[c], "-", weighted_coverage2))
print(result)
c = c + 1
}


