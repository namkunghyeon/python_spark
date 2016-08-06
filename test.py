from pyspark import SparkContext
sc = SparkContext("local","simple app")

a=['1','4','3','5']
a = sc.parallelize(a)

logData = sc.textFile('/home/odroid/Downloads/spark-2.0.0/README.md').cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
print a
print a.take(2)
