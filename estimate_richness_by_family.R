# estimate_richness_by_family.R

# Usage
# R --no-save -f estimate_richness_by_family.R <outfile.csv>
# 1	2     3   4   				5

args <- commandArgs()

#setwd("~/blastsearch/trimmed.reads.vs.cazy.n.foly/round3/all2/done")
#data = read.delim("temp", header =TRUE, skip =2)
data <- read.delim(file = args[5], header = TRUE, skip = 2)



list_of_families = as.vector(unique(data$CAZYme_Family))
sample_name = as.data.frame(data[1,1])
names(sample_name)[1] = 'sample'

# create empty matrix with zeroes
output = matrix(data = 0, nrow = 1, ncol = 3)
names(output) = c('V1', 'V2', 'V3')

for(cazyme in list_of_families){
    data2 = subset (data, data$CAZYme_Family == cazyme)
    richness_result = length(unique(data2$subject_id))
    result = cbind (sample_name, cazyme, richness_result)
    names(result) = c('V1', 'V2', 'V3')
    names(output)
    result2 = rbind (output, result)
    output = result2
}

names(output) = c('sample', 'cazyme', 'richness_result')
output2 = output
output2 = output2[2:nrow(output2),]
fileout = paste(args[5], '.csv')
write.csv(output2, fileout, row.names = FALSE )
