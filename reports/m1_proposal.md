# Milestone 1 Proposal: Global Pharamaceutrical Spendings

Group 17: Jason Lee, Celine Habashy, Daria Khon, Catherine Meng

## Motivation and Purpose

**Our Role:** A healthcare economics consultancy specializing in data-driven policy analysis.

**Target Audience:** Health care administrators

Healthcare administrators worldwide are faced with the constant challenge of ensuring patient care quality along with the constraints of limited budgets and unpredictable supply chains. In Canada, the rising cost of pharmaceuticals has been a significant concern, with expenditures on pharmaceuticals consuming an increasingly large share of healthcare budgets over the past decade. For those managing hospitals, clinics, and regional health networks, these trends create operational risks—delays in securing essential drugs, strained budgets, and unstable supplier partnerships—that directly jeopardize their ability to provide reliable care.

This **Global Pharmaceutical Spendings** dashboard is designed to assist healthcare administrators by transforming scattered worldwide information into decision-ready intelligence for daily decision-making. During periods of supply disruption, administrators can look at historical data to identify persistent vulnerabilities and find alternatives. For administrators who are preparing annual budgets, the dashboard provides a view of long-term trends in spending. Being able to see how Canadian drug costs have persistently increased relative to other countries gives a foundation for renegotiating agreements with drug suppliers or revising formulary guidelines.

The **Global Pharmaceutical Spendings** dashboard addresses these challenges by providing an interactive platform that visualizes over 40 years of pharmaceutical expenditure data across 30+ countries to prioritize patient care outcomes. 


## Description of Data
We will be visualizing a dataset of pharmaceutical spending by country and year. 
In total, there are 1036 rows and 7 columns. 
In this dataset, pharmaceutical spending is represented in 4 different ways. 
This gives health authorities a few different lenses to inspect how pharmaceutical spending in different countries has changed across different time horizons. 
A short description for each variable in the dataset is provided below.

LOCATION: Categorical variable that denotes the ISO country code. There are 36 countries in this data set.
TIME: Denotes the year and spans from 1970 to 2016.
PC_HEALTHXP: Percentage of pharmaceutical spending relative to healthcare spend
PC_GDP: Percentage of pharmaceutical spending relative to country GDP
USD_CAP: Pharmaceutical spending (in USD) per capita
TOTAL_SPEND: Total pharmaceutical spending (in USD m)
FLAG_CODES: This column was not clearly defined in the dataset. We will not use this column for the dashboard.

Using this data we will also derive 4 new variables that will analyse the year on year percentage change in pharmaceutical spending (PC_HEALTHXP_PCT_CHANGE, PC_GDP_PCT_CHANGE, USD_CAP_PCT_CHANGE, TOTAL_SPEND_PCT_CHANGE) 
We will also create a new categorical column called `COUNTRY_NAME` that will contain country names for better interpretability. 


## Research Questions

**Persona:** Christine Crudo, Senior Official at the Canadian Ministry of Health

Christine Crudo is responsible for developing and implementing policies related to public health regulations. They play a key role in shaping national health strategies and policies, ensuring regulatory compliance, and Canada's ability to proactively react to any health emergencies. Therefore, Christine could rely on the **Global Pharmaceutical Spendings** dashboard to gain insights on the following:
- Understand the current trends on the market for 'off-the-shelf' drugs
- Control Canadian healthcare costs
- Ensure supply chain integrity and stability
- Assessing holistic impact of the trends on the gloabl healthcare systems

#### User Story: Using the Global Pharmaceutical Spendings Dashboard

Christine is currently drafting a tax policy on imported drugs. They opens a dashboard to analyze historical and recent trends in global drug expenditures, performing the following tasks: 
1. **Filtering time data:** they set the time range to the last 20 years to focus on recent spending patterns.
2. **Comparing trends and statistics:** they look at the share of total health spending on pharmaceuticals worldwide, then narrow it down to North America, and then finally isolate Canada's data
3. **Geospatial Analysis:** they explore the distribution of pharmaceutical spending across different countries to identify high and low-expenditure regions and investigates their respective healthcare policies.

Based on their findings Christine identifies Luxemburg as a country with lowest expenditures in the last 20 years, and creates a task for them to investigate Luxemburg's tax policies. Moreover, Christine has numeric data to support the growth in spendings in the last 20 years in Canada that would influence the 2026 tax policy.
