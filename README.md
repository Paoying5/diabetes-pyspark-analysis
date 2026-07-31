<h1 align="center">
🩺 Diabetes Data Analysis Using PySpark
</h1>

<p align="center">
A learning project focused on building a <strong>production-oriented data analytics workflow</strong> using <strong>Apache Spark (PySpark)</strong>, <strong>Docker</strong>, and <strong>Linux automation</strong>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PySpark](https://img.shields.io/badge/PySpark-3.x-E25A1C?logo=apachespark)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-Big%20Data-F26B3A?logo=apachespark)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Latest-2496ED?logo=docker)
![Linux](https://img.shields.io/badge/Linux-Bash-orange?logo=linux)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📖 Project Overview

This project is part of my journey to learn modern Data Engineering and Data Analytics using Apache Spark.

Instead of developing everything inside a single Jupyter Notebook, this repository gradually transforms notebook experiments into a structured, production-style Python project.

The project emphasizes:

- Production-ready project organization
- PySpark data processing
- Docker-based development
- Linux automation with Bash
- Git & GitHub workflow
- Software Engineering best practices

---

# 🎯 Project Goals

The primary goals of this project are:

- Learn Apache Spark with PySpark
- Build reusable data processing modules
- Practice Data Engineering workflows
- Develop clean project architecture
- Containerize the development environment
- Prepare a portfolio-quality GitHub repository

---

# 📊 Dataset

Current dataset:

- Diabetes Health Indicators Dataset

The dataset will be processed using PySpark DataFrame APIs.

Future improvements include:

- Data validation
- Schema management
- Feature engineering
- Data quality checking

---

# 🏗 Project Architecture

```
Raw Dataset

      │

      ▼

Load Data

      │

      ▼

Preprocessing

      │

      ▼

Exploratory Data Analysis

      │

      ▼

Feature Engineering

      │

      ▼

Machine Learning

      │

      ▼

Evaluation

      │

      ▼

Reports & Visualization
```

---

# 📂 Project Structure

```text
diabetes-pyspark-analysis/

├── data/
│   ├── raw/
│   └── processed/
│
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
│
├── notebook/
│   └── 01_eda.ipynb
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── scripts/
│   ├── build.sh
│   ├── clean.sh
│   ├── init.sh
│   ├── run.sh
│   └── stop.sh
│
├── src/
│   ├── analysis.py
│   ├── config.py
│   ├── load_data.py
│   ├── preprocess.py
│   ├── utils.py
│   └── visualization.py
│
├── tests/
│
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| Apache Spark (PySpark) | Distributed Data Processing |
| Pandas | Data Inspection |
| Matplotlib | Visualization |
| Docker | Containerization |
| Docker Compose | Development Environment |
| Bash Script | Development Automation |
| Git | Version Control |
| GitHub Actions | Continuous Integration |

---

# 🐳 Docker Workflow

The project is designed to run inside Docker containers.

Development workflow:

```
Host Machine

      │

docker compose

      │

      ▼

Python Container

      │

      ▼

Apache Spark

      │

      ▼

Notebook / Source Code
```

---

# 🚀 Getting Started

## Clone Repository

### HTTPS

```bash
git clone https://github.com/Paoying5/diabetes-pyspark-analysis.git
```

### SSH

```bash
git clone git@github.com:Paoying5/diabetes-pyspark-analysis.git
```

---

## Enter Project

```bash
cd diabetes-pyspark-analysis
```

---

## Build Containers

```bash
docker compose build
```

---

## Start Containers

```bash
docker compose up -d
```

---

# 📜 Automation Scripts

Current scripts:

```
scripts/

build.sh
clean.sh
init.sh
run.sh
stop.sh
```

These scripts will gradually automate the development workflow, reducing repetitive Docker commands.

---

# 📈 Learning Progress

Completed:

- ✅ Project initialization
- ✅ Git & GitHub repository
- ✅ Docker project structure
- ✅ Linux project organization
- ✅ Bash automation structure

Currently Learning:

- 🔄 Apache Spark
- 🔄 PySpark DataFrame
- 🔄 Data preprocessing
- 🔄 Data analysis

Future Goals:

- Feature Engineering
- Machine Learning Pipeline
- MLflow
- Unit Testing
- Data Validation
- Logging
- Configuration Management
- CI/CD Pipeline
- Production Deployment

---

# 🎯 Learning Objectives

This project focuses on learning:

- Apache Spark
- PySpark
- Data Analytics
- Data Engineering
- Docker Workflow
- Linux Development
- Software Project Organization
- Production-oriented Python Development

---

# 👨‍💻 Author

**Truong Pham**

Final-year Information Technology Student

GitHub:

https://github.com/Paoying5

---

# ⭐ Notes

This repository is built primarily for learning purposes.

The goal is not only to analyze a diabetes dataset, but also to learn how to organize a real-world PySpark project from scratch using modern software engineering practices.

Every module will be developed incrementally, documented, and continuously improved throughout the learning journey.