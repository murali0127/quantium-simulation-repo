import pandas as pd
import glob

files = glob.glob('data/*.csv')
dfs = [pd.read_csv(file) for file in files]

df =  pd.concat(dfs)

df = df[df['product'] == 'pink morsel']
#create Sales Column
df['price'] = df['price'].str.replace('$', '' ,regex=False)
df['sales' ] = df['price'].astype(float) * df['quantity']

cols = [ col for col in df.columns if col in ['sales', 'date', 'region']]

print(df[cols])
#save
df.to_csv('task-2_formating_data_completed.csv',index=False)