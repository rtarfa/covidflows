import pandas as pd
df = pd.read_csv('/Users/aopple/COVID_policy_imact_dataset/Policy/COVID-19_State_and_County_Policy_Orders.csv')
df['date'] = pd.to_datetime(df['date'])
sorted = df.sort_values(by=['date'])
print(sorted['date'])
# timer = (sorted['date'] > '2020-3-1') & (df['date'] <= '2020-4-30')
# print(sorted.loc[timer])

state_idf = (sorted['state_id'] == 'VA')
print(sorted.loc[state_idf]['date'])
output = sorted.loc[state_idf]
output.to_csv('/Users/aopple/COVID_policy_imact_dataset/Policy/policy_sorted_VA.csv')
