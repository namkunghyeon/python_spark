from pyspark import SparkContext
sc = SparkContext("local","simple app")

a=['1','4','3','5']
a = sc.parallelize(a)
numAs = a.filter(lambda s: '1' in s).count()
numBs = a.filter(lambda s: '2' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
print a
print a.take(2)
