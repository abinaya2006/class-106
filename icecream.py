import plotly_express as px
import csv 

'''
with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as a:
    df=csv.DictReader(a)

    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales( â‚¹ )")
    fig.show()

'''

with open("cups of coffee vs hours of sleep.csv") as a:
    df=csv.DictReader(a)

    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()