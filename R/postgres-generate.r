#!/usr/bin/Rscript

require('RPostgreSQL')

testFunc <- function()
{
    drv <- dbDriver('PostgreSQL')
    con <- dbConnect(drv, user='postgres', dbname='cancer')
    resp <- dbGetQuery(con, "SELECT * FROM tumors")
    print(resp)
    dbDisconnect(con)
    dbUnloadDriver(drv)
}

testFunc()
