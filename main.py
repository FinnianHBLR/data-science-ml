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

plt.figure(figsize=(6, 6))
plt.scatter(distanceOfTrip, totalAmountDataFrame)
plt.xlabel('Distance', fontsize=14, labelpad=15)
plt.ylabel('Cost', fontsize=14, labelpad=15)
plt.show()


# scatter plot for distance and money earned


