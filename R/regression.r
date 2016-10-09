#!/usr/bin/Rscript

require('RPostgreSQL')

setup <- function()
{
    drv <- dbDriver('PostgreSQL')
    con <- dbConnect(drv, user='postgres', dbname='cancer')
    return(con)
}

get_data <- function(con)
{
    d <- dbGetQuery(con, 'SELECT * FROM tumors')
    return(d)
}

# Connect to our postgres database

con <- setup()

# Do a select query to get the data
d <- get_data(con)

# Lets make a simple plot, add some labels, and save it to a png file
png('plot.png')
plot(d[,2], d[,3], xlab="Tumor Size", ylab="Malignancy", main="Tumor Malignancy from Size")

# Now we figure out the decision boundary based on the data 
pre = glm(formula = malignant ~ size, family=binomial(link='logit'),data=d)

# Now we add it to the graph
curve(predict(pre, data.frame(size=x), type='resp'), add=TRUE)

# And we're done. Disconnect from the database, say 'cowabunga', go home.
dbDisconnect(con)
print("Cowabunga!")
