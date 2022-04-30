import matplotlib.pyplot as plt

# The boundaries of the image map
map_box = [-74.3307, -73.6765, 40.4961, 40.9768]
# The name of the image of the New York map might be different.
map_img = plt.imread('map (6).png')
fig, ax = plt.subplots()

import pandas as pd

try:
    fareData = pd.read_csv('C:\\Users\\alyth\\Documents\\GitHub\\data-science-ml\\data\\sampleData\\sampleDataFare.csv')
    tripData = pd.read_csv('C:\\Users\\alyth\\Documents\\GitHub\\data-science-ml\\data\\sampleData\\sampleDataTrip.csv')
    print('Successful data import')
except:
    print("Error [Check data exists in file location]")

tripData = tripData.loc[tripData["pickup_latitude"] > 40.4961,]
tripData = tripData.loc[tripData["pickup_latitude"] < 40.9768,]


plat = tripData['pickup_latitude']
plong = tripData['pickup_longitude']


center = 40.6958

pnorth = plat.loc[plat > center,]
psouth = plat.loc[plat < center,]

print(str(pnorth.count()/plat.count() * 100)+ "%" + " of taxi rides were in the north of nyc")
print(str(psouth.count()/plat.count() * 100)+ "%" + " of taxi rides were in the south of nyc")

ax.scatter(plong, plat,s = 1)
ax.set_ylim(map_box[2], map_box[3])
ax.set_xlim(map_box[0], map_box[1])
plt.axhline(40.6958, color='r', linestyle='-')

ax.imshow(map_img, extent=map_box, alpha=0.9)

plt.savefig("map_small.png")
fig.savefig("map_big.png", format="png", dpi=1200)
plt.show()