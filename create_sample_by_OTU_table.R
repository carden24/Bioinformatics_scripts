#Use script like this
#R --no-save -f create.sample.by.OTU.table.R <file.to process> <output>
#1    2       3 4               		  5		6    

args <- commandArgs()
data <- read.csv(file = args[5], header = FALSE)

#data<-read.csv(file=file.choose(),header=FALSE) # read  csv file, no headers. Use this line if open from R gui


# get list of samples
samples = unique(data$V1)                                                                         
# get list of OTU
OTUs = unique(data$V2)                                                                            
# create empty matrix with zeroes
output = matrix(data = 0, nrow = length(samples), ncol = length(OTUs)) 
# Change names of rows to sample names
rownames(output)=samples                                                                        
# Change names of rows to OTU names
colnames(output)=OTUs                                                                           

 
#go through each line getting sample, otu and count
#then assign into matrix

total_rows=nrow(data)
counter=1


while (counter <= total_rows){
my_line = data[counter,]
da_sample = my_line[1,1]
da_OTU = my_line[1,2]
da_count = my_line[1,3]
output[da_sample,da_OTU] = da_count
message <- gsub("( )", "", paste("Processing ", counter, ",out of ", total_rows))
print(message)
counter = counter + 1
}

write.csv(output, file = args[6])

 

