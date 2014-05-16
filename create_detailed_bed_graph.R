#R --no-save -f create.detailed.bed.graph.R <graph.file> <window size>#usage
#1    2       3 4                           5             6

args <- commandArgs() #read from arguments
data <- read.delim(file = args[5], header = FALSE)
head(data)

window_size = as.integer(args[6])
print(window_size)

unique_list = as.data.frame(unique(data$V1))


counter = 1
maxx = nrow(unique_list)
while (counter <= maxx){
  data2 = subset(data, data$V1 == unique_list[1, counter])  
  genome_size = data2[nrow(data2), 3]
  new = data.frame(cbind(Replicon = unique_list[1, counter], Position = 1 : genome_size, Coverage = 0))
  counter2 = 1
  while (counter2 <= length(data2)){
    line = data2[counter2, ]
    coord_start = (line$V2) + 1
    coord_end = (line$V3)
    coverage = (line$V4)
    new[coord_start : coord_end, 2] = coverage
    counter2 = counter2 + 1
    new$Replicon = unique_list[1, counter]
    }
  counter3 = 1
  while(counter3 <= genome_size){
    mystart = counter3
    myend = counter3 + window_size - 1
    if (myend > genome_size){
      myend = genome_size           
    }
    #print(gsub("( )", "", paste(mystart,"\t",myend,"\t",mean(new[mystart:myend,2]))))
    
    
    out = matrix(ncol = 3, nrow = 1)
    out[1, 1] = mystart
    out[1, 2] = myend
    out[1, 3] = mean(new[mystart : myend, 2])
    file_out <- gsub("( )", "", paste(args[5], "_", unique_list[1, counter], ".csv"))
    write.csv(out, file_out, append = TRUE)
    
    counter3 = counter3 + window_size
  }
  
  counter = counter + 1
}