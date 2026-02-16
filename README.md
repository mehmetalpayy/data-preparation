<h1 align="center"><strong>Data Preparation Pipeline with Hydra, Dask, and DVC</strong></h1>

## Overview

Welcome to the **data-preparation** repository. This project provides a configurable data processing pipeline that reads raw datasets, standardizes their schema, and outputs a unified dataset using Dask. Configuration is managed via Hydra and Pydantic, and raw data can be versioned and retrieved with DVC.

## Task Description

The objective of this project is to create a repeatable data-preparation workflow for text classification datasets. The pipeline loads raw data, splits it into train/dev/test sets, validates required columns, and merges multiple datasets into a single standardized dataframe.

### Requirements

- Load raw datasets from a local directory (optionally retrieved from a DVC remote).
- Normalize each dataset into a common schema: `text`, `label`, `split`, `dataset_name`.
- Produce consistent train/dev/test splits and validate split names.
- Support multiple datasets via a dataset reader manager.

## Repository Structure

This repository contains the following key files and directories:

1. **`mehmet/process_data.py`**: Entry point for the data-processing pipeline. Loads the Hydra config, instantiates dataset readers, reads data, and prints a preview.
2. **`mehmet/data_processing/dataset_readers.py`**: Abstract dataset reader and concrete implementation for GHC. Includes splitting and validation logic.
3. **`mehmet/configs/`**: Hydra configs that define dataset readers, data locations, and runtime settings.
4. **`mehmet/config_schemas/`**: Pydantic dataclass schemas for strong configuration validation.
5. **`mehmet/utils/`**: Utility functions for config loading, DVC data retrieval, AWS Secrets Manager access, and shell execution.
6. **`data/raw/`**: Raw dataset files (tracked via DVC in `data/raw.dvc`).
7. **`docker/`** and **`docker-compose.yaml`**: Containerized environment for reproducible runs.
8. **`Makefile`**: Common tasks for building, running, linting, and testing in Docker.
9. **`notebooks/`**: EDA notebooks for dataset exploration.

## Installation and Setup

You can run the project locally or inside Docker.

1. **Clone the Repository**:

```bash
git clone https://github.com/mehmetalpayy/data-preparation.git
cd data-preparation
```

2. **Local Setup (Poetry)**:

```bash
python3 -m pip install poetry
poetry install
```

3. **Run the Data Processing Script (Local)**:

```bash
python mehmet/process_data.py
```

4. **Docker Setup**:

```bash
make build
make up
```

5. **Run the Data Processing Script (Docker)**:

```bash
make process-data
```

## Configuration

The pipeline is configured through Hydra using `mehmet/configs/data_processing_config.yaml`. Key settings include:

- `version`: DVC revision for raw data retrieval.
- `data_local_save_dir`: Local path for raw datasets.
- `dvc_remote_repo` and `dvc_data_folder`: DVC source location.
- `dataset_reader_manager`: Set of dataset readers to load and merge.

Dataset readers are defined under `mehmet/configs/dataset_reader_manager/`. Each reader specifies the dataset path, name, and split behavior. For example, the GHC reader reads `ghc_train.tsv` and `ghc_test.tsv`, creates labels, and splits a dev set from the train data.

## Design and Engineering Decisions

- **Hydra + Pydantic**: Configuration is strongly typed and validated, making it easier to extend and safer to run.
- **Dask DataFrames**: Used to support large datasets and parallel processing.
- **Dataset Reader Abstraction**: Each dataset implements a common interface, ensuring consistent output and allowing easy expansion.
- **DVC Integration**: Raw data can be versioned and fetched reproducibly using DVC.
- **Docker-First Workflow**: A Docker environment provides consistent dependencies and reproducible execution.

## Limitations and Future Work

- **Single Reader in Default Config**: The default configuration currently enables only the GHC reader. Additional datasets can be added to the reader manager config.
- **Limited Output Persistence**: The current pipeline prints a preview and does not persist processed data. Adding a write step to store cleaned datasets (e.g., Parquet) would improve usability.
- **Optional Data Retrieval**: DVC retrieval is present but commented in `mehmet/process_data.py`. A CLI flag or config toggle would improve the workflow.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications and commit them.
4. Submit a pull request with a detailed description of the changes.

## Contact

For any questions or feedback, please contact me at iletisimehmetalpay@gmail.com.

---

Thank you for visiting the data-preparation repository. I hope you find the project useful and informative!
