#usage
#R --no-save -f concatenate.cazy.results.R <outfile.csv>
#1	2     3   4   				5

#change this first, location of files
#myfolder = "/home/erick/tmp/"
#myfolder = "home/erick/blastsearch/trimmed.reads.vs.cazy.n.foly/round3/all/done/temp"
myfolder = "/home/erick/blastsearch/trimmed.reads.vs.cazy.n.foly/round3/all/done/temp"
print(myfolder)
args <- commandArgs() #read from arguments


#Create CAZy family list
GH = paste("GH", 1 : 132, sep = "")
GT = paste("GT", 1 : 94, sep = "")
CE = paste("CE", 1 : 16, sep = "")
PL = paste("PL", 1 : 22, sep = "")
AA = paste("AA", 1 : 10, sep = "")

CAZY = c(GH, GT, CE, PL, AA)

#read files in folder
#list_of_files=list.files("c:/r/temp",all.files=TRUE)

list_of_files = list.files(myfolder, all.files=FALSE)
print(list_of_files)

#list_of_files = list.files(getwd(), all.files = TRUE)
tempdim = length(list_of_files)
list_of_files = list_of_files[3 : tempdim]
print(list_of_files)

# Create empty matrix

result_matrix = matrix(nrow = length(CAZY), ncol = length(list_of_files), data = 0)

row.names(result_matrix) = CAZY
colnames(result_matrix) = list_of_files


# Open file
# Get first family
# Get family count
# Update results
# Go with file

counter = 1


while (counter <= length(list_of_files)){
filename = paste(myfolder,"/", list_of_files[counter], sep = "")    

#data = read.delim(file = filename, header = FALSE)
data = read.delim(file = filename, header = FALSE, skip =1 )    

counter2 = 1
while (counter2 <= nrow(data)){
#  family = data[counter2, 1]
  family = data[counter2, 2]
  family
# family_count = data[counter2, 2]
  family_count = data[counter2, 3]
  family_count
  result_matrix[family, counter] = family_count
  counter2 = counter2 + 1
}
print(counter)
counter = counter + 1  
}


fileout = args[5]

write.csv(result_matrix,fileout)







