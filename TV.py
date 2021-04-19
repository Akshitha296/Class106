import plotly.express as px
import csv
import numpy as np

def plotFigure(datapath):
    with open(datapath) as csv_file:
        df = csv.DictReader(csv_file) 
        fig = px.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(datapath):
    tv_size = []
    time = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tv_size.append(float(row["Size of TV"]))
            time.append(float(row["Average time spent watching TV in a week (hours)"]))
    return{"x": tv_size, "y": time}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between size and time is: \n", correlation[0,1])

def main():
    datapath = "TV.csv"

    plotFigure(datapath)
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

main()