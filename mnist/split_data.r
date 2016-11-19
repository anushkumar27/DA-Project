stu <- read.table('student-por-mod-mod.csv', sep=',', header=T)

stu$gp <- runif(dim(stu)[1])

# famrel freetime goout Dalc Walc health absences G1 G2 G3

test_set <- subset(stu,  stu$gp <= 0.3)
training_set <- subset(stu, stu$gp > 0.3)

test_set$gp <- NULL
training_set$gp <- NULL

#colnames(test_set)
#rownames(test_set)

write.csv(training_set, file = "stu-por-train.csv", row.names=FALSE)
write.csv(test_set, file="stu-por-test.csv", row.names=FALSE)
