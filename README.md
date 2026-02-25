# 📊 Airflow + dbt + PostgreSQL Project

This project demonstrates how to build a modern **data pipeline** using:

- **Apache Airflow** — workflow orchestration  
- **dbt (Data Build Tool)** — data transformation and modeling  
- **PostgreSQL** — data warehouse / database  
- **Docker & Docker Compose** — containerized environment  

The goal of this project is to implement an automated **ELT pipeline** that:

1. 📥 Extracts data  
2. 🗄 Loads data into PostgreSQL  
3. 🔄 Transforms data using dbt  
4. ⚙ Orchestrates everything using Airflow  

---

## 🚀 Tech Stack

- Python  
- Apache Airflow  
- dbt  
- PostgreSQL  
- Docker & Docker Compose  
- Bash / Shell  

---
        +------------+
        |   Data     |
        |  Source    |
        +------------+
               ↓
        +------------+
        | PostgreSQL |
        |   (Raw)    |
        +------------+
               ↓
        +------------+
        |    dbt     |
        | Transform  |
        +------------+
               ↓
        +------------+
        | PostgreSQL |
        |   (Mart)   |
        +------------+
               ↑
        +------------+
        |  Airflow   |
        | Orchestrator|
        +------------+

---

## ✅ Best Practices Applied

- Containerized environment with Docker  
- Separation of concerns (orchestration vs transformation)  
- Layered modeling approach (staging → marts)  
- Environment-based configuration  
- Version control with Git  
- Data quality testing with dbt  
