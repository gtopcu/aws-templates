
# https://www.youtube.com/watch?v=3-pnWVWyH-s

from pandas import DataFrame #, read_csv, read_excel, read_json, read_html, read_clipboard

# pip install pyspark
# from pyspark import SparkContext as sc
from pyspark import RDD
# from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as sf
from pyspark.sql.functions import udf #
from pyspark.sql.types import IntegerType#, DecimalType, StringType, StructType, StructField, ArrayType, MapType, DateType, TimestampType
# from pyspark.sql.window import Window

# .ipynb

# conf = SparkConf().setMaster("local").setAppName("SparkSQL")
spark:SparkSession = SparkSession.builder.appName("SparkSQL").getOrCreate()
spark.conf.set("spark.sql.repl.eagerEval.enabled", "true") # format tables
# spark.sparkContext.setLogLevel("ERROR")
# spark.conf.set("spark.sql.shuffle.partitions", "5")
# spark.conf.set("spark.sql.session.timeZone", "UTC")
# spark.conf.set("spark.sql.execution.arrow.enabled", "true")
# spark.conf.set("spark.sql.execution.arrow.fallback.enabled", "true")
# spark.conf.set("spark.sql.execution.arrow.maxRecordsPerBatch", "10000")
 
# sc = spark.sparkContext
# nums = list(range(0, 1000001))
# nums_rdd:RDD = sc.parallelize(nums) # ParallelCollectionRDD

# spark.readStream
# spark.read.parquet("data/parquet")
# spark.read.orc("data/orc")
# spark.read.json("data/json")
# spark.read.jdbc("jdbc:postgresql://localhost:5432/postgres", "public.users")
# spark.read.text("data/text")
# spark.read.table("public.users")
# df = spark.read.csv("data.csv")
# df = spark.read.csv("data.csv", header=True, inferSchema=True, sep=",")
# df = spark.read.csv("data.csv").toPandas()
# spark.read.schema("name STRING, age INT").csv("data/csv").show()
# spark.read.format("csv").option("header", "true").load("data/csv").show()
# spark.read.format("csv").option("header", "true").load("data/csv")

# Read CSV into dataframe
# df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
df = spark.read.csv("data.csv", header=True, inferSchema=True, sep=",")
df.describe()
df.dtypes
df.printSchema()
df.select("*")#.show(10)
df.where((df.Age > 30) & (df.Type == 1) & df.Job.isin(["student", "doctor"])).limit(5)
df.agg({"Age": "max", "Salary": "min"})
df.agg(sf.min(df.age))
df.groupby("Age").count().orderBy(sf.desc("count"), ascending=False).limit(5)
df.groupby("Age").agg({"Fare": "avg"})

def round_float_down(x:float):
    return int(x)
round_float_down_udf = udf(round_float_down, IntegerType())
df.select(round_float_down_udf("Fare").alias("Fare"))


# SQL
#df.createTempView("people")
df.createOrReplaceTempView("people")
# df2 = df.filter(df.age > 3)
# df3 = spark.sql("SELECT * FROM people")
# >>> sorted(df3.collect()) == sorted(df2.collect())
# True
# >>> spark.catalog.dropTempView("people")
# True
