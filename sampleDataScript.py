import pandas as pd
# !--Must only be run once--!
# This script must be run first to create the sample dataset that rangeConstraints.py can then use.

# The range of data that is selected
indexSelectionFare = 15000
indexSelectionTrip = 15000
# Reads the raw data and then takes a selection of this data and then saves this to
# the sample data file. These files are then read by rangeConstraints.py
try:
    wholeData = pd.read_csv('./data/FareData/trip_fare_1.csv')
    sampleData = wholeData[:indexSelectionFare]
    sampleData.to_csv("./data/sampleData/sampleDataFare.csv")
    print('1. Sample script has created sample data set [Fare]')
except:
    print('Sample script execution has failed : [Fare]')

try:
    wholeDataTrip = pd.read_csv('./data/TripData/trip_data_1.csv')
    sampleDataTrip = wholeDataTrip[:indexSelectionTrip]
    sampleDataTrip.to_csv("./data/sampleData/sampleDataTrip.csv")
    print('2. Sample script has created sample data set [Trip]')
except:
    print('Sample script execution has failed : [Trip]')
