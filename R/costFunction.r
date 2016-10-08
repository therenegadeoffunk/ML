#!/usr/bin/Rscript

J <- function(theta) {
    a <- nrow(X)
    b <- sigmoid(X%*%theta)
    z <- (1 / a) * sum((-Y * log(b)) - ((1 - Y) * log(1 - b)))
    return(z)
}
