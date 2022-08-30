import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff

df=pd.read_csv("medium_data.csv")
data=df['reading_time'].tolist()
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()

population_mean=statistics.mean(data)
print('population mean -> ',population_mean)
population_std_dev=statistics.stdev(data)
print('population standard deviation -> ',population_std_dev)



dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)
print("the mean of the data od dataset is ->    ",mean)
print("standard deviation of the dataset is -> ",std_deviation)

