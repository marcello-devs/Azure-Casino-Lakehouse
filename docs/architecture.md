# Architecture

This project follows a Medallion Architecture pattern:

## Bronze Layer
- Raw CSV data ingested into Azure Data Lake
- Stored without transformation

## Silver Layer
- Data cleaned using Azure Databricks (PySpark)
- Data types corrected
- Stored as Parquet

## Gold Layer
- Aggregated analytics tables:
  - Daily revenue (GGR)
  - Player activity
  - Responsible gaming alerts

## Tools Used
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- PySpark
- Parquet format