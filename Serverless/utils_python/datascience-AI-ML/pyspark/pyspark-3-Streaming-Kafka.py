
from pyspark import DataStreamReader
from pyspark.sql import SparkSession


spark:SparkSession = SparkSession.builder.appName("SparkStreaming").getOrCreate()
# spark.readStream.format("socket").option("host","localhost").option("port","9999").load().printSchema()

stream:DataStreamReader = spark.readStream.format("kafka") \
                    .option("kafka.bootstrap.servers", "localhost:9092") \
                    .option("kafka.group.id", "testGroup") \
                    .option("subscribe", "testTopic") \
                    .option("startingOffsets", "earliest") \
                    .option("endingOffsets", "latest") \
                    .option("failOnDataLoss", "false") \
                    .option("maxOffsetsPerTrigger", "10") \
                    .option("checkpointLocation", "checkpoint") \
                    .option("kafka.auto.offset.reset", "earliest") \
                    .option("kafka.enable.auto.commit", "false") \
                    .option("kafka.max.poll.records", "10") \
                    .option("kafka.session.timeout.ms", "60000") \
                    .option("kafka.request.timeout.ms", "60000") \
                    .option("kafka.poll.timeout.ms", "60000") \
                    .option("kafka.fetch.min.bytes", "1") \
                    .option("kafka.fetch.max.wait.ms", "100") \
                    .option("kafka.max.partition.fetch.bytes", "1") \
                    .load()
                    # .load("kafka://localhost:9092/testTopic")
                    
stream.printSchema()
stream.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
stream.select("*").limit(5).show(truncate=False)
stream.writeStream.format("console").option("truncate", "false").start().awaitTermination()
# spark.stop()
