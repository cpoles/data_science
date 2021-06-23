## Loading libraries ----
library(caret)
library(tidyverse)

i# attach to the environment
data("iris")
# rename the dataset
iris_ds <- iris

## Create validation dataset ----

# list of 80% of rows of the original dataset for training
validation_index <- createDataPartition(iris_ds$Species, p=0.80, list=FALSE)
# select 20% of the data for validation
validation <- iris_ds[-validation_index, ]
# select the remaining 80% for training and testing the models
iris_ds <- iris_ds[validation_index, ] # overwrite original

## Summarize dataset ----

# dimensions of the dataset
dim(iris_ds)

# list types for each attribute
sapply(iris_ds, class)

# peek at the data
head(iris_ds)

# list the levels of the Species class
levels(iris_ds$Species)

# there are 3 labels/levels/categories -> (multinomial classification)

## Class Distribution ----
# Descriptive Stats
summary(iris_ds)

## Visualise Dataset ----
# split input and output
x <- iris_ds[, 1:4]
y <- iris_ds[, 5]

## Univariate plots

# boxplots for each variable
par(mfrow=c(1,4))

for (i in 1:4) {
  boxplot(x[, i], main=names(iris)[i])
}

# scatterplot matrix for each variable
featurePlot(x = x, y = y, plot = "ellipse")

# boxplots for each variable
featurePlot(x = x, y = y, plot = "box")

# density plots for each attribute by class value
scales <- list(x = list(relation="free"), y = list(relation = "free"))
featurePlot(x = x, y = y, plot = "density", scales = scales)

## Evaluate Algorithms ----

# run algorithms using 10-fold cross validation

