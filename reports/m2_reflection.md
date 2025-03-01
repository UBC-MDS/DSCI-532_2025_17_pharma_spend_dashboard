# Milestone 2 Reflection

## Current Implementations (as of milestone 2)
Basic functionality for all elements in our proposal has been implemented. That is: 
- Global filters for country and year selection that update summary stats cards and graph outputs
- Local filters for the spend metric selection (radio buttons) that update graph outputs
- Choropleth map chart (top left)
- Time series chart (top right)
- Bar graph (bottom left)
- Pie chart (bottom right)
- About section to provide context to the data

## Impending Implementations
- Map chart: adding zoom selection
- Map chart code: optimize country selection code/ move the computation outside of the 'plotting' block to speed up the dashboard loading time
- Potentially replace or remove the pie chart. Making this change will allow us to make the map chart larger.
- Country labels: Country names are currently are being displayed as a country code. We intend to change this to the full country name in the next milestone.

## Differences compared to initial proposal / sketch
- Headings: The `Summary Stats` heading has been removed. It's readily apparent that the cards represent summary stats so the title becomes unneccessary.
- Map chart: Added points to the graph on top of the color scale to improve visual representation of each spend metric among selected countries.
- Time series chart: Includes a scatter plot layer on top of the line graph for additional clarity.
- Bar chart: Now includes a y-axis label for clarity
- Units: The total spend metric was initially expressed in millions of USD. For better readability, total spend is now expressed in billions of USD.

## Deviations from DSCI_531 best practices

## Other reflections

1. What the dashboard does well
- The global sidebar makes it simple to filter by country and year, updating instantly to reflect users selections.
- The four summary cards at the top show an immediate overview of key metrics (e.g., GDP, health spending), which is important for users looking for quick information.
- All charts (map, time series, bar, pie) and summary cards update in real-time based on user selections.
2. Limitations of the dashboard
- Slow loading time (to be addressed by optimizing the code in later milestones). The dashboard currently takes 3-5 seconds to load the graphics upon filter selections. This could be partly due to the on-the-go data frame merge that happens with each filter update. The code will be improved by having the computations performed outside of the plotting function.
- Our data set has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. Our team will discuss how to address this limitations (removing n/a values, imputations, other) for the future milestones.
3. Good potential future improvements and additions
- Adding a background color to the summary cards could improve readability and make the statistics stand out more.
- Potentially adding a reset button to quickly return to default selections.
- Ensure all charts have consistent and equal sizing.
- Removing the pie chart in favor of the bar plot would make sense since they both show similar data, and the pie chart could get too crowded when multiple countries are selected.
- Zoom-in feature for the map
