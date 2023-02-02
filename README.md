# Accuracy check
This algorithm calculates the accuracy of a model on recently served predictions. It needs two liveSet inputs. One needs to be the models predictions and the other needs to be the ground truth labels. Order doesn't matter. It ignores any trainSet inputs.

## Parameters
- **threshold**: The accuracy value below which the algorithm should signal dataset shift. If not provided the default value of 0.8 will be used.