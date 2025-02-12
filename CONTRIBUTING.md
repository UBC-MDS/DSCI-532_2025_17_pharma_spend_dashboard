# Contributing to project

Thank you for considering contributing to our project! We welcome all contributions that help make this project better for everyone. Please read this guide to understand how you can help and how to do so effectively.

### Fixing typos

Small typos or grammatical errors in documentation may be edited directly using the GitHub web interface, so long as the changes are made in the *source* file.

- YES: you edit a roxygen comment in a `.R` file below `R/`.
- NO: you edit an `.Rd` file below `man/`.

### Prerequisites

Before you make a substantial pull request, you should always file an issue and make sure someone from the team agrees that it's a problem. If you've found a bug, create an associated issue and illustrate the bug with a minimal [reprex](https://www.tidyverse.org/help/#reprex).

### Reporting Bugs

If you find a bug, please open an issue and include:

1. A clear and descriptive title.

2. Steps to reproduce the problem.

3. Expected vs. actual results.

4. Screenshots, if applicable.

5. Information about your environment (e.g., OS, browser, or relevant tool versions).

### Suggesting Features

To suggest a feature or enhancement:

1. Check existing issues to avoid duplicates.

2. Open a new issue with the label `feature request`.

3. Include:

    - A detailed description of the feature.

    - Use cases and why it would be helpful.

### Pull request process

- We recommend that you create a Git branch for each pull request (PR).\
- New code should follow the tidyverse [style guide](http://style.tidyverse.org). You can use the [styler](https://CRAN.R-project.org/package=styler) package to apply these styles, but please don't restyle code that has nothing to do with your PR.\
- We use [roxygen2](https://cran.r-project.org/package=roxygen2), with [Markdown syntax](https://cran.r-project.org/web/packages/roxygen2/vignettes/rd-formatting.html), for documentation.\
- We use [testthat](https://cran.r-project.org/package=testthat). Contributions with test cases included are easier to accept.\

### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

### Attribution

These contributing guidelines were adapted from the [dplyr contributing guidelines](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md).
