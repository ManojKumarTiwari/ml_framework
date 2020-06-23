"""This module is used to make predictions"""

#import
import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import ensemble
from sklearn import metrics

import joblib

from . import dispatcher

# configured in run.sh file
# path to training file with folds
TRAINING_DATA = os.environ.get("TRAINING_DATA")
# path to testing file
TEST_DATA = os.environ.get("TEST_DATA")
# which model to use
MODEL = os.environ.get("MODEL")

def predict():
  # read the traning file with folds
  df = pd.read_csv(TRAINING_DATA)
  # read the test file
  df_test = pd.read_csv(TEST_DATA)

  df_test_idx = df_test["id"]
  predictions = None

  for FOLD in range(df.kfold.nunique()):
    print(FOLD)
    df_test = pd.read_csv(TEST_DATA)
    cols = joblib.load(os.path.join("models",f"{MODEL}_{FOLD}_columns.pkl"))
    encoders = joblib.load(os.path.join("models",f"{MODEL}_{FOLD}_label_encoder.pkl"))
    for c in cols:
        lbl = encoders[c]
        df_test.loc[:, c] = lbl.transform(df_test[c].values.tolist())

    df_test = df_test[cols]
    clf = joblib.load(os.path.join("models",f"{MODEL}_{FOLD}.pkl"))
    preds = clf.predict_proba(df_test)[:, 1]
    if FOLD == 0:
        predictions = preds
    else:
        predictions += preds
  predictions /= df.kfold.nunique()

  # for submission to kaggle
  sub = pd.DataFrame(np.column_stack((df_test_idx, predictions)), columns=['id', 'target'])
  return sub

if __name__ == "__main__":
    submission = predict()
    submission.to_csv(f"models/{MODEL}.csv", index=False)





  














