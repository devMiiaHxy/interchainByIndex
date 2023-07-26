from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db["Access to electricity (% of population)"]

accessToElectricity = [
    {'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2022'},
{'value': 41.9736328125, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2021'},
{'value': 40.9859313964844, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2020'},
{'value': 39.9980926513672, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2019'},
{'value': 39.0094223022461, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2018'},
{'value': 34.5, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2017'},
{'value': 37.0262756347656, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2016'},
{'value': 29.62, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2015'},
{'value': 34.1, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2014'},
{'value': 34.6536293029785, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2013'},
{'value': 38.4, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2012'},
{'value': 36.9, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2011'},
{'value': 34.2, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2010'},
{'value': 29.9869403839111, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2009'},
{'value': 28.9918003082275, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2008'},
{'value': 28.0100479125977, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2007'},
{'value': 27.9, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2006'},
{'value': 26.1018295288086, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2005'},
{'value': 25.177396774292, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2004'},
{'value': 24.2654361724854, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2003'},
{'value': 23.3589420318604, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2002'},
{'value': 21.9, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2001'},
{'value': 21.534330368042, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR2000'},
{'value': 20.5620422363281, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR1999'},
{'value': 19.578254699707, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR1998'},
{'value': 18.5896263122559, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BEN', 'aggregate': False, 'time': 'YR1997'},

]

ty = collection.insert_many(accessToElectricity)
print (ty)