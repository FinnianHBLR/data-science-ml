from scipy.stats import gaussian_kde
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import preprocessing

def calculateHighestTiploc():
    # Thanks to Aly!

    fareData = pd.read_csv("./sampleDataFare.csv")
    tripData = pd.read_csv("./sampleDataTrip.csv")

    # The boundaries of the image map
    map_box = [-74.3307, -73.6765, 40.4961, 40.9768]
    # The name of the image of the New York map might be different.
    map_img = plt.imread('map (6).png')
    fig, ax = plt.subplots()
    # Just for NYC
    tripData = tripData.loc[tripData["pickup_latitude"] > 40.4961,]
    tripData = tripData.loc[tripData["pickup_latitude"] < 40.9768,]
    # Add the datasets together.
    concatenated = pd.concat([fareData, tripData], axis=1, join='inner').copy()

    # Normalization typically means rescales the values into a range of [0,1].
    x = np.array(concatenated[' tip_amount'].values).reshape(-1,1)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normalisedData = pd.DataFrame(x_scaled)

    # Using this for scale.
    ax.scatter(concatenated['pickup_longitude'], concatenated['pickup_latitude'], s=20, c=(normalisedData*255), cmap='tab20')

    ax.set_ylim(map_box[2], map_box[3])
    ax.set_xlim(map_box[0], map_box[1])
    ax.imshow(map_img, extent=map_box, alpha=0.9)

    plt.show()

if __name__ == '__main__':
    calculateHighestTiploc()