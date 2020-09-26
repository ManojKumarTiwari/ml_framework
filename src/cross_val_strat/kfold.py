# imports
import pandas as pd
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

    # parse the arguments
    args = vars(ap.parse_args())

    # read the file
    df = pd.read_csv(args["input"])
    # create "kfold" column and intialize with -1
    df["kfold"] = -1

    # shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)

    # create number of folds
    kf = model_selection.KFold(n_splits=int(args["kfolds"]))

    # loop over each fold and get the training and validation indexes
    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df)):
        print(len(train_idx), len(val_idx))
        # assign the currect fold value to the "kfold" column of all rows which validation indexes
        df.loc[val_idx, "kfold"] = fold

    # save the file
    df.to_csv(args["output"], index=False)