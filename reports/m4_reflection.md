# Milestone 4 Reflection

## Current Implementations (as of milestone 4)
- Major implementations:
    - 
- Minor implementations:
    - Enabled caching for faster updates when loading plots and the summary card.
    - Adjusted the bar plot height and sidebar spacing for better styling.
    - Added a watermark image to the sidebar.
    - Based on peer feedback, updated tooltips to display values in USD and rounded numbers to two significant digits.
    - Removed the three-dot menu from the bar plot and time series plot.
    - Added a custom favicon and set the tab title.
    - Created a processed data file in binary format.
    - Specified the VegaFusion package version in the Conda environment file to align with the Python requirements file.
    - Added a submit button to improve execution efficiency.
    - Included docstrings in charts.py
    - Introduced a title formatter function for more flexible chart name changes.
    - Implemented tooltip formatting logic.
    - Improved data loading speed by adding a Parquet version of the dataset (binary file format).

## Differences compared to initial proposal / sketch

## Corner Cases

## Deviations from DSCI_531 best practices

## Other reflections
1. What the dashboard does well
- Our dashboard is well-styled, and nicely laid out with a teal theme
  
3. Limitations of the dashboard
- Our data set still has a fair amount of missing values, especially for the earlier years (1970s to 1990s). As a result, directly comparing averages across countries with varying levels of data completeness would be misleading for the user. Our team will discuss how to address this limitations (removing n/a values, imputations, other) for the future milestones.
  
3. Good potential future improvements and additions
4. Challenging
