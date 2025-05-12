
# Apache Spark / pyspark
# https://www.youtube.com/watch?v=QLQsW8VbTN4

"""
Spark is basically Pandas on steroids :)
- Distributed to many machines, and like Hadoop, does Map/Reduce
- Can use S3, HDFS etc as storage

Spark (originally written in Scala):
    - Distributed computing framework
    - Supports:
        - Scala
        - Java
        - Python
    - Spark SQL: SQL on Spark
    - Spark Streaming: streaming data processing (ie. Kafka/Kinesis etc)
    - Spark MLlib: machine learning

RDD: Resilient Distributed Dataset
    - Resilient: can be lost or corrupted (stored in memory by default)
    - Distributed: distributed across multiple nodes
    - Dataset: collection of data    
    - RDD is immutable
    - RDD is lazy: only executed when needed
    - RDD is fault tolerant: can recover from failures

"""

# .ipynb

# pip install pyspark
from pyspark import SparkContext as sc, RDD
# from pyspark import SparkConf, SQLContext

nums = list(range(0, 1000001))
nums_rdd:RDD = sc.parallelize(nums) # ParallelCollectionRDD
nums_range:RDD = sc.range(0, 100, 5).collect()
# nums_rdd.cache()
# nums_rdd.persist()
# nums_rdd

# nums_rdd.count()
# nums_rdd.countByKey()
# nums_rdd.countByValue()
# nums_rdd.combineByKey()
# nums_rdd.distinct()

# nums_rdd = nums_rdd.groupBy(lambda x: x % 2).collect()
# >>> sorted([(x, sorted(y)) for (x, y) in result])
# [(0, [2, 8]), (1, [1, 1, 3, 5])]
# nums_rdd = nums_rdd.groupBy(lambda x: x % 2).mapValues(list).collect()

# grouped = nums_rdd.groupByKey()
# grouped = grouped.map(lambda x: (x[0], list(x[1])))
# averaged = grouped.mapValues(lambda x: sum(x) / len(x))
# nums_rdd.groupWith()

# nums_rdd = nums_rdd.map(lambda x: x * 2)
# nums_rdd = nums_rdd.map(lambda x: (x, x * 2))         # tuple elements
# nums_rdd = nums_rdd.filter(lambda x: x[1] % 2 == 0)   # filtering by the tuple's second element
# flipped = nums_rdd.map(lambda x: (x[1], x[0]))        # flips items in the tuple
# nums_rdd = nums_rdd.flatMap(lambda x: [x, x * 2])
# nums_rdd.foreach(lambda x: print(x)
# nums_rdd.reduce(lambda x, y: x + y)
# nums_rdd.reduceByKey(lambda x, y: x + y).collect()
# nums_rdd.randomSplit([0.5, 0.5])

# nums_rdd.first()
# nums_rdd.collect()            -> List
# nums_rdd.collectAsMap()       -> Dict
# nums_rdd.take(5)              -> List
# nums_rdd.takeOrdered(5)       -> List
# nums_rdd.takeSample(False, 5)
# nums_rdd.top(5)               -> List

# nums_rdd.saveAsTextFile("output")
# nums_rdd.saveAsObjectFile("output")
# nums_rdd.saveAsSequenceFile("output")
# nums_rdd.saveAsNewAPIHadoopFile("output", "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat",
#                                  "org.apache.hadoop.io.IntWritable", "org.apache.hadoop.io.Text")




