#three_column_table_to_matrix.R

#usage
#R --no-save -f three_column_table_to_matrix.R <infile> <outfile.csv>
#0 1         2  3                              4   	5

library(reshape2)


# Read from arguments
args <- commandArgs() #read from arguments
print(args)
filein = args[6]
fileout = args[7]

#filein = file.choose()

data = read.delim(file = filein, header = FALSE)
head(data)
data2 = acast(data, V1 ~ V2, value.var = 'V3', fill = 0)
write.csv(data2, fileout)


