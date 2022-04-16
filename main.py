import pandas as pd

try:
    fareData = pd.read_csv('./data/sampleData/sampleDataFare.csv')
    tripData = pd.read_csv('./data/sampleData/sampleDataTrip.csv')
    print('Successful data import')
except:
    print("Error [Check data exists in file location]")

print(fareData)