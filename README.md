# Global Pharamaceutical Spendings Dashboard

Dashboard for visualization of pharmaceutical drug spendings across the world.

## About
The Global Pharmaceutical Spendings Dashboard aims to provide intuitive tools for healthcare policy administrators across the world to make knowlegeable decisions around drug price policies. This dashboard takes in the scattered worldwide information and presents it as a decision-ready intelligence for daily decision-making.

This project is based on [Kaggle Pharmaceutical Drug Spending by countries](https://www.kaggle.com/datasets/tunguz/pharmaceutical-drug-spending-by-countries/data) data set, which originated from Organisation for Economic Co-operation and Development (OECD) collected data. With the data capped at 2016, this dashboard architechture can be easily integrated into a new data set.

## Dashboard Overview
TODO
### Charts Overview
TODO
### Interactions
TODO
### Demo
TODO
## Contributors

Jason Lee, Celine Habashy, Daria Khon, Catherine Meng

## Developer note
In order to work on this dashboard locally, follow these steps:<br><br>
Clone this GitHub repository
```{bash}
git clone https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard
```
From the project root directory, create and activate the virtual environment

```{bash}
conda env create -f environment.yml
conda activate pharma_spend_dashboard
```

Run dashboard locally

```{bash}
python src/app.py
```

You should see output "Your application is running on `http://127.0.0.1:8050/`". Copy the url into your browser to view the dashboard.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Data

Tunguz. "Pharmaceutical Drug Spending by Countries." Kaggle, [Pharmaceutical Drug Spending by Countries Dataset, Accessed](https://www.kaggle.com/datasets/tunguz/pharmaceutical-drug-spending-by-countries/data) [2024-02-14].

## License

`pharma_spend_dashboard` was created by Jason Lee, Celine Habashy, Daria Khon, Catherine Meng. It is licensed under the terms of the MIT license.