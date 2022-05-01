from os import times_result

from scipy.stats import gaussian_kde
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    fareData = pd.read_csv('./data/sampleData/sampleDataFare.csv')
    tripData = pd.read_csv('./data/sampleData/sampleDataTrip.csv')
    print('Successful data import')
except:
    print("Error [Check data exists in file location]")


def calcAverage(statement, amount, rounder, unit):
    average = amount.mean()
    print(f"{statement} {round(average, rounder)} {unit}")


def calcProbability(y, z, message, rounder):
    print(y, z)
    prob = y / z
    print(f'{message}{round(prob, rounder)}')

def calcNumberForGraph(input):
    numberOfEntriesLen = len(input)
    return numberOfEntriesLen


# Zero mi trips (may contain outliers)
distance0 = tripData.loc[tripData.trip_distance == 0]
tripData.drop(distance0.index, axis=0, inplace=True)
fareData.drop(distance0.index, axis=0, inplace=True)
distance0.to_csv("./data/dataOutput/trips0.csv")

# Trips Above 31mi
distanceAbove31 = tripData.loc[tripData.trip_distance >= 31]
# Merge the medallion so I can access financial data
distanceAbove31 = distanceAbove31.merge(fareData, left_index=True, right_index=True)
distanceAbove31.to_csv("./data/dataOutput/tripsAbove31.csv")

# Trips below 18.64
distanceBelow31 = tripData.loc[tripData.trip_distance <= 18.64]
# Merge medallion so both cost and distance are available
distanceBelow31 = distanceBelow31.merge(fareData, left_index=True, right_index=True)
distanceBelow31.to_csv("./data/dataOutput/tripsBelow18.csv")

# Trips below 31mi
distanceBelow31mi = tripData.loc[tripData.trip_distance <= 31]
distanceBelow31mi = distanceBelow31mi.merge(fareData, left_index=True, right_index=True)
distanceBelow31mi.to_csv("./data/dataOutput/tripsBelow31.csv")

# Select trips that are above 18.64 mi in length
distanceAbove31 = tripData.loc[tripData.trip_distance >= 18.64]
# Merge the data by medallion to create a dataset with both trips >= 18.64 mi and the cost of the trip
distanceAbove31 = distanceAbove31.merge(fareData, left_index=True, right_index=True)
distanceAbove31.to_csv("./data/dataOutput/tripsAbove18.csv")

totalAmountDataFrame = fareData[' total_amount']
distanceOfTrip = tripData['trip_distance']
distanceBelow31Cost = distanceBelow31[' total_amount']
distanceAbove31Cost = distanceAbove31[' total_amount']
distanceBelow31miCost = distanceBelow31mi[' total_amount']

calcAverage('Average cost for ALL trip $', totalAmountDataFrame, 3, 'USD')
calcAverage('Average distance for ALL trip', distanceOfTrip, 3, 'mi')
calcAverage('Average cost for trips below 18.64 mi: $', distanceBelow31Cost, 3, 'USD')
calcAverage('Average cost for trips below 31 mi: $', distanceBelow31miCost, 3, 'USD')
calcAverage('Average cost for trips Above 18.64 mi: $', distanceAbove31Cost, 3, 'USD')
calcProbability(len(distanceAbove31), len(tripData), 'Probability of trip being above 18.64 mi: %', 5)
calcProbability(len(distanceBelow31), len(tripData), 'Probability of trip being below 18.64 mi: %', 5)

# Joined data
joinData = pd.concat([fareData, tripData], axis=1, join='inner')

# Reshaped data.
xData = np.array(joinData['trip_distance']).reshape(-1, 1)
yData = np.array(joinData[' tip_amount']).reshape(-1, 1)

# Flatten the array
# Flattened data.
faltX = xData.flatten()
faltY = yData.flatten()

xy = np.vstack([faltX, faltY])
z = gaussian_kde(xy)(xy)

# scatter plot for distance and money earned
plt.figure(figsize=(6, 6))
plt.title(f'Trips above 18.64mi(31km): [{calcNumberForGraph(distanceAbove31)}]')
plt.scatter(distanceOfTrip, totalAmountDataFrame, c=z)
plt.scatter(distanceAbove31['trip_distance'], distanceAbove31[' total_amount'], c='r', alpha=0.3)
plt.xlabel('Distance', fontsize=14, labelpad=15)
plt.ylabel('Cost', fontsize=14, labelpad=15)
plt.show()
