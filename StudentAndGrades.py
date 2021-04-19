import plotly.express as px
import csv
import numpy as np

def plotFigure(datapath):
    with open(datapath) as csv_file:
        df = csv.DictReader(csv_file) 
        fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        fig.show()

def getDataSource(datapath):
    present_days = []
    grade = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            present_days.append(float(row["Days Present"]))
            grade.append(float(row["Marks In Percentage"]))
    return{"x": present_days, "y": grade}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between present days and grades are: \n", correlation[0,1])

def main():
    datapath = "StudentAndGrades.csv"

    plotFigure(datapath)
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

main()