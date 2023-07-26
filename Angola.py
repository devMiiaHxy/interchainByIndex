from pymongo import MongoClient

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://meetmiiah:dc1lQnMTpGgpNLVK@cluster0.jgp6wj0.mongodb.net/?retryWrites=true&w=majority")

db = cluster["africaIndicators"]
collection = db ["Access to electricity (% of population)"]

angolaGDP = [
{'value': 2998.50115810921, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2022},
{'value': 1903.71740495688, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2021},
{'value': 1502.95075414518, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2020},
{'value': 2142.23875712854, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2019},
{'value': 2487.50099555267, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2018},
{'value': 2283.21423255725, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2017},
{'value': 1709.51553404553, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2016},
{'value': 3100.83068530533, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2015},
{'value': 5059.08044128816, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2014},
{'value': 5101.98387641128, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2013},
{'value': 4962.55207190082, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2012},
{'value': 4511.15322719034, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2011},
{'value': 3496.78479608032, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2010},
{'value': 3123.69889829937, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2009},
{'value': 4081.71749719537, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2008},
{'value': 3121.34873520681, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2007},
{'value': 2597.96358484271, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2006},
{'value': 1900.7238165071, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2005},
{'value': 1254.69612612243, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2004},
{'value': 982.805589644709, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2003},
{'value': 872.657638045899, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2002},
{'value': 527.464118489685, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2001},
{'value': 556.88424373456, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 2000},
{'value': 387.689414798423, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1999},
{'value': 423.393452775682, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1998},
{'value': 514.309886597359, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1997},
{'value': 523.310909069442, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1996},
{'value': 399.73555844781, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1995},
{'value': 251.856499216203, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1994},
{'value': 847.653799281656, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1993},
{'value': 1196.46496180871, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1992},
{'value': 1038.91401921854, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1991},
{'value': 949.349840556856, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1990},
{'value': 891.803204709644, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1989},
{'value': 792.914088450066, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1988},
{'value': 755.972444720059, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1987},
{'value': 684.489277182734, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1986},
{'value': 757.632389208355, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1985},
{'value': 637.519759416351, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1984},
{'value': 623.533932500336, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1983},
{'value': 620.363109508475, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1982},
{'value': 643.052851443849, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1981},
{'value': 711.941169235015, 'series': 'NY.GDP.PCAP.CD', 'economy': 'AGO', 'aggregate': False, 'time': 1980},

]

#fg = collection.insert_many(angolaGDP)
#print(fg)

accessToElectricity = [
{'value': None, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2022'},
{'value': 48.2238540649414, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2021'},
{'value': 46.9554443359375, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2020'},
{'value': 45.6338806152344, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2019'},
{'value': 45.29, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2018'},
{'value': 42.9062423706055, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2017'},
{'value': 41.7850341796875, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2016'},
{'value': 42, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2015'},
{'value': 32, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2014'},
{'value': 38.3981781005859, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2013'},
{'value': 37.2594909667969, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2012'},
{'value': 34.6, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2011'},
{'value': 34.980052947998, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2010'},
{'value': 33.8469772338867, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2009'},
{'value': 38.49, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2008'},
{'value': 37.5, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2007'},
{'value': 30.5203876495361, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2006'},
{'value': 29.4483089447021, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2005'},
{'value': 28.3954849243164, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2004'},
{'value': 27.3551368713379, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2003'},
{'value': 26.320255279541, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2002'},
{'value': 20, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2001'},
{'value': 24.2388648986816, 'series': 'EG.ELC.ACCS.ZS', 'economy': 'AGO', 'aggregate': False, 'time': 'YR2000'},

]

#op = collection.insert_many(accessToElectricity)
#print(op)