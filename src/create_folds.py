"""This module is used to create stratified k-folds"""

# imports
import pandas as pd
from sklearn import model_selection

# to run the script
if __name__ == "__main__":

    # INPUT_FILE_PATH = "input/train.csv"
    # read the file
    df = pd.read_csv("../input/train.csv")
    # create "kfold" column
    df["kfold"] = -1
    
    # shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)

    # create number of folds
    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=123)

    # loop over each fold and get the training and validation indexes
    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=df.target.values)):
        print(len(train_idx), len(val_idx))
        # assign the currect fold value to the "kfold" column of all rows which validation indexes
        df.loc[val_idx, "kfold"] = fold

    # save the file
    df.to_csv("../input/train_folds.csv", index=False)













