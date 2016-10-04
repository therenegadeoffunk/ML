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
    # If only all cancer screening were so simple...
    if (size > .8) {
        malig <- 1
    } else {
        malig <- 0
    }
    param <- list(id, size, malig)
    return(param)
}

insert_data <- function(connection, parameters)
{
    query <- sprintf("INSERT INTO tumors VALUES ( '%s', %s, %s)",
                    parameters[1], parameters[2], parameters[3])
    resp <- dbGetQuery(con, query)
}

con <- setup()
param <- make_parameters()
insert_data(con, param)
print("All done!")
