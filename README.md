# Vituity Take-Home Test

## Instructions

The project instructions are listed under `Project_README.md`


## Data

Data files are under `/data`.

## Environments

To activate the environment:

```
conda env create
source activate vituity
```

## Notebooks

Data exploration: `notebook/vituity_exploration.ipynb`

Data cleaning and model training pipelines: `notebook/pipeline_training.ipynb`

To run, activate the environment and run `jupyter notebook`.

## Demo

A demo of the model is availabe at (https://bqkj32i4x9.execute-api.us-east-1.amazonaws.com/dev/). This is a flask wrapper around the sklearn model that was deployed with Zappa.

For more details see `web_app/README.md`.