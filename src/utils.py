"""This module houses any utility functions required"""

def fold_mapping(folds=5):
  """This function will return the fold mapping for any number of folds.
  output will be like below for the default folds=5.
     {0: [1, 2, 3, 4],
      1: [0, 2, 3, 4],
      2: [0, 1, 3, 4],
      3: [0, 1, 2, 4],
      4: [0, 1, 2, 3]}"""
  fm = {}
  for fold in range(folds):
    fm.update({fold: [x for x in range(folds) if x!=fold]})
  return fm