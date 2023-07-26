import wbgapi as wb
import pandas as pd

for silo in wb.data.fetch('EG.ELC.ACCS.ZS','BFA'):
    print(silo)

