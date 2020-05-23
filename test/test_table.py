"""
test_table performs sanity checks on basic data manipulations for the MetOncoFit application

@author: Scott Campit
"""

import os
import pandas as pd
import numpy as np

base = os.path.dirname(os.path.abspath(__file__))
df = pd.read_json('./../data/db.json')
print("Current MetOncoFit database")
print(df.head(10))

print("Database columns")
print(df.columns)

# Create a dataframe based on the target labels. I chose UPREGULATED/GAIN as an arbitrary example.
print("Creating dataframes based on target labels")
up   = df.loc[(df["Type"] == "UPREGULATED") | (df["Type"] == "GAIN")]
up   = up.sort_values(by="Gini", ascending=False)

print("UPREGULATED/GAIN dataframe (sorted by Gini impurity value)")
print(up.head(10))

# Get a single cancer from the database
print("Print cancer types in the database")
print(up["Cancer"].unique())

print("Get Glioma from the database")
cns=up.loc[up['Cancer']=="Glioma"]
print(cns.head(10))

# Pivot datatable
pivot_up = pd.pivot(cns,
                    values='Value',
                    index=['Gene'],
                    columns=['Feature'],
                    aggfunc=np.mean)
print(pivot_up)


