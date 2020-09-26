# Note:
# We can use kfold and stratified kfold as hold-out cross validation by keep one fold for testing and rest for training
# We use hold-out strat when the dataset is huge ex. if dataset is has 1 million rows
# Also hold-out strat is mainly used for time-series problems
# for small datasets we can use kfold strat where k=N-1, when k is no. of folds and N is number of rows
# and the validation is performed one remaining row

# TODOs:
# 1: Need to implement GroupKFold with Straified fold for case like finding tumours in images of patients.
# we need to group a single patient's image and also make sure it falls in either training or validation set.