#!/usr/bin/Rscript

costFunction <- function(theta) {
    a <- nrow(X)
    b <- sigmoid(X%*%theta)
    J <- (1 / a) * sum((-Y * log(b)) - ((1 - Y) * log(1 - b)))
    return(J)
}
