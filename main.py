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


# Trips Above 50km
distanceAbove50 = tripData.loc[tripData.trip_distance >= 50]
# Merge the medallion so I can access financial data
distanceAbove50 = distanceAbove50.merge(fareData, left_on="medallion", right_on="medallion", how="left")
distanceAbove50.to_csv("./data/dataOutput/tripsAbove50.csv")

# Trips below 30km
distanceBelow30 = tripData.loc[tripData.trip_distance <= 30]
# Merge medallion so both cost and distance are available
distanceBelow30 = distanceBelow30.merge(fareData, left_on="medallion", right_on="medallion", how="left")
distanceBelow30.to_csv("./data/dataOutput/tripsBelow30.csv")

# Trips above 50km
distanceBelow50km = tripData.loc[tripData.trip_distance <= 50]
distanceBelow50km = distanceBelow50km.merge(fareData, left_on="medallion", right_on="medallion", how="left")
distanceBelow50km.to_csv("./data/dataOutput/tripsBelow50.csv")

# Select trips that are above 30km in length
distanceAbove30 = tripData.loc[tripData.trip_distance >= 30]
# Merge the data by medallion to create a dataset with both trips >= 30 km and the cost of the trip
distanceAbove30 = distanceAbove30.merge(fareData, left_on="medallion", right_on="medallion", how="left")
distanceAbove30.to_csv("./data/dataOutput/tripsAbove30.csv")

totalAmountDataFrame = fareData[' total_amount']
distanceOfTrip = tripData['trip_distance']
distanceBelow30Cost = distanceBelow30[' total_amount']
distanceBelow50kmCost = distanceBelow50km[' total_amount']

calcAverage('Average cost for ALL trip $', totalAmountDataFrame, 3, 'USD')
calcAverage('Average distance for ALL trip', distanceOfTrip, 3, 'km')
calcAverage('Average cost for trips below 30 km: $', distanceBelow30Cost, 3, 'USD')
calcAverage('Average cost for trips below 50 km: $', distanceBelow50kmCost, 3, 'USD')

# scatter plot for distance and money earned
plt.figure(figsize=(6, 6))
plt.scatter(distanceOfTrip, totalAmountDataFrame)
plt.scatter(distanceAbove30['trip_distance'], distanceAbove30[' total_amount'], c='r')
plt.xlabel('Distance', fontsize=14, labelpad=15)
plt.ylabel('Cost', fontsize=14, labelpad=15)
plt.show()
