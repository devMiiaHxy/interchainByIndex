import wbgapi as wb
import pandas as pd

for tye in wb.data.fetch('EG.ELC.ACCS.ZS', 'BWA'):
    print(tye)