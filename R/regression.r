#!/usr/bin/Rscript

require('RPostgreSQL')

setup <- function()
{
    drv <- dbDriver('PostgreSQL')
    con <- dbConnect(drv, user='postgres', dbname='cancer')
    return(con)
}

# TODO - Needs to select the data, shape it, then do logistic regression!

con <- setup()
# DO STUFF
dbDisconnect(con)
print("Cowabunga!")
