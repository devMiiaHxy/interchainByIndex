from pymongo import MongoClient

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db ["Access to electricity (% of population)"]

accessToElectcrity = [
    
{'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2022'},
{'value': 73.7259063720703, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2021'},
{'value': 71.8291244506836, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2020'},
{'value': 70.095085144043, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2019'},  
{'value': 68.2547378540039, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2018'},  
{'value': 67.4, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2017'},
{'value': 64.2029647827148, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2016'},
{'value': 62.13, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2015'},
{'value': 60.0222434997559, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2014'},  
{'value': 57.972297668457, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2013'}, 
{'value': 55.9656753540039, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2012'},  
{'value': 53.24, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2011'},
{'value': 52.0336112976074, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2010'}  ,
{'value': 43.36, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2009'},
{'value': 44.5, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2008'},
{'value': 41.9153594970703, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2007'},
{'value': 39.6760482788086, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2006'}, 
{'value': 37.457576751709, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2005'}, 
{'value': 35.2583618164063, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2004'},  
{'value': 33.0716171264648, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2003'}, 
{'value': 27, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2002'},
{'value': 24.8, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2001'},
{'value': 26.5161628723145, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR2000'},
{'value': 25.0527400970459, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1999'}, 
{'value': 22.8273296356201, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1998'}, 
{'value': 20.5970783233643, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1997'}, 
{'value': 18.3627471923828, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1996'}, 
{'value': 16.1250171661377, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1995'}, 
{'value': 13.8845663070679, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1994'}, 
{'value': 11.6420764923096, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1993'}, 
{'value': 9.39822673797607, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'BWA', 'aggregate': False, 'time': 'YR1992'}

]

f =collection.insert_many(accessToElectcrity)
print(f)