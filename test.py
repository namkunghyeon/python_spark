from pyspark import SparkContext
sc = SparkContext("local","simple app")

a=['1','4','3','5']
a = sc.parallelize(a)

logData = sc.textFile('/home/nkh/spark-2.0.0-bin-hadoop2.7/README.md')

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

logData2 = sc.textFile('/home/odroid/Work/raw_data/ml-10M100K/ratings.dat')
rating1 = logData.filter(lambda s: '1' in s).count()
rating2 = logData.filter(lambda s: '2' in s).count()
print("Lines with rating 1: %i, lines with rating 2: %i" % (rating1, rating2))

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
print a
print a.take(2)
