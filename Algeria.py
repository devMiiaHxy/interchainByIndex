from pymongo import MongoClient

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db ["Access to electricity (% of population)"]

accessToElectricity = [
    
{'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2022},
{'value': 99.7878265380859, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2021},  
{'value': 99.7187728881836, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2020} , 
{'value': 99.5, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2019},
{'value': 99.6377410888672, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2018},
{'value': 99.5300216674805, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2017},
{'value': 99.4336929321289, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2016},
{'value': 99.3561935424805, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2015},
{'value': 99.2745513916016, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2014},
{'value': 99.1879272460938, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2013}, 
{'value': 98.7646604654583, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2012}, 
{'value': 99.0026550292969, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2011}, 
{'value': 98.9109039306641, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2010},
{'value': 98.8248596191406, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2009}, 
{'value': 99.3, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2008},
{'value': 98.6852493286133, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2007}  ,
{'value': 98.7, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2006},
{'value': 98.6143188476563, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2005},
{'value': 98.608528137207, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2004},
{'value': 98.6152114868164, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2003},  
{'value': 98.6273574829102, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2002}, 
{'value': 98.6379699707031, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2001}, 
{'value': 98.6400299072266, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'DZA', 'aggregate': False, 'time': 2000}

]

x = collection.insert_many(accessToElectricity)
print (x)