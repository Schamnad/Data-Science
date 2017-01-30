library(ggplot2)
library(caret)
library(rpart)
library(randomForest)
library(e1071)

setwd("/media/sanjeed/Mine/OSDSM/Introduction to data science/datasci_course_materials/assignment5")

#Step 1:  Read and summarize the data
heisenberg <- read.csv("seaflow_21min.csv")
summary(heisenberg)

#Step2: Split the data into test and training sets
splitHeisenberg <- function(dataFrame) {
  dataIndex = createDataPartition(dataFrame$cell_id+dataFrame$file_id, p = 0.7, list = FALSE, times=1)
  train <- heisenberg[dataIndex,]
  test <- heisenberg[-dataIndex,]
  list(trainingSet=train, testSet=test)
}

dataSplit = splitHeisenberg(heisenberg)
training = dataSplit$trainingSet
test = dataSplit$testSet


# Question 3: mean time of training set
mean(training$time)

#Step3:Plot the data
plot = ggplot(training, aes(pe, chl_small))
plot + geom_point() + geom_point(aes(color = pop))

testPlot = ggplot(heisenberg, aes(pe, chl_small))
testPlot + geom_point() + geom_point(aes(color = pop))

#Step 4: Train a decision tree.
# Question 5: what populations, if any, is the tree *incapable* of measuring?
# (Hint: look for the one that's not listed.)
# Question 6: Verify there's a threshold on PE learned in the model.
# Question 7: Based on the tree, which variables appear most important
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
decision_tree <- rpart(fol, method = 'class', data = training)
print(decision_tree)

# Question 8: Decision tree prediction.
decision_pd <- predict(decision_tree, newdata = test, type ='class')
decision_result <- decision_pd == test$pop
summary(decision_result)

#Step 6: Build and evaluate a random forest.
rf_model <- randomForest(fol, data = training)
rf_pd <- predict(rf_model, newdata = test, type ='class')
decision_result <- rf_pd == test$pop
summary(decision_result)


# Question 10: which varibles appear most important in terms of gini
# impurity measure
importance(rf_model)

#Step 7: Train a support vector machine model and compare results.
svm_model <- svm(fol, data = training)
svm_pd <- predict(svm_model, newdata = test)
decision_result <- svm_pd == test$pop
summary(decision_result)

#Step 8: Construct confusion matrices
table(pred=decision_pd, true=test$pop)
table(pred=rf_pd, true=test$pop)
table(pred=svm_pd, true=test$pop)

#Step 9: Sanity check the data
# Question 13: We assumed variables were continuous.  One of them has a
# lot of clustering. 
plot(heisenberg$chl_big, heisenberg$chl_small)
plot(heisenberg$fsc_big, heisenberg$fsc_small)
plot(heisenberg$fsc_perp, heisenberg$pe)

# Question 14: Remove File 208 from the mix and run the SVM again.
# What's the change in accuracy
plot(heisenberg$chl_big, heisenberg$time)
dataset2 = subset(heisenberg, heisenberg$file_id != 208)
resample = splitHeisenberg(dataset2)
training_set = resample$training
test_set = resample$test

svm_model <- svm(fol, data = training_set)
svm_pd <- predict(svm_model, newdata=test_set)
svm_result <- svm_pd == test_set$pop
summary(svm_result)
table(pred=svm_pd, true= test_set$pop)