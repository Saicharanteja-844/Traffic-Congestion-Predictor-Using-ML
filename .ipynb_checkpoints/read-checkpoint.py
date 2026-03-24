#code to read the data from the METER-LA dataset METR-LA.h5\METR-LA.h5
# read data and import to excel data sheet

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the traffic speed data
df = pd.read_hdf('METR-LA.h5/METR-LA.h5')
# Convert the DataFrame to an Excel file
# df.to_excel('METR-LA.xlsx', index=False)

print(df.head())