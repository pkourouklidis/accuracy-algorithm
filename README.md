# Accuracy check
This algorithm calculates the accuracy of a model given a set of predictions and the coresponding ground truth labels.

## Live data inputs
- A _Model's_ _Prediction_. For example _happiness_prediction_ for the _callcenter-tree_ _Model_
- The _Label_ that the afformentioned _Prediction_ is trying to predict. For example _is_happy_ for the _happiness_prediction_ _Prediction_.

**Note**: The algorihtm will only consider the first two _live data_ inputs and ignore the rest. It will also ignore any _historical data_ inputs. The order that the _Prediction_ and _Label_ in the _live data_ does not matter.

## Parameters
- **threshold**: The accuracy value below which the algorithm should signal dataset shift. If not provided the default value of 0.8 will be used.