import numpy as np
import pandas as pd

# Load the data and initialize dataset in a bid to store the pre-processed data
data_origin = pd.read_excel("2.4.xlsx")
# Convert the origin shape into numpy array
data_np = np.array(data_origin)
dataset = np.zeros([data_np.shape[0] // 2 ,data_np.shape[1] + 2])

# Process the pretreatment process
j = 0
for i in range(1, data_np.shape[0],2):
    dataset[j, 0:3] = data_np[i, 0:3]
    j += 1

# Calculation of the average temperature
for i in range(0, dataset.shape[0]):
    average_current = (dataset[i, 1] + dataset[i, 2]) / 2.
    dataset[i, 3] = average_current
    average_current = 0

# Calculation of the effective temperature
for i in range(0, dataset.shape[0]):
    effective_temperature = (dataset[i,3] - 3)
    dataset[i,4] = effective_temperature
    effective_temperature = 0

# Calculation of the days required for the 900 day-degrees in day 119
total_day_degrees_1 = 0
day_tag_1 = 119
for i in range(0, dataset.shape[0]):
    if dataset[i,4] >= 0:
        total_day_degrees_1 += dataset[i,4]
    if total_day_degrees_1 > 900:
        day_tag_1 += i + 1
        break

# Calculation of the days required for the 900 day-degrees in day 150
total_day_degrees_2 = 0
day_tag_2 = 150
j = 0
for i in range(150 - 119, dataset.shape[0]):
    if dataset[i,4] >= 0:
        total_day_degrees_2 += dataset[i,4]
    if total_day_degrees_2 > 900:
        day_tag_2 += j
        break
    j += 1

print(f"Answer:\nThe date of flowering of spring wheat planted on day 119 if required 900 day-degrees is: {day_tag_1}.")
print(f"The date of flowering of spring wheat planted on day 150 if required 900 day-degrees is: {day_tag_2}.")
print(f"If planting is delayed to day 150, it will need {day_tag_2 - day_tag_1} extra days.")