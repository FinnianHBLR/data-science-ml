import pandas as pd
import matplotlib.pyplot as plt

try:
    fareData = pd.read_csv('./data/sampleData/sampleDataFare.csv')
    tripData = pd.read_csv('./data/sampleData/sampleDataTrip.csv')
    print('Successful data import')
except:
    print("Error [Check data exists in file location]")

totalAmountDataFrame = fareData[' total_amount']
distanceOfTrip = tripData['trip_distance']


def calculateAvgCost(totalAmount):
    print(f'Average cost per trip + {totalAmount.mean()}')

def calculateAvgDistance(distances):
    print(f'Average distance per trip + {distances.mean()}')

calculateAvgCost(totalAmountDataFrame)
calculateAvgDistance(distanceOfTrip)

# Select trips that are above 30km in length
distanceAbove30 = tripData.loc[tripData.trip_distance >= 30]
# Merge the data by medallion to create a dataset with trips > 30 with the cost of the trip
distanceAbove30 = distanceAbove30.merge(fareData, left_on="medallion", right_on="medallion", how="left")
distanceAbove30.to_csv("./data/sampleData/tripsOver30.csv")

plt.figure(figsize=(6, 6))
plt.scatter(distanceOfTrip, totalAmountDataFrame)
plt.scatter(distanceAbove30['trip_distance'], distanceAbove30[' total_amount'], c='r')
plt.xlabel('Distance', fontsize=14, labelpad=15)
plt.ylabel('Cost', fontsize=14, labelpad=15)
plt.show()


# scatter plot for distance and money earned


