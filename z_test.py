import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("marks.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(mean)
print(stdev)

def group_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_means = group_of_means(100)
    mean_list.append(set_of_means)
mean_sample = statistics.mean(mean_list)
stdev_sample = statistics.stdev(mean_list)
print("Sample mean:", mean_sample)
print("Sample standard deviation:", stdev_sample)

first_std_dev_start, first_std_dev_end = mean_sample - stdev_sample, mean_sample + stdev_sample
second_std_dev_start, second_std_dev_end = mean_sample - (2 * stdev_sample), mean_sample + (2 * stdev_sample)
third_std_dev_start, third_std_dev_end = mean_sample - (3 * stdev_sample), mean_sample + (3 * stdev_sample)

"""fig = ff.create_distplot([mean], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0, 0.20], mode = "lines", name = "First Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 0.20], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y = [0, 0.20], mode = "lines", name = "Second Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0, 0.20], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y = [0, 0.20], mode = "lines", name = "Third Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0, 0.20], mode = "lines", name = "Third Standard Deviation End"))
fig.show()"""

df = pd.read_csv("data2.csv")
data1 = df["Math_score"].tolist()
mean_of_sample_1 = statistics.mean(data1)
"""fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y = [0, 0.20], mode = "lines", name = "Mean of sample"))
fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 0.20], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0, 0.20], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0, 0.20], mode = "lines", name = "Third Standard Deviation End"))
fig.show()"""

zscore = (mean_sample - mean_of_sample_1)/stdev_sample
print(zscore)