from pymongo import MongoClient

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db ["Access to electricity (% of population)"]

accessToElectricity = [
    
{'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2022'},
{'value': 18.9506874084473, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2021'},
{'value': 18.4672794342041, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2020'},
{'value': 17.6, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2019'},
{'value': 14.4, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2018'},
{'value': 17.0133209228516, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2017'},
{'value': 16.5673961639404, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2016'},
{'value': 16.1532001495361, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2015'},
{'value': 19.2, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2014'},
{'value': 15.3885135650635, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2013'},
{'value': 15.0658206939697, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2012'},
{'value': 14.7755994796753, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2011'},
{'value': 13.1, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2010'},
{'value': 12.63, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2009'},
{'value': 12.5246601104736, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2008'},
{'value': 12.0471992492676, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2007'}, 
{'value': 11.5869636535644, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2006'}, 
{'value': 11.1475677490234, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2005'},
{'value': 10.7274255752563, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2004'}, 
{'value': 11.4, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2003'},
{'value': 9.91755771636963, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2002'},
{'value': 9.51381778717041, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2001'}, 
{'value': 9.10153102874756, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR2000'}, 
{'value': 6.9, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1999'},
{'value': 8.10726451873779, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1998'},
{'value': 7.61713981628418, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1997'}, 
{'value': 7.1229362487793, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1996'}, 
{'value': 6.62533283233643, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1995'},  
{'value': 6.12501001358032, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BFA', 'aggregate': False, 'time': 'YR1994'} 

]

d = collection.insert_many(accessToElectricity)
print(d)