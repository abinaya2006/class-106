import plotly_express as px
import csv 
import numpy as np

def getDataSource(data_path):
    ice_cream_sales=[]
    temperature=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        fig=px.scatter(csv_reader,x="Temperature",y="Ice-cream Sales( â‚¹ )")
        fig.show()
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))

    
    return {"x":temperature,"y":ice_cream_sales}

def find_correlation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between temperature and icecream sales: ",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source=getDataSource(data_path)
    find_correlation(data_source)

setup()


