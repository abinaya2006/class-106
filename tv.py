import plotly_express as px
import csv
import numpy as np

'''
with open ("Size of TV,_Average time spent watching TV in a week (hours).csv") as file_data:
    df=csv.DictReader(file_data)

    fig=px.scatter(df,x="Size of TV",y="\tAverage time spent watching TV in a week (hours)")
    fig.show()
'''

def getDataSource(data_path):
    size_of_tv=[]
    average_time_spent=[]

    with open(data_path) as a:
        df=csv.DictReader(a)

        for row in df:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
        
    return {"x":size_of_tv,"y":average_time_spent}


def find_correlation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("Correlation between size of tv and average time spent : ",correlation[0,1] )

def setup():
    data_path="Size of TV,_Average time spent watching TV in a week (hours).csv"
    data=getDataSource(data_path)
    find_correlation(data)

setup()