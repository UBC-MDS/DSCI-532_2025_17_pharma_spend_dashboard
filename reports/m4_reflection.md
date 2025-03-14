# Milestone 4 Reflection

## Current Implementations (as of milestone 4)
- Major implementations:
   Performance Improvements
    - Enabled caching for faster updates when loading plots and the summary card.
    - Created a processed data file in binary format (geoparquet).
    - Added a submit button to improve execution efficiency.

- Minor implementations:
  
    Dashboard:
    - Adjusted the bar plot height and sidebar spacing for better styling.
    - Added a watermark image to the sidebar.
    - Based on peer feedback, updated tooltips to display values in USD and rounded numbers to two significant digits.
    - Removed the three-dot menu from the bar plot and time series plot.
    - Added a custom favicon and set the tab title.
    - Specified the VegaFusion package version in the Conda environment file to align with the Python requirements file.
    - Added a title formatter function for more flexible chart name changes.
    - Added logic that controls tooltip formatting.
    - The choropleth map now uses a binary color scale instead of a diverging one. Choropleth color scale ranges from white to a burgundy color.
    - The "country" label has been removed from the legend of the time series chart and the y-axis of the bar chart to avoid redundancy
    - "USD" has been removed from chart titles to avoid redundancy
    - The dashboard title has been shortened for conciseness and design purposes
    - Country selection has now been configured to have a minimum selection of 1 country. "Canada" is now the default country if the user attempts to clear the selection.

    Readme:
    - Motivation section has been updated
    - Badges have been added
    - New logo has been added
    - GIF has been updated to reflect dashboard updates
 
    Challenging:
    - Added docstrings to functions (Challenging)
    - Created tests for callbacks and sidebar
    - Added relevant code comments 

## Differences compared to initial proposal / sketch
- Pie chart has been removed due to redundancy in information conveyed together with the bar chart
- Radio buttons moved to the left side bar
- Dashboard title has been shortened for better space alignment

## Corner Cases

- When the user attempts to clear all country selections, "Canada" will be set as the default selection, and an error message will appear indicating that at least one country must be selected. The error message will automatically disappear after 5 seconds.

- When the user attempts to select more than 10 countries, any extra selections will be removed, and an error message will appear indicating that a maximum of 10 countries is allowed. The error message will automatically disappear after 5 seconds.

## Deviations from DSCI_531 best practices
- In our design we attempted to adhere to all DSCI_531 best practices

## Other reflections
1. What the dashboard does well
- Our dashboard is well-styled, and nicely laid out with a teal theme.
- Added a white-to-burgundy color scale that provides better contrast on the map.
- We've optimized the dashboard for speed by implementing caching and using binary file formats like GeoParquet. 
- Faster response times make for a seamless experience when switching between different countries and metrics.
- Adding a submit button was a great way to prevents the dashboard from recalculating every time a selection changes, running updates only when the user is ready. This keeps everything faster and more efficient.
- Tooltips now display values in a cleaner format (rounded to two significant digits), making them more readable.
- We removed redundant labels from the y-axis of the bar chart and the legend in the time series chart, creating a cleaner and more professional look.
- We’ve made sure that titles, legends, and axis labels are all formatted in a way that makes sense and doesn’t overwhelm the user with excessive detail.
  
2. Limitations of the dashboard
- Our data set still has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. To address this, we have added a disclaimer button next to the year dropdown. This button provides users with a clear notice about potential data gaps and advises caution when interpreting trends over time.
  
3. Good potential future improvements and additions
- Users could hover over countries on the map to instantly see key metrics.
- Clicking on a country in the map could dynamically update the line chart and bar plot to focus on that country’s trends.

