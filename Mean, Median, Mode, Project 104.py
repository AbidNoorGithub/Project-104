import pandas as pd
import plotly_express as px
import csv
import statistics as s
import colorama
from colorama import Fore 
colorama.init()

weight = []
height = []

with open("SampleGraph.csv") as csv_file:
    Graph = csv.DictReader(csv_file)

    for row in Graph:
        weight.append(float(row["Weight"]))
        height.append(float(row["Height"]))

meanOfWeight = s.mean(weight)
meanOfHeight = s.mean(height)

medianOfWeight = s.median(weight)
medianOfHeight = s.median(height)

modeOfWeight = s.mode(weight)
modeOfHeight = s.mode(height)

print(Fore.RED + "The mean of the weight and height is: " + Fore.BLUE + str(meanOfWeight) + Fore.RED + " and " + Fore.BLUE + str(meanOfHeight))

print(Fore.RED + "The median of the weight and height is: " + Fore.BLUE + str(medianOfWeight) + Fore.RED + " and " + Fore.BLUE + str(medianOfHeight))

print(Fore.RED + "The mode of the weight and height is: " + Fore.BLUE + str(modeOfWeight) + Fore.RED + " and " + Fore.BLUE + str(modeOfHeight))
    