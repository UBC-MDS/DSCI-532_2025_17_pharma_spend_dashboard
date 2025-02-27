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
2. Limitations of the dashboard
- Slow loading time (to be addressed by optimizing the code in later milestones). The dashboard currently takes 3-5 seconds to load the graphics upon filter selections. This could be partly due to the on-the-go data frame merge that happens with each filter update. The code will be improved by having the computations performed outside of the plotting function.
- Our data set has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. Our team will discuss how to address this limitations (removing n/a values, imputations, other) for the future milestones.
3. Good potential future improvements and additions