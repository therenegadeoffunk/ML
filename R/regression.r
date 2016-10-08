#!/usr/bin/Rscript

require('RPostgreSQL')
require('ggplot2')

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

# TODO - l-l-l-logistic regression!

con <- setup()
d <- get_data(con)
# Lets plot it and take a look see
m = data.matrix(d)
png('plot.png')
qplot(m[,2], m[,3])
dbDisconnect(con)
print("Cowabunga!")
