#!/usr/bin/Rscript

require('RPostgreSQL')
require('random')

args <- commandArgs(trailingOnly=TRUE)

if (length(args)==0) {
    print('Gonna need at least one argument Jim laddy')
    stop()
} else {
    num <- strtoi(args[1])
}

stringlist <- randomStrings(num, len=20)

setup <- function()
{
    drv <- dbDriver('PostgreSQL')
    con <- dbConnect(drv, user='postgres', dbname='cancer')
    return(con)
}

make_parameters <- function(astring)
{
    id <- astring
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
for (s in stringlist) {
    param <- make_parameters(s)
    insert_data(con, param)
}
dbDisconnect(con)
print("All done!")
