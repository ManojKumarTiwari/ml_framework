"""This module is used to create stratified k-folds csv file"""

# imports
import pandas as pd
import numpy as np
from sklearn import model_selection
import argparse

# to run the script
if __name__ == "__main__":

    # construct the ArgumentParser Object
    ap = argparse.ArgumentParser()

    # add an argument
    ap.add_argument("-k","--kfolds", help="number of folds to create")
    ap.add_argument("-i","--input", help="path to input file")
    ap.add_argument("-o","--output", help="path to output file")
    ap.add_argument("-t_col","--target_column_name", help="enter the target column name")
    ap.add_argument("-pt", "--problem_type", help="enter clf for classification(clf) problem or reg for regression(reg)")

    # parse the arguments
    args = vars(ap.parse_args())

    # read the file
    df = pd.read_csv(args["input"])
    # create "kfold" column
    df["kfold"] = -1
    
    # shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)

    if str(args["problem_type"]) == "reg":
        # Calculate the number of bins according to Sturge's Law
        num_bins = np.floor(1 + np.log2(len(df)))
        df.loc[:,"bin"] = pd.cut(df[str(args["target_column_name"])], bins=num_bins, labels=False)

        # create number of folds
        kf = model_selection.StratifiedKFold(n_splits=int(args["kfolds"]), shuffle=False, random_state=123)

        # loop over each fold and get the training and validation indexes
        for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=df["bin"].values)):
            print(len(train_idx), len(val_idx))
            # assign the currect fold value to the "kfold" column of all rows which validation indexes
            df.loc[val_idx, "kfold"] = fold

        # drop the bin column
        df.drop(labels="bin", axis=1, inplace=True)

    elif str(args["problem_type"]) == "clf":
        # create number of folds
        kf = model_selection.StratifiedKFold(n_splits=int(args["kfolds"]), shuffle=False, random_state=123)

        # loop over each fold and get the training and validation indexes
        for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=df[str(args["target_column_name"])])):
            print(len(train_idx), len(val_idx))
            # assign the currect fold value to the "kfold" column of all rows which validation indexes
            df.loc[val_idx, "kfold"] = fold

    # save the file
    df.to_csv(args["output"], index=False)


