from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Cluster-Test")

sc   = SparkContext(conf=conf)

logData = sc.textFile('/home/nkh/spark-2.0.0-bin-hadoop2.7/README.md')

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
