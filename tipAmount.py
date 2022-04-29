from scipy.stats import gaussian_kde
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def runCode():
    from sklearn import linear_model

    # Access data. Sort of done weird, I know. Better code is in the tip0Distance0Run(), use that for reference!.
    fareData = pd.read_csv("./sampleDataFare.csv")
    tripData = pd.read_csv("./sampleDataTrip.csv")

    fareDataAbove0 = pd.read_csv("./sampleDataFare.csv")
    tripDataAbove0 = pd.read_csv("./sampleDataTrip.csv")

    print(f'LOADED FAREDATA \n {fareData.head()} \n AND TRIP DATA \n {tripData.head()}')
    print(f'ACCESSING FIRST FARE: \n {fareData.iloc[0]}')
    print(f'ACCESSING FIRST TRIP: \n {tripData.iloc[0]}')

    # For travel that is more than 0, then that is removed and connected back together. It works, but could use some work tbh.
    distanceAbove0 = tripData.loc[tripData.trip_distance > 0]
    fareDataAbove0.drop(distanceAbove0.index, axis=0, inplace=True)
    tripDataAbove0.drop(distanceAbove0.index, axis=0, inplace=True)
    travelMoreThan0Removed = pd.concat([fareDataAbove0, tripDataAbove0], axis=1, join='inner')

    # Finds distance == 0, then removes it. Main code being used, ONLY EXCLUDING 0 DISTANCE FOR PROCESSING.
    distance0 = tripData.loc[tripData.trip_distance == 0]
    tripData.drop(distance0.index, axis=0, inplace=True)
    fareData.drop(distance0.index, axis=0, inplace=True)
    joinedData = pd.concat([fareData, tripData], axis=1, join='inner')
    # Save data.
    joinedData.to_csv("concatenatedTripAndFare.csv")

    # Reshaped data.
    xData = np.array(joinedData['trip_distance']).reshape(-1,1)
    yData = np.array(joinedData[' tip_amount']).reshape(-1,1)

    # Flattened data.
    faltX = xData.flatten()
    faltY = yData.flatten()

    # LinearRegression
    model = linear_model.LinearRegression()
    model.fit(xData, yData)
    print(model.coef_)
    print(model.intercept_)

    x_plot = np.arange(0, 35)
    x_plot = x_plot.reshape(-1, 1)
    y_predicted = model.predict(x_plot)

    # polyfit
    linear_model = np.polyfit(faltX, faltY, 2)
    linear_model_fn = np.poly1d(linear_model)
    x_s = np.arange(0, 35)

    # gaussian distance density.
    xy = np.vstack([faltX, faltY])
    z = gaussian_kde(xy)(xy)

    # Plot labels, data from linear regression model.
    plt.title(f'Tip amount including no tip. {round(model.coef_[0][0],2)} coefficient.')
    plt.xlabel("Distance")
    plt.ylabel("Tip amount")
    # Scatter processed data.
    plt.scatter(joinedData['trip_distance'], joinedData[' tip_amount'], c=z, s=10,)
    plt.scatter(travelMoreThan0Removed['trip_distance'], travelMoreThan0Removed[' tip_amount'], c='red', s=10)
    plt.plot(x_plot, y_predicted, color='cyan')
    plt.plot(x_s, linear_model_fn(x_s), color="green")
    plt.show()

    print(f'HERE \n {joinedData.columns}')

def tip0Distance0Run():
    # This code is much better than the code written above!!
    from sklearn import linear_model

    fareDataWTip = pd.read_csv("./sampleDataFare.csv")
    tripDataWTip = pd.read_csv("./sampleDataTrip.csv")
    # Concatenated files
    concatenated = pd.concat([fareDataWTip, tripDataWTip], axis=1, join='inner').copy()
    # Processed data. tip0Distance0 includes all data that has no tip and has no distance.
    tip0Distance0 = concatenated.loc[(concatenated[' tip_amount'] == 0) | (concatenated.trip_distance == 0)].copy()
    # Processed data. Only processes data has a tip and has a distance.
    moreThan0 =  concatenated.loc[((concatenated[' tip_amount'] > 0) & (concatenated.trip_distance > 0))]

    # Processing - reshaping arrays.
    xData = np.array(moreThan0['trip_distance']).reshape(-1, 1)
    yData = np.array(moreThan0[' tip_amount']).reshape(-1, 1)
    faltX = xData.flatten()
    faltY = yData.flatten()
    # Linear regression model
    model = linear_model.LinearRegression()
    model.fit(xData, yData)
    print(model.coef_)
    print(model.intercept_)

    x_plot = np.arange(0, 35)
    x_plot = x_plot.reshape(-1, 1)
    y_predicted = model.predict(x_plot)
    # Polyfit model.
    linear_model = np.polyfit(faltX, faltY, 2)
    linear_model_fn = np.poly1d(linear_model)
    x_s = np.arange(0, 35)

    # Gaussian distance density.
    xy = np.vstack([moreThan0['trip_distance'], moreThan0[' tip_amount']])
    z = gaussian_kde(xy)(xy)
    # Plot labels, data from linear regression model.
    plt.title(f'Tip amount excluding no tip. {round(model.coef_[0][0],2)} coefficient.')
    plt.xlabel("Distance")
    plt.ylabel("Tip amount")
    # Scatter processed data.
    plt.scatter(tip0Distance0['trip_distance'], tip0Distance0[' tip_amount'], s=10, c='red')
    # c is the gaussian calculation
    plt.scatter(moreThan0['trip_distance'], moreThan0[' tip_amount'], s=10, c=z)
    # Plot model lines.
    plt.plot(x_plot, y_predicted, color='cyan')
    plt.plot(x_s, linear_model_fn(x_s), color="green")
    plt.show()

if __name__ == '__main__':
    runCode()
    tip0Distance0Run()
