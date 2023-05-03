import pandas as pd
import matplotlib.pyplot as plt

# Read the data do not remove the C:/ or / when filling in the path. you have to use / insted of windows standard \
sti='C:/the path to the file on your computer or network drive'
fil='/file_name'
df = pd.read_csv(sti+fil, delimiter=";",decimal=",",na_values="---")
print(df)

# Convert the datetime column to a datetime data type
df["Dato og tid"] = pd.to_datetime(df["Dato og tid"], format="%d.%m.%Y %H:%M")

# Set the datetime column as the index
df.set_index("Dato og tid", inplace=True)
#in the bracket under you can limit the colums by adding numbers like this exmp: [2913:3274] this example only works if you have the orignal file
#this will limit it til september the first to oktober the first ofc. you can change this to fit your time frame or colum size but does not need to be defined
df=df[:]
#printer df slik at du kan se hvordan csv filen ser ut
print(df)
# Plot the temperature data the name is the of the top row is the colum
df["Tempu"].plot(figsize=(12,6))
plt.title("Temperature over Time")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()

#plots a twin axis temp and fukt
fig, ax1 = plt.subplots(figsize=(10,10))  
ax2 = ax1.twinx()
ax1.plot(df["Tempu"])
ax2.plot(df["Relativ fuktighet"], color='orange')
ax1.set_ylabel('Temperatur inne')
ax2.set_ylabel('Fuktighet inne')
plt.show()

#plots a twin axis 1 axis temp and fukt 2 axis duggpunkt
fig, ax1 = plt.subplots(figsize=(10,6))
ax2 = ax1.twinx()
ax1.plot(df["Tempu"], label='Temperatur')
ax1.plot(df["Relativ fuktighet"], color='orange', label='Fuktighet')
ax2.plot(df["Duggpunkt"], color='green', label='Duggpunkt')
ax1.set_ylabel('Temperatur og fuktighet inne')
ax2.set_ylabel('Duggpunkt inne')
ax1.legend(loc='upper left')
ax2.legend()
plt.show()
#plots a scatter of fuktighet and duggpunkt
plt.scatter(df["Relativ fuktighet"],df["Duggpunkt"])
plt.ylabel('Fuktighet inne')
plt.xlabel('Duggpunkt inne')
plt.show()
#adds in library for colors maps
from matplotlib import cm 
#plots a scatter of fuktighet and duggpunkt with colors
cmap = cm.get_cmap('inferno', len(df.index))
colors = range(len(df.index))
ax=plt.axes()
sc=ax.scatter(df["Relativ fuktighet"],df["Duggpunkt"],c=colors,cmap=cmap,vmin=0, vmax=len(df.index))
plt.colorbar(sc, label='tid-index') 
plt.ylabel('Duggpunkt inne')
plt.xlabel('Fuktighet inne')
plt.show()

