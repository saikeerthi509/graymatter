# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

df_01=spark.read.csv("/FileStore/gmde/googleplaystore.csv")


# COMMAND ----------

df_01.show()

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01=spark.read.option("header",True).csv("/FileStore/gmde/googleplaystore.csv")

# COMMAND ----------

df_01.printSchema

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_01=spark.read.option("header",True).option("inferschema",True).csv("/FileStore/gmde/googleplaystore.csv")

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_01.printSchema

# COMMAND ----------



# COMMAND ----------





sch=StructType().add("App",StringType(),True)\
    .add("Category",StringType(),True)\
    .add("Rating",DoubleType(),True)\
    .add("Reviews",IntegerType(),True)\
    .add("Size",StringType(),True)\
    .add("Installs",StringType(),True)\
    .add("Type",StringType(),True)\
    .add("Price",StringType(),True)\
    .add("Content Rating",StringType(),True)\
    .add("Genres",StringType(),True)\
    .add("Last Updated",StringType(),True)\
    .add("Current Ver",StringType(),True)\
    .add("Android Ver",StringType(),True)


# COMMAND ----------

df_01=spark.read.option("header",True).schema(sch).csv("/FileStore/gmde/googleplaystore.csv")

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01=df_01.withColumn("appscore",col("Rating"))

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01=df_01.withColumn("APPcateg",concat(col("APP")*col("Category")))

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01=df_01.withColumn("owner",lit("keerthi"))

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_01=df_01.withColumn("appscore",col("Rating")).withColumn("APPcateg",concat(col("APP")*col("Category"))).withColumn("owner",lit("keerthi"))

# COMMAND ----------

df_01.display()

# COMMAND ----------

dfmain=df_01

# COMMAND ----------

df_01=df_01.withColumnRenamed("App","Appname")

# COMMAND ----------

df_01.display()

# COMMAND ----------

df_02.printSchema()

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_01.printSchema()

# COMMAND ----------

df_03=spark.read.option("header",True).schema(sch).csv("/FileStore/gmde/googleplaystore.csv")

# COMMAND ----------

df_03=df_03.printSchema()

# COMMAND ----------

df_04=df_03.selectExpr('cast(Rating as integer) as new_rate')

# COMMAND ----------

df=df_03.orderBy(col("Rating").desc())

# COMMAND ----------

df_01=df_01.orderBy(col("Rating").desc())

# COMMAND ----------

df1=df_01.distinct()
df1.display()

# COMMAND ----------

df_001=spark.read.option("header",True).schema(sch).csv("/FileStore/gmde/googleplaystore.csv")

# COMMAND ----------

dropdf_001=df_001.dropDuplicates(["Category","Installs"])

# COMMAND ----------

dropdf_001.display()

# COMMAND ----------

newdf_001 = df_001.withColumn("Rating",when(col("Rating")<2,"poor")\
                .when((col("Rating")>2) & (col('Rating')<4,"avg"))\
                .when(col("Rating")>4,"good").otherwise(lit("notrated") ))))

# COMMAND ----------

df_001.printSchema()

# COMMAND ----------

sch_user=StructType().add("App",StringType(),True)\
    .add("Translated_Review",StringType(),True)\
    .add("Sentiment",StringType(),True)\
    .add("Sentiment_Polarity",DoubleType(),True)\
    .add("Sentiment_Subjectivity",DoubleType(),True)
    

# COMMAND ----------

df_user=spark.read.option("header",True).schema(sch_user).csv("/FileStore/gmde/googleplaystore_user_reviews.csv")

# COMMAND ----------

df_user.display()

# COMMAND ----------

final_df=df_001.join(df_user,df_001.App==df_user.App,how="left").select(df_001['*'],df_user['Sentiment'])

# COMMAND ----------

final_df.display()

# COMMAND ----------

df_grp=final_df.groupBy("App").sum("Rating")


# COMMAND ----------

df_grp.display()
