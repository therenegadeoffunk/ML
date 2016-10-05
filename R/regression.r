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
    df <- dbGetQuery(con, 'SELECT * FROM tumors')
    return(df)
}

# TODO - Needs to select the data, shape it, then do logistic regression!

con <- setup()
data <- get_data(con)
# Quick test
dbDisconnect(con)
print("Cowabunga!")
