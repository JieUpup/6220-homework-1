import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
filename = "test.csv"




# read data and format it.
df = pd.read_csv(filename, parse_dates=['date'])

ratings = {}
# formatted
for index, row in df.iterrows():
    date = row['date']
    rate = row['rate']

    y_m = date.strftime('%Y-%m')
    # condition
    if ratings.get(y_m) == None:
        v = [int(rate), 1]
        ratings[y_m] = v
    else:
        s, count = ratings[y_m]
        ratings[y_m] = [s + int(rate), count + 1]

new_r = {}
# use for loop to check is the k and v in the ratings.
for k, v in ratings.items():
    s = v[0]
    c = float(v[1])
    new_r[k] = s/c
x_arr = [datetime.strptime(s, "%Y-%m") for s in new_r.keys()]
fig, ax = plt.plot(x_arr, new_r.values())
plt.savefig('d.pdf')

#ax = df.plot.scatter(x='date', y='rate')

#fig = ax.get_figure()
#fig.savefig('distri.pdf')