# pkg/etl.py
import unittest

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import regexp_replace
from pyspark.testing.utils import assertDataFrameEqual

# Create a SparkSession
spark = SparkSession.builder.appName("Sample PySpark ETL").getOrCreate()

sample_data = [{"name": "John    D.", "age": 30},
  {"name": "Alice   G.", "age": 25},
  {"name": "Bob  T.", "age": 35},
  {"name": "Eve   A.", "age": 28}]

df = spark.createDataFrame(sample_data)

# Define DataFrame transformation function
def remove_extra_spaces(df, column_name):
    # Remove extra spaces from the specified column using regexp_replace
    df_transformed = df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

    return df_transformed