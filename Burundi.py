from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db["Access to electricity (% of population)"]

accessToElectricity = [
{'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2022'},
{'value': 10.2338275909424, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2021'},
{'value': 9.1, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2020'},
{'value': 9.83940029144287, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2019'},
{'value': 9.50929260253906, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2018'},
{'value': 9.3, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2017'},
{'value': 8.47799873352051, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2016'},
{'value': 7.89011478424072, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2015'},
{'value': 7, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2014'},
{'value': 6.9, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2013'},
{'value': 6.5, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2012'},
{'value': 6.15572309494019, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2011'},
{'value': 5.3, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2010'},
{'value': 5.38613891601563, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2009'},
{'value': 4.8, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2008'},
{'value': 4.65474510192871, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2007'},
{'value': 2.66, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2006'},
{'value': 3.20731707317073, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2005'},
{'value': 3.69034385681152, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2004'},
{'value': 3.40113353729248, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2003'},
{'value': 2.83210754394531, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2001'},
{'value': 2.53827786445618, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR2000'},
{'value': 2.07094931602478, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BDI', 'aggregate': False, 'time': 'YR1999'},

]

xv = collection.insert_many(accessToElectricity)
print (xv)