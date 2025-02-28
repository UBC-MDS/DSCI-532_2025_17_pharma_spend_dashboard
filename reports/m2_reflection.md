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
- Potentially replace or remove the pie chart


## Differences compared to initial proposal / sketch
- Map chart: added points to the graph on top of the color scale to improve visual representation of each spend metric among selected countries.


## Deviations from DSCI_531 best practices

## Other reflections

1. What the dashboard does well
- The global sidebar makes it simple to filter by country and year, updating instantly to reflect their selections.
- The four summary cards at the top show an immediate overview of key metrics (e.g., GDP, health spending), which is important for users looking for quick information.
- All charts (map, time series, bar) and summary cards update in real-time based on user selections.
3. Limitations of the dashboard
- Slow loading time (to be addressed by optimizing the code in later milestones). The dashboard currently takes 3-5 seconds to load the graphics upon filter selections. This could be partly due to the on-the-go data frame merge that happens with each filter update. The code will be improved by having the computations performed outside of the plotting function.
- Our data set has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. Our team will discuss how to address this limitations (removing n/a values, imputations, other) for the future milestones.
3. Good potential future improvements and additions
- Adding a background color to the summary cards could improve readability and make the statistics stand out more.
- Potentially adding  a reset button to quickly return to default selections.
- Ensure all charts have consistent and equal sizing.
- Removing the pie chart in favor of the bar plot would make sense since they both show similar data, and the pie chart could get too crowded when multiple countries are selected.
- Zoom-in feature for the map