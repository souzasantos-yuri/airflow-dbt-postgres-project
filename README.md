# 📊 Airflow + dbt + PostgreSQL Project

Pipeline ELT moderno que extrai e carrega dados no PostgreSQL, transforma com dbt e orquestra tudo via Apache Airflow — ambiente totalmente containerizado com Docker.

---

## 🎯 Objetivo

Implementar um pipeline ELT automatizado seguindo uma abordagem em camadas (staging → marts), com separação clara entre orquestração (Airflow) e transformação (dbt), aplicando boas práticas de engenharia de dados.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Apache Airflow | Orquestração do pipeline |
| dbt | Transformação e modelagem dos dados |
| PostgreSQL | Data warehouse |
| Docker / Docker Compose | Infraestrutura containerizada |

---

## 🗂️ Estrutura

```
airflow-dbt-postgres-project/
└── weather-data-project/
    ├── dags/               # DAGs do Airflow
    ├── dbt/
    │   ├── models/
    │   │   ├── staging/    # Modelos de staging
    │   │   └── marts/      # Modelos finais
    │   └── profiles.yml
    └── docker-compose.yaml
```

---
