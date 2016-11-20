getwd()

#setwd("/home/sreedhar/Sem5/DAProject/student") # Set path to the file

list.files()

math <- read.csv2("student-por.csv")

#studytime <- math$studytime

#traveltime <- math$traveltime

head(math)

View(math)

cor.test(math$G1,math$G2)

library(ggplot2)

ggplot(aes(x = math$studytime,math$studytime),data = math ) + geom_abline() + geom_point()

cor.test(math$traveltime,math$studytime)

indexes = sample(1:nrow(math), size=0.2*nrow(math))

test = math[indexes,]

train = math[-indexes,]

nrow(test)
nrow(train)

math_mod <- math[,30:33]

# ------------------------------ CLUSTERING (Looking For patterns using KMEANS) --------------------

clusters <- kmeans(math_mod,4)

student_clusters <- clusters

student_clusters$cluster <- as.factor(student_clusters$cluster)

new_math <- cbind(math_mod,ClusterNum = student_clusters$cluster)


View(new_math)

library(ggplot2)


ggplot(aes(x = new_math$ClusterNum , y = new_math$G1),data = new_math) + geom_point() + xlab("Cluster Label ") + ylab("Final Student Score")

ggplot(aes(x = new_math$ClusterNum , y = new_math$absences),data = new_math) + geom_point() + xlab("Cluster Label ") + ylab("Student Absentees")

ggplot(aes(x = math$health,y = math$G3),data = math) + geom_point() + xlab("Health ") + ylab("Final Student Score")

# -------------------------------------------------------------------------------------------------------

#data <- new_math[,1:4]

data <- math[,24:33] # Selecting Appropriate Attributes

#data <- cbind(data,studytime)

#data <- cbind(data,traveltime)

# -------------------- Creating training and test set ---------

index <- sample(1:nrow(data),round(0.75*nrow(data)))
train <- data[index,]
test <- data[-index,]

# ----------------------------------------------------------

# ---------------- Linear Model Creation and Evaluation -------

lm.fit <- glm(G3~., data=train)

summary(lm.fit)

pr.lm <- predict(lm.fit,test)

MSE.lm <- sum((pr.lm - test$G3)^2)/nrow(test)

print(MSE.lm)

# Using mean squared error to estimate how far away our estimates are

maxs <- apply(data, 2, max) 
mins <- apply(data, 2, min)

scaled <- as.data.frame(scale(data, center = mins, scale = maxs - mins))

train_ <- scaled[index,]
test_ <- scaled[-index,]

# -------------------------------------------------------

# Neural Network Evaluation ----------------------------------------

#install.packages("neuralnet")
library(neuralnet)
n <- names(train_)
f <- as.formula(paste("G3 ~", paste(n[!n %in% "G3"], collapse = " + ")))
nn <- neuralnet(f,data=train_,hidden=c(3,5),linear.output=T,rep = 1)

plot(nn) # Plotting the neural network

pr.nn <- compute(nn,test_[,1:9])

pr.nn_ <- pr.nn$net.result*(max(data$G3)-min(data$G3))+min(data$G3)
test.r <- (test_$G3)*(max(data$G3)-min(data$G3))+min(data$G3)

MSE.nn <- sum((test.r - pr.nn_)^2)/nrow(test_)

print(paste(sqrt(MSE.lm),sqrt(MSE.nn)))

par(mfrow=c(1,2))

# ------------------------------------------------------------------

# -------------------------------------------------- Visualisation -----------------

plot(test$G3,pr.nn_,col='red',main='Real vs predicted NN',xlab = "Final Marks(Real)",ylab = "Final Marks Predicted",pch=18,cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend='NN',pch=18,col='red', bty='n')

plot(test$G3,pr.lm,col='blue',main='Real vs predicted LM',xlab = "Final Marks(Real)",ylab = "Final Marks Predicted",pch=18, cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend='LM',pch=18,col='blue', bty='n', cex=.95)

# Real vs Predicted NN

plot(test$G3,pr.nn_,col='red',main='Real vs predicted NN',pch=18,cex=0.7)
points(test$G3,pr.lm,col='blue',pch=18,cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend=c('NN','LM'),pch=18,col=c('red','blue'))

# -------------------------------------------------------------------------------------------

