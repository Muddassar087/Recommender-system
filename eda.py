from ratings import ratings
import pandas as pd
import matplotlib.pyplot as plt

def ratingdataInfo():
    data = pd.DataFrame(ratings)
    print(data.describe)

def dataTypes():
    data = pd.DataFrame(ratings)
    print(data.dtypes)

def ratingbyuserid():
    data = pd.DataFrame(ratings)
    n = data.groupby(by='user_id')['rating'].count().sort_values(ascending=False)
    print(n.head(10))

def _plot():
    data = pd.DataFrame(ratings)
    n = data.groupby("product_id")['rating'].count().sort_values(ascending=False)
    fig = plt.figure(figsize=plt.figaspect(.5))
    ax = plt.gca()
    plt.plot(n.values)
    plt.title('# RATINGS per Product')
    plt.xlabel('Product')
    plt.ylabel('No of ratings per product')
    ax.set_xticklabels([])
    plt.show()
