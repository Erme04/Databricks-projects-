from pyspark.sql.functions import as F
from pyspark.sql.types import IntegerType, StructType, StringType, IntegerType, Floatype, DoubleType, StructField, TimestampType, CurrentTimestamp, col, 
import pandas as pd
import geopangas as gpd 



df = spark.read.format("csv").option("header", "true").load("/FileStore/tables/StudentData.csv")