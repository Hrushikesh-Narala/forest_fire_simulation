# Forest Fire Simulation using AI/ML

## Project Overview
This project aims to simulate and predict forest fire initiation, spread, and containment in Indian forests using AI/ML techniques and satellite plus meteorological data.

## Directory Structure

- `data/` - Raw and processed data
- `notebooks/` - Jupyter notebooks for EDA and prototyping
- `src/` - Source code (data processing, models, utils)
    - `data_ingest.py` - Data download and ingestion
    - `preprocess.py` - Data cleaning and preprocessing
    - `model.py` - ML/DL models for fire prediction
    - `visualize.py` - Visualization utilities
- `requirements.txt` - Python dependencies
- `main.py` - Entry point for running simulations

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download data using scripts in `src/data_ingest.py`.
3. Run simulations using `main.py`.

## Data Sources
- NASA FIRMS, ISRO Bhuvan, IMD, Sentinel-2, MODIS

## Contact
For queries, contact: [Your Name/Email] 