# Global Pharmaceutical Spending Dashboard

Dashboard for visualization of pharmaceutical drug spending across the world.

## About
The Global Pharmaceutical Spending Dashboard aims to provide intuitive tools for healthcare policy administrators across the world to make knowlegeable decisions around drug price policies. This dashboard takes in the scattered worldwide information and presents it as a decision-ready intelligence for daily decision-making.

This project is based on [Kaggle Pharmaceutical Drug Spending by countries](https://www.kaggle.com/datasets/tunguz/pharmaceutical-drug-spending-by-countries/data) data set, which originated from Organisation for Economic Co-operation and Development (OECD) collected data. With the data capped at 2016, this dashboard architechture can be easily integrated into a new data set.

## Dashboard Overview
Pharmaceutical Spending Dashboard is hosted on the Render platform, and can be accessed [here](https://dsci-532-2025-17-pharma-spend-dashboard.onrender.com/)
### Components
- Choropleth Map (Top Left): Displays geographic distribution of spending.
- Time Series Chart (Top Right): Shows spending trends over time.
- Bar Graph (Bottom Left): Breaks down overall spending by countries.
- Summary statistic
### Interactions
The user can customize the view of the dashboard by interacting with:
- Global filters: Country and year selectors apply to all charts and summary statistics, keeping the dashboard focused on the selected region and time period.
- Local filters: Radio buttons allow users to choose the specific spending metric they want to explore, which will apply to all charts.
- All charts have tooltips to provide additional information about the data, which will be displayed upon hovering over the chart element of interest.

### Demo
![img/demo.gif](https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard/blob/main/img/demo.gif)

## Contributors
Jason Lee, Celine Habashy, Daria Khon, Catherine Meng

## Developer note
### In order to work on this dashboard locally, follow these steps:
Clone this GitHub repository
```{bash}
git clone https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard
```
From the project root directory, create and activate the virtual environment

```{bash}
conda env create -f environment.yml
conda activate pharma_spend_dashboard
```

Run dashboard locally (To activate debug mode comment out change the argument in `app.run()` to `app.run(debug=True)`)

```{bash}
python src/app.py
```

You should see output "Your application is running on `http://127.0.0.1:8050/`". Copy the url into your browser to view the dashboard.

### Feedback and Support:
Feedback is welcomed! If you encounter an issue or would like to suggest new features, please let us know by opening a new issue via `Issues` tab. The new issue should have a descriptive title and a brief outline of the feedback.

## Contributing
Interested in contributing? Check out the contributing guidelines in [CONTRIBUTING.md](https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Data

Tunguz. "Pharmaceutical Drug Spending by Countries." Kaggle, [Pharmaceutical Drug Spending by Countries Dataset, Accessed](https://www.kaggle.com/datasets/tunguz/pharmaceutical-drug-spending-by-countries/data) [2024-02-14].

## License

`pharma_spend_dashboard` was created by Jason Lee, Celine Habashy, Daria Khon, Catherine Meng. It is licensed under the terms of the MIT license.
