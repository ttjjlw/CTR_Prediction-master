import pandas as pd

train = pd.read_csv('train.csv', chunksize=1000)
for data in train:
    data.to_csv('train_frac_0.01.csv', index=False)
    print(data.shape)
    break