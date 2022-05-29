import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data request
url              = 'https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest'
parameters       = {}
response         = requests.request("GET", url, params=parameters)
objects          = json.loads(response.text)
data = objects['data']

df = pd.DataFrame(data)

# sort by population
#df = df.sort_values(by=['Population'], ascending=False)

states = df['State']
total_pop = df['Population'].sum()

# create another column with population percentage
for index, row in df.iterrows():
    df.at[index, 'Population %'] = (row['Population'] * 100 / total_pop)

# set graph color
colors = sns.color_palette('colorblind')[0:5]

# output
plt.pie(df['Population %'], labels = states, colors = colors, textprops={'fontsize':6})
plt.show()
#plt.savefig("graph/usa_population_by_state.jpeg")