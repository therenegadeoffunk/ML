// Basic script for testing stuff

val df = spark.read.format("csv").option("header", "true").load("test.csv")

df.sort()

df.first

System.exit(0)
