import wbgapi as wb
import pandas as pd

info = wb.source.info()
# print(info)
info2 = wb.series.info('NY.GDP.PCAP.CD')
country = wb.economy.info(['CAN', 'USA', 'MEX'])
print(country)
nigerians = wb.economy.info(q='nigeria')
print(nigerians)

yeah = wb.economy.info(wb.income.members('LIC'))
print(yeah)

division = wb.topic.info()
sectorHealthCare = wb.series.info(topic=1)
print(division)
print(sectorHealthCare)
talk = wb.search('fossil fuels')

#wb.data.DataFrame('SP.POP.TOTL', time=2015, labels=True).reset_index()

for buns in wb.data.fetch('EG.ELC.ACCS.ZS','CHN'):
    print(buns)

