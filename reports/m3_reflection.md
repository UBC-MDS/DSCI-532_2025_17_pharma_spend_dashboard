# Milestone 3 Reflection

## Current Implementations (as of milestone 3)
- Major implementations:
  - Summary Cards are now highlighted when the spend metric from the sidebar is selected.
  - The choropleth map chart is now zoomable. We did this by swapping from using Altair's mark_geoshape to using Plotly's px.choropleth. 

- Minor implementations:
  - The pie chart from milestone 2 has been removed.
  - All charts are now placed into cards. Each card has a card header with the title of the chart.
  - Due to visual clutter, bubbles on the map chart have been removed.
  - The country filter in the sidebar now has a max selection limit of 10 countries.
  - A minimal loading animation has been added for all charts.
  - The dashboard now adheres to a "Teal" color theme
  - Countries are now displayed as their full name instead of the country code for better readability
  - Spend metric radio button controls are now moved into the sidebar
  - The bar chart is now sorted in ascending order to adhere to DSCI_531 best practices
  - Summary card padding has been adjusted to be more compact
  - Starting year is now 2000 by default (as this is the inflection point where most countries in the dataset have available data)
  - Minor padding / font size adjustments 

## Impending Implementations
- We will look into whether it is possible to make the summary cards a clickable button that selects the spend metric. This was a stretch goal suggested by Joel.


## Differences compared to initial proposal / sketch

## Corner Cases

## Deviations from DSCI_531 best practices
- We have attempted to adhere strictly to DSCI_531 best practices

## Other reflections

1. What the dashboard does well
- From an aesthetics standpoint, the dashboard is now a lot more visually cohesive and organised.  
- From a performance perspective, the dashboard now loads quicker and runs faster compared to the previous version.

2. Limitations of the dashboard

3. Good potential future improvements and additions
