# -*- coding: utf-8 -*-
"""Varun Saini Food wastage.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CjoQBk6yiRI6rcsg3o7vU9i8_bHfV4I1
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn as sklearn
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import math

url = '/content/FoodWasteData.csv'
df = pd.read_csv(url)

df.head()

df.drop(["geographicaream49", "measureditemcpc", "method_datacollection", "tag_datacollection", "reference", "url"], axis = 1, inplace = True)
df.drop(["region", "percentage_loss_of_quantity"], axis = 1, inplace = True)
df.head()

df.drop(["loss_quantity", "loss_qualitiative", "loss_monetary", "periodofstorage", "treatment", "samplesize", "units", "causeofloss"], axis = 1, inplace = True)
df.head()

df = df.rename(columns={"timepointyears": "year", "loss_per_clean": "percent_lost", "activity": "activity_when_lost"})
df = df.rename(columns={"fsc_location1": "location_of_loss"})
df.head()

df = df.replace(float('nan'), "Unknown")
df.head()

x = df["year"]
y = df["percent_lost"]
plt.plot(x,y,'o', color='black')
plt.title("Percent Food Lost Versus Year Scatter Plot")
plt.xlabel("Year")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

df.drop(df[df["year"] < 1960].index, inplace = True)
x = df["year"]
y = df["percent_lost"]
plt.plot(x,y,'o', color='black')
plt.title("Percent Food Lost Versus Year Scatter Plot")
plt.xlabel("Year")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

decades = []
for year in df["year"]:
    decade = year/10
    decade = math.trunc(decade)
    decade = decade*10
    decades.append(decade)
#Make new column in df that has decade
df["decade"] = decades
#Run through each decade and add percent lost with that decade to different index of decade_groups
decade_groups = []
decade = 1960
while (decade < 2020):
    decade_groups.append(df[df["decade"] == decade]["percent_lost"])
    decade = decade + 10
#make typed np array to allow boxplot to work
decade_groups = np.array(decade_groups, dtype="object")
plt.boxplot(decade_groups)
#Rename x axis markings
plt.xticks([1, 2, 3, 4, 5, 6], ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s"])
plt.title("Percent Food Lost Versus Decade Box Plot")
plt.xlabel("Decade")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

plt.hist(df["year"])
plt.title("Number of Incidents Versus Year Histogram")
plt.xlabel("Year")
plt.ylabel("Number of Food Loss Incidents")
plt.show()

x = df["crop"]
y = df["percent_lost"]
plt.plot(x,y,'o', color='black')
plt.title("Percent Food Lost Versus Lost Crops Scatter Plot")
plt.xlabel("Crop")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

crop_data = []
crops = []
for crop in df["crop"]:
    #Is it a new crop
    if crop not in crops:
        crops.append(crop)
        #Add data of new crop to dataset
        crop_data.append(df[df["crop"] == crop])
#Find the ten crops with the highest number of entries
k = 0
ten_crops = []
#Run 10 times
while k < 10:
    #Find data with the max length in crop dataset
    max = len(crop_data[0])
    mi = 0
    i = 0
    while i < len(crop_data):
        if len(crop_data[i]) > max:
            #New max found
            max = len(crop_data[i])
            mi = i
        i = i + 1
    #Add max length crop to set of ten
    ten_crops.append(crop_data[mi])
    #Remove added crop so that it wont be found next run of loop
    del crop_data[mi]
    k = k + 1
i = 0
#Make plot bigger
fig= plt.figure(figsize=(10,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
#Plot each crop in max ten
while i < 10:
    x = ten_crops[i]["crop"]
    y = ten_crops[i]["percent_lost"]
    axes.plot(x,y,'o', color='black')
    i = i + 1
plt.title("Percent Food Lost Versus Top 10 Lost Crops Scatter Plot")
plt.xlabel("Crop")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

crop_groups = []
i = 0
while (i < 10):
    crop_groups.append(ten_crops[i]["percent_lost"])
    i = i + 1
#make typed np array to allow boxplot to work
crop_groups = np.array(crop_groups, dtype="object")
#Make plot bigger
fig= plt.figure(figsize=(10,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.boxplot(crop_groups)
#Rename x axis markings
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["Maize (corn)", "Rice", "Millet", "Sorghum", "Wheat", "Potatoes", "Barley", "Fonio", "Tomatoes", "Cabbages"])
plt.title("Percent Food Lost Versus Top 10 Lost Crops Box Plot")
plt.xlabel("Crop")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

country_data = []
countries = []
for country in df["country"]:
    #Is it a new country
    if country not in countries:
        countries.append(country)
        #Add data of new country to dataset
        country_data.append(df[df["country"] == country])
#Find the ten countries with the highest number of entries
k = 0
ten_countries = []
#Run 10 times
while k < 10:
    #Find data with the max length in country dataset
    max = len(country_data[0])
    mi = 0
    i = 0
    while i < len(country_data):
        if len(country_data[i]) > max:
            max = len(country_data[i])
            mi = i
        i = i + 1
    #Add max length country to set of ten
    ten_countries.append(country_data[mi])
    #Remove added country so that it wont be found next run of loop
    del country_data[mi]
    k = k + 1
i = 0
#Make plot bigger
fig= plt.figure(figsize=(10,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
#Plot each country in max ten
while i < 10:
    x = ten_countries[i]["country"]
    y = ten_countries[i]["percent_lost"]
    axes.plot(x,y,'o', color='black')
    i = i + 1
plt.title("Percent Food Lost Versus Top 10 Countries Scatter Plot")
plt.xlabel("Country")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

country_groups = []
i = 0
while (i < 10):
    country_groups.append(ten_countries[i]["percent_lost"])
    i = i + 1
#make typed np array to allow boxplot to work
country_groups = np.array(country_groups, dtype="object")
#Make plot bigger
fig= plt.figure(figsize=(10,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.boxplot(country_groups)
#Rename x axis markings
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["Peru", "Turkey", "India", "Ghana", "Malawi", "Ethiopia", "Bangladesh", "Togo", "Mali", "Uganda"])
plt.title("Percent Food Lost Versus Top 10 Countries Box Plot")
plt.xlabel("Country")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

activity_data = []
activities = []
for activity in df["activity_when_lost"]:
    #Is it a new activity
    if activity not in activities and activity != "Unknown":
        activities.append(activity)
        #Add data of new activity to dataset
        activity_data.append(df[df["activity_when_lost"] == activity])
#Find the ten activites with the highest number of entries
k = 0
ten_activities = []
#Run 10 times
while k < 10:
    #Find data with the max length in activity dataset
    max = len(activity_data[0])
    mi = 0
    i = 0
    while i < len(activity_data):
        if len(activity_data[i]) > max:
            max = len(activity_data[i])
            mi = i
        i = i + 1
    #Add max length activity to set of ten
    ten_activities.append(activity_data[mi])
    #Remove added activity so that it wont be found next run of loop
    del activity_data[mi]
    k = k + 1
i = 0
#Make plot bigger
fig= plt.figure(figsize=(19,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
#Plot each activity in max ten
while i < 10:
    x = ten_activities[i]["activity_when_lost"]
    y = ten_activities[i]["percent_lost"]
    axes.plot(x,y,'o', color='black')
    i = i + 1
plt.title("Percent Food Lost Versus Top 10 Activities When Lost Scatter Plot")
plt.xlabel("Activity of Food When Loss Occured")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

#Create a dataset for each unique location
location_data = []
locations = []
for location in df["location_of_loss"]:
    #Is it a new location
    if location not in locations and location != "Unknown" and location != "SWS_Total":
        locations.append(location)
        #Add data of new location to dataset
        location_data.append(df[df["location_of_loss"] == location])
#Find the ten locations with the highest number of entries
k = 0
ten_locations = []
#Run 10 times
while k < 10:
    #Find data with the max length in location dataset
    max = len(location_data[0])
    mi = 0
    i = 0
    while i < len(location_data):
        if len(location_data[i]) > max:
            max = len(location_data[i])
            mi = i
        i = i + 1
    #Add max length location to set of ten
    ten_locations.append(location_data[mi])
    #Remove added location so that it wont be found next run of loop
    del location_data[mi]
    k = k + 1
i = 0
#Make plot bigger
fig= plt.figure(figsize=(19,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
#Plot each location in max ten
while i < 10:
    x = ten_locations[i]["location_of_loss"]
    y = ten_locations[i]["percent_lost"]
    axes.plot(x,y,'o', color='black')
    i = i + 1
plt.title("Percent Food Lost Versus Top 10 Locations of Loss Scatter Plot")
plt.xlabel("Location of Loss")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

activity_groups = []
activity_names = []
i = 0
while (i < 10):
    #Get name of each top ten activity
    for name in ten_activities[i]["activity_when_lost"]:
        activity_names.append(name)
        break;
    activity_groups.append(ten_activities[i]["percent_lost"])
    i = i + 1
#make typed np array to allow boxplot to work
activity_groups = np.array(activity_groups, dtype="object")
#Make plot bigger
fig= plt.figure(figsize=(19,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.boxplot(activity_groups)
#Rename x axis markings
plt.title("Percent Food Lost Versus Top 10 Activities When Lost Box Plot")
plt.xlabel("Activity of Food When Loss Occured")
plt.ylabel("Percent Food Lost in Incident")
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], activity_names)
plt.show()

#Run through each of 10 locations and add percent lost data with that location to different index of array
location_groups = []
location_names = []
i = 0
while (i < 10):
    #Get name of each top ten location
    for name in ten_locations[i]["location_of_loss"]:
        location_names.append(name)
        break;
    location_groups.append(ten_locations[i]["percent_lost"])
    i = i + 1
#make typed np array to allow boxplot to work
location_groups = np.array(location_groups, dtype="object")
#Make plot bigger
fig= plt.figure(figsize=(19,5))
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.boxplot(location_groups)
#Rename x axis markings
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], location_names)
plt.title("Percent Food Lost Versus Top 10 Locations of Loss Box Plot")
plt.xlabel("Location of Loss")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

x = df["decade"]
y = df["percent_lost"]
X = np.array(x).reshape(-1, 1)
y2 = np.array(y).reshape(-1, 1)
#Run regression and predict an output
reg = LinearRegression().fit(X, y2)
Y = reg.predict(X)
#Plot the output against the original data
plt.plot(x, y, 'o', color='black')
plt.plot(X, Y, color ='k')
plt.title("Percent Food Lost Versus Year Linear Regression")
plt.xlabel("Year")
plt.ylabel("Percent Food Lost in Incident")
plt.show()

crops = ["Potatoes", "Tomatoes", "Cabbages"]
countries = ["Peru", "Turkey", "Ghana"]
activities = ["Sorting/Grading", "Harvesting/field drying", "Farm storage"]
locations = ["WholeSupplyChain", "Retail", "Export"]
groups = [crops, countries, activities, locations]
#Set up array of column names
group_labels = ["crop", "country", "activity_when_lost", "location_of_loss"]
i = 0
for group in groups:
    for name in group:
        #Take the appropriate year and percent lost columns and reshape them for regression
        x = df[df[group_labels[i]] == name]["year"]
        y = df[df[group_labels[i]] == name]["percent_lost"]
        X = np.array(x).reshape(-1, 1)
        y2 = np.array(y).reshape(-1, 1)
        #Run regression and predict an output
        reg = LinearRegression().fit(X, y2)
        Y = reg.predict(X)
        #Plot the output against the original data
        plt.plot(x, y, 'o', color='black')
        plt.plot(X, Y, color ='k')
        plt.title("Percent Food Lost Versus Year for " + name + " Linear Regression")
        plt.xlabel("Year")
        plt.ylabel("Percent Food Lost in Incident")
        plt.show()
    i = i + 1

