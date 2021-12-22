from ratings import ratings
from data import products
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def recommendKNN(_id):
    df_data = pd.DataFrame(ratings)
    features = df_data.pivot(
        index="product_id",
        columns="user_id",
        values="rating"
    ).fillna(0)
    n =  list(features.index).index(_id)
    cm = csr_matrix(features.values)

    d = NearestNeighbors(metric="cosine", algorithm="brute")
    d.fit(cm)
    dis, ind = d.kneighbors(features.iloc[n, :].values.reshape(1,-1), n_neighbors=7)
    _products = []
    prodName = []
    distance = []

    for i in range(1, len(dis.flatten())):
        pro = list(filter(lambda pr: pr["product_id"] == features.index[ind.flatten()[i]], products))[0]['name']
        prodName.append(pro)
        _products.append(features.index[ind.flatten()[i]])
        distance.append(dis.flatten()[i])    

    m=pd.Series(_products,name='product')
    d=pd.Series(distance,name='distance')

    pr = pd.Series(prodName, name="productName")
    di = pd.Series(distance, name="p_distance")
    prdi = pd.concat([pr, di], axis=1)
    prdi = prdi.sort_values("p_distance",ascending=False)

    recommend = pd.concat([m,d], axis=1)
    recommend = recommend.sort_values('distance',ascending=False)
    recommendedP = []

    for i in range(0,recommend.shape[0]):
        pro = list(filter(lambda pr: pr["product_id"] == recommend["product"].iloc[i], products))[0]
        recommendedP.append(pro)     
    
    return recommendedP, (prdi)
