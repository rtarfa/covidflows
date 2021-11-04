import pandas as pd
import glob

# read in all the files in weekly_flows folder
# path = r'/Users/aopple/COVID_policy_imact_dataset/COVID19USFlows-WeeklyFlows-master/weekly_flows/state2state_2020/' # use your path
# all_files = glob.glob(path + "/*.csv")
# li = []
# for filename in all_files:
#     df = pd.read_csv(filename, index_col=None, header=0)
#     li.append(df)
# frame = pd.concat(li, axis=0, ignore_index=True)

# here the prefix '51' means the counties in Virginia
# to find out how the GeoID is made up, go to https://www2.census.gov
df = pd.read_csv('/Users/aopple/COVID_policy_imact_dataset/COVID19USFlows-WeeklyFlows-master/weekly_flows/state2state_2020/weekly_state2state_2020_06_29.csv')
intoVA_o = df[df['geoid_o'] == 51]
intoVA_d = df[df['geoid_d'] == 51]
# print(intoVA_o)
# print(intoVA_d)
visitor_flow = intoVA_o['visitor_flows'].sum() + intoVA_d['visitor_flows'].sum()
print(visitor_flow)
pop_flow = intoVA_o['pop_flows'].sum() + intoVA_d['pop_flows'].sum()
print(pop_flow)

