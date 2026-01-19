# Databricks-projects-

df=(
    spark.read.option("header", "true")
    .option("inferSchema","true")
    .csv("/Volumes/dev_project/bronze/source_systems/source_crm/cust_info.csv")
)
df.display()