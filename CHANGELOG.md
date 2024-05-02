# Release History

---

## 0.2.1
- Added test for `x_begin` parameter

## 0.2.0
- Added `x_begin` parameter that gives ability to calculate limits based on a specific window, when paired with existing `x_cutoff` parameter. Previously you had to filter the data being passed into the `XmR_Chart` method if you wanted to specify a start date for calculating limits.

## 0.1.3
- Fixed bug when using sloped data that plotted annotation and shapes prior to actual data. xref now is set at paper and x-value is calculated accordingly.
- Fixed bug that threw error when x Series is not datetime.

## 0.1.2
- Added tests for all parameters under `src/tests/`

## 0.1.1
- Updates to package structure and README.

## 0.1.0

- Initial commit. Ability to create XmR Charts from a pandas dataframe. Package will automatically calculate the limits for you and identify signals in your data according to the SPC framework.