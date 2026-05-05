# Azure Casino Lakehouse

🚀 End to end Azure Data Engineering Pipeline using Medallion Architecture (Bronze → Silver → Gold)

This project simulates casino transactions and builds a scalable data pipeline using:
- Azure Data Factory (orchestration)
- Azure Data Lake Storage Gen2 (data lake)
- Azure Databricks (PySpark transformations)
- Parquet format for optimized analytics

## Key Outcomes

- Built a full ETL pipeline from raw data → analytics
- Implemented Bronze, Silver, Gold architecture
- Generated business metrics such as:
  - Daily Revenue (GGR)
  - Player activity tracking
  - Responsible gaming alerts

## Architecture

![Architecture](docs/screenshots/architecture.png)

## Data Orchestration (Azure Data Factory)

Pipeline execution:
![ADF Pipeline](docs/screenshots/adf_pipeline.png)

## Data Transformation (Azure Databricks)

PySpark transformations:
![Databricks](docs/screenshots/databricks_transform.png)

## Analytics Layer (Gold Tables)

Responsible Gaming Alerts:
![Responsible Gaming Alerts](docs/screenshots/gold_alerts.png)

Daily Revenue:
![Daily Revenue](docs/screenshots/gold_daily_revenue.png)

Player Activity:
![Player Activity](docs/screenshots/gold_player_activity.png)

## Data Pipeline

1. Generate mock casino data (Python + Faker)
2. Upload to Azure Data Lake (Bronze)
3. Use Azure Data Factory to orchestrate ingestion
4. Transform data in Databricks (Bronze → Silver)
5. Build analytics tables (Silver → Gold)

## Tech Stack

- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- PySpark
- Parquet

## Data Domains

- Players
- Bets
- Deposits
- Withdrawals
- Game sessions
- Bonuses
- Responsible-gaming alerts