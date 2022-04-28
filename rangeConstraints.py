from os import times_result

import pandas as pd
import matplotlib.pyplot as plt

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


# Zero km trips (may contain outliers)
distance0 = tripData.loc[tripData.trip_distance == 0]
tripData.drop(distance0.index, axis=0, inplace=True)
fareData.drop(distance0.index, axis=0, inplace=True)
distance0.to_csv("./data/dataOutput/trips0.csv")

# Trips Above 50km
distanceAbove50 = tripData.loc[tripData.trip_distance >= 50]
# Merge the medallion so I can access financial data
distanceAbove50 = distanceAbove50.merge(fareData, left_index=True, right_index=True)
distanceAbove50.to_csv("./data/dataOutput/tripsAbove50.csv")

# Trips below 30km
distanceBelow30 = tripData.loc[tripData.trip_distance <= 30]
# Merge medallion so both cost and distance are available
distanceBelow30 = distanceBelow30.merge(fareData, left_index=True, right_index=True)
distanceBelow30.to_csv("./data/dataOutput/tripsBelow30.csv")

# Trips above 50km
distanceBelow50km = tripData.loc[tripData.trip_distance <= 50]
distanceBelow50km = distanceBelow50km.merge(fareData, left_index=True, right_index=True)
distanceBelow50km.to_csv("./data/dataOutput/tripsBelow50.csv")

# Select trips that are above 30km in length
distanceAbove30 = tripData.loc[tripData.trip_distance >= 30]
# Merge the data by medallion to create a dataset with both trips >= 30 km and the cost of the trip
distanceAbove30 = distanceAbove30.merge(fareData, left_index=True, right_index=True)
distanceAbove30.to_csv("./data/dataOutput/tripsAbove30.csv")

totalAmountDataFrame = fareData[' total_amount']
distanceOfTrip = tripData['trip_distance']
distanceBelow30Cost = distanceBelow30[' total_amount']
distanceAbove30Cost = distanceAbove30[' total_amount']
distanceBelow50kmCost = distanceBelow50km[' total_amount']

calcAverage('Average cost for ALL trip $', totalAmountDataFrame, 3, 'USD')
calcAverage('Average distance for ALL trip', distanceOfTrip, 3, 'km')
calcAverage('Average cost for trips below 30 km: $', distanceBelow30Cost, 3, 'USD')
calcAverage('Average cost for trips below 50 km: $', distanceBelow50kmCost, 3, 'USD')
calcAverage('Average cost for trips Above 30 km: $', distanceAbove30Cost, 3, 'USD')
calcProbability(len(distanceAbove30), len(tripData), 'Probability of trip being above 30km: %', 5)
calcProbability(len(distanceBelow30), len(tripData), 'Probability of trip being below 30km: %', 5)

# scatter plot for distance and money earned
plt.figure(figsize=(6, 6))
plt.scatter(distanceOfTrip, totalAmountDataFrame)
plt.scatter(distanceAbove30['trip_distance'], distanceAbove30[' total_amount'], c='r')
plt.xlabel('Distance', fontsize=14, labelpad=15)
plt.ylabel('Cost', fontsize=14, labelpad=15)
plt.show()
