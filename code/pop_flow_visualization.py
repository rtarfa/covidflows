from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Draw Plot
df = pd.read_csv('/Users/aopple/COVID_policy_imact_dataset/flow_data.csv', index_col=0, parse_dates=True)
lines = df.plot.line(   subplots=True,
                        color={"visitor_flow": "red", "pop_flow": "green"}
)
plt.show()

#visualization