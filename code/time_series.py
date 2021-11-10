import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("../dataset/policy/flow_data_2020.csv", parse_dates=True, index_col = "time")
df.head()
df['pop_flow'].plot()
df.plot(subplots=True, figsize=(10,12))