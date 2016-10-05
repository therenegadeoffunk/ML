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
    df <- dbGetQuery(con, 'SELECT * FROM tumors')
    return(df)
}

# TODO - l-l-l-logistic regression!

con <- setup()
df <- get_data(con)
# Lets plot it and take a look see
m = data.matrix(df)
png('plot.png')
qplot(m[,2], m[,3])
dbDisconnect(con)
print("Cowabunga!")
