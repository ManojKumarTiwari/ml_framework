"""This module is used to train the model"""

#import
import os
import pandas as pd
from sklearn import preprocessing
from sklearn import ensemble
from sklearn import metrics

import joblib

from . import utils
from . import dispatcher

# configured in run.sh file
# path to traning file
TRAINING_DATA = os.environ.get("TRAINING_DATA")
# which fold to use for training
FOLD = int(os.environ.get("FOLD"))
# which model to use
MODEL = os.environ.get("MODEL")
# mapping to segregate training and validation set
FOLD_MAPPING = None

if __name__ == "__main__":
  df = pd.read_csv(TRAINING_DATA)
  FOLD_MAPPING = utils.fold_mapping(df.kfold.nunique())
  train_df = df[df.kfold.isin(FOLD_MAPPING.get(FOLD))]
  valid_df = df[df.kfold==FOLD]

  ytrain = train_df.target.values
  yvalid = valid_df.target.values

  train_df = train_df.drop(["id", "target", "kfold"], axis=1)
  valid_df = valid_df.drop(["id", "target", "kfold"], axis=1)

  # set the order of features in valid_df same as train_df
  valid_df = valid_df[train_df.columns]

  label_encoders = []
  for c in train_df.columns:
    lbl = preprocessing.LabelEncoder()
    lbl = lbl.fit(train_df[c].values.tolist() + valid_df[c].values.tolist())
    train_df.loc[:, c] = lbl.transform(train_df[c].values.tolist())
    valid_df.loc[:, c] = lbl.transform(valid_df[c].values.tolist())
    label_encoders.append((c, lbl))

  # data is ready to train
  clf = dispatcher.MODELS[MODEL]
  clf.fit(train_df, ytrain)
  preds = clf.predict_proba(valid_df)[:, 1]
  print(metrics.roc_auc_score(yvalid, preds))

  #save files
  joblib.dump(label_encoders, f"models/{MODEL}_label_encoder.pkl")
  joblib.dump(clf, f"models/{MODEL}.pkl")



  














