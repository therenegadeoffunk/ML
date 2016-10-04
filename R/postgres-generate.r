#!/usr/bin/Rscript

require('RPostgreSQL')
require('random')

setup <- function()
{
    drv <- dbDriver('PostgreSQL')
    con <- dbConnect(drv, user='postgres', dbname='cancer')
    return(con)
}

make_parameters <- function()
{
    id <- randomStrings(1, len=20)
    size <- runif(1)
    # Need some method for deciding malignancy based on size
}

insert_data -< function(connection, parameters)
{
    resp <- dbGetQuery(con, "SELECT * FROM tumors")
}

con <- setup()
param <- make_parameters()
insert_data(con, param)
print("All done!")
