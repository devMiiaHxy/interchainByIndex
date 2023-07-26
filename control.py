import wbgapi as wb
import numpy as np
import scipy as sc
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data,
				columns = data.feature_names)

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#job = wb.data.DataFrame(['NY.GDP.PCAP.CD', 'SP.POP.TOTL'], 'AGO', mrv=50)
#print(job)

drip = wb.data.DataFrame('SP.POP.TOTL', wb.region.members('AFR'), range(1960, 2020, 1))
print(drip)

#cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

#db = cluster["Afrca"]
#collection = db["Angola"]

#y = collection.insert_many(x)
#print(y)