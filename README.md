# DE-PRJT
#Updated/Modularized
We collaborated to create a GitHub repository named “Data_Engineering_Project” and used an API key from the Kaggle API to fetch the wine dataset via Bash. The data was then analyzed using Python in Google Colab, where we performed exploratory data analysis (EDA) and generated visualizations to better understand the dataset.

The analysis shows that most wines are priced in the low to mid range, with only a few very expensive ones, which can affect average values, so the median is more reliable. Wine ratings are quite similar across the dataset, meaning it’s harder to clearly distinguish quality based on scores alone. There is also a weak link between price and rating, suggesting that price is influenced more by factors like brand or origin rather than quality. Some countries appear more frequently and have a strong influence on pricing patterns. Missing data was handled to keep the dataset usable, though it may reduce some detail. Overall, the dataset is somewhat complex, with outliers and no strong relationships between key variables.


<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

WINEDATASET

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         DATAENG and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── DATAENG   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes DATAENG a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

