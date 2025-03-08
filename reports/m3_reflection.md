# Milestone 3 Reflection

## Current Implementations (as of milestone 3)
- Major implementations:
  - Summary Cards are now highlighted when the spend metric from the sidebar is selected.
  - The choropleth map chart is now zoomable. We did this by swapping from using Altair's mark_geoshape to using Plotly's px.choropleth. 

- Minor implementations:
  - The pie chart from milestone 2 has been removed.
  - All charts are now placed into cards. Each card has a card header with the title of the chart. (we were inspired by team 18's milestone 2 implementation of this https://canadian-house-prices.onrender.com . They have a similar dashboard layout to ours so after seeing their charts inside of cards, it became readily apparent that this was next logical step for our project!)
  - Due to visual clutter, bubbles on the map chart have been removed.
  - The country filter in the sidebar now has a max selection limit of 10 countries.
  - A minimal loading animation has been added for all charts.
  - The dashboard now adheres to a "Teal" color theme
  - Countries are now displayed as their full name instead of the country code for better readability
  - Spend metric radio button controls are now moved into the sidebar
  - The bar chart is now sorted in ascending order to adhere to DSCI_531 best practices
  - Summary card padding has been adjusted to be more compact
  - Starting year is now 2000 by default (as this is the inflection point where most countries in the dataset have available data)
  - Added a collapsable "About" button to give the sidebar a more clean appearance. When the button is clicked, more details about the project appear.
  - Minor padding / font size adjustments 

## Impending Implementations
- We will look into whether it is possible to make the summary cards a clickable button that selects the spend metric. This was a stretch goal suggested by Joel.

## Differences compared to initial proposal / sketch
- Pie chart has been removed due to redundancy in information conveyed together with the bar chart
- Radio buttons moved to the left side bar

## Corner Cases
- There is some missing data for earlier years (1970-1990s). In the later milestone we will add a warning/disclaimer about comparing averages with missing data.
- The pie chart has been removed, as it conveyed redundant information with the bar chart
- Radio buttons moved from the body to the left side bar

## Corner Cases
- There is some missing data in the earlier years (1970s-1990s), which would make comparing averages 'unfair'. We will add a warning/disclaimer about it in the later milestone.

## Deviations from DSCI_531 best practices
- We have attempted to adhere strictly to DSCI_531 best practices

## Other reflections
1. What the dashboard does well
- From an aesthetics standpoint, the dashboard is now a lot more visually cohesive and organised.  
- From a performance perspective, the dashboard now loads quicker and runs faster compared to the previous version.
- With interactive filters and multiple spend metrics, the dashboard gives users plenty of ways to explore the data in detail.
  
2. Limitations of the dashboard
- Our data set has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. In this milestone, we addressed this issue by changing the default year to 2000 (where there is less missingness in the data) instead of 1970.

4. Good potential future improvements and additions
- While the loading performance has significantly improved compared to milestone 2 submission, we can look into further optimizing the performance by implementing dask or other parallel computing techniques.

3. Challenging
- We attempted the challenging question by adding borders to our charts to make the dashboard more structured. We were inspired from Group 18’s dashboard, where they used subtle borders to help separate elements in a clean and effective way. Seeing how it improved readability in their design, we decided to implement a similar approach to enhance our own dashboard.
